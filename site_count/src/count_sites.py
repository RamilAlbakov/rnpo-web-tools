"""Count total number of sites and Kcell sites."""

from .select import select


def count():
    """
    Count total number of sites and Kcell sites.

    Returns:
        dict
    """
    operator_rows = select('operator')
    vendor_rows = select('vendor')
    region_rows = select('region')

    total_row = {
        '2G': 0,
        '3G': 0,
        '4G': 0,
        '5G': 0,
        'total': 0,
    }

    for row in operator_rows:
        total_row['2G'] += row['2G']
        total_row['3G'] += row['3G']
        total_row['4G'] += row['4G']
        total_row['5G'] += row['5G']
        total_row['total'] += row['total']

    kcell_sites = list(filter(
        lambda operator_row: operator_row['header'] == 'Kcell',
        operator_rows,
    ))[0]

    return {
        'operator_rows': operator_rows,
        'vendor_rows': vendor_rows,
        'region_rows': region_rows,
        'total_row': total_row,
        'kcell_sites': kcell_sites,
    }
