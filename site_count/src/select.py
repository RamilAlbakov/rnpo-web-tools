"""Select site data from network live for rendering on the web page."""

import os

import cx_Oracle
from dotenv import load_dotenv

load_dotenv('.env')


def create_row_sqls(row_header, field):
    """
    Create sql commands to get data for each row in result table.

    Args:
        row_header: string
        field: string

    Returns:
        dict
    """
    main_sql = """
        SELECT
            COUNT(site)
        FROM
            webtool_sites
    """

    networks = ['2G', '3G', '4G', '5G', 'total']

    if field == 'operator':
        field_condition = f"WHERE operator='{row_header}'"
    elif field == 'vendor':
        field_condition = f"WHERE vendor='{row_header}'"
    elif field == 'region':
        field_condition = f"WHERE region='{row_header}'"

    conditions = {
        '2G': f"{field_condition} and gsm='1'",
        '3G': f"{field_condition} and wcdma='1'",
        '4G': f"{field_condition} and lte='1'",
        '5G': f"{field_condition} and nr5g='1'",
        'total': field_condition,
    }

    return {
        network: f'{main_sql} {conditions[network]}' for network in networks
    }


def select_field_data(cursor, field):
    """
    Select data for each field value.

    Args:
        cursor: cx_Oracle connection cursor
        field: string

    Returns:
        list
    """
    if field == 'all':
        return cursor.execute('SELECT * FROM webtool_sites').fetchall()
    field_sql = f"""
        SELECT
            {field}
        FROM
            webtool_sites
        WHERE
            {field} is not null
        GROUP BY
            {field}
    """
    rows = [row[0] for row in cursor.execute(field_sql).fetchall()]
    select_results = []
    for row in sorted(rows):
        row_data = {'header': row}
        sqls = create_row_sqls(row, field)
        for network, sql in sqls.items():
            row_data[network] = cursor.execute(sql).fetchone()[0]
        select_results.append(row_data)
    return select_results


def select(field):
    """
    Select site data for operator, vendor or region field.

    Args:
        field: string

    Returns:
        list of dicts
    """
    atoll_dsn = cx_Oracle.makedsn(
        os.getenv('ATOLL_HOST'),
        os.getenv('ATOLL_PORT'),
        service_name=os.getenv('SERVICE_NAME'),
    )
    with cx_Oracle.connect(
        user=os.getenv('ATOLL_LOGIN'),
        password=os.getenv('ATOLL_PASSWORD'),
        dsn=atoll_dsn,
    ) as connection:
        cursor = connection.cursor()
        return select_field_data(cursor, field)
