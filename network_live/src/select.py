"""Select cell data from network_live db."""

import os

import cx_Oracle
from dotenv import load_dotenv

load_dotenv('.env')


def select_data(technologies):
    """
    Select cell data from network_live.

    Args:
        technologies: list

    Returns:
        list of tuples
    """
    network_live_tables = {
        'lte': 'LTECELLS2',
        'wcdma': 'WCDMACELLS2',
        'gsm': 'GSMCELLS2',
        'nr': 'NRCELLS',
    }
    network_live_data = {}

    network_live_dsn = cx_Oracle.makedsn(
        os.getenv('ATOLL_HOST'),
        os.getenv('ATOLL_PORT'),
        service_name=os.getenv('SERVICE_NAME'),
    )
    with cx_Oracle.connect(
        user=os.getenv('ATOLL_LOGIN'),
        password=os.getenv('ATOLL_PASSWORD'),
        dsn=network_live_dsn,
    ) as connection:
        cursor = connection.cursor()
        for technology in technologies:
            sql_select = 'SELECT * FROM {table}'.format(table=network_live_tables[technology])
            network_live_data[technology] = cursor.execute(sql_select).fetchall()

    return network_live_data
