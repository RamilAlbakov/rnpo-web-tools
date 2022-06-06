"""Views for site_count app."""

from django.http import HttpResponse
from django.shortcuts import render

from .src.count_sites import count
from .src.fill_table import fill_table
from .src.select import select


def count_sites(request):
    """
    Count sites by operator, vensor or region and render tables.

    Args:
        request: http get request

    Returns:
        http response
    """
    context = count()
    return render(request, 'site_count/index.html', context)


def download_sites(request):
    """
    Send a excel file with all sites for downloading.

    Args:
        request: http post request

    Returns:
        http response with a excel file
    """
    sql_data = select('all')
    table_path = fill_table(sql_data)

    with open(table_path, 'rb') as attachment:
        file_data = attachment.read()
        response = HttpResponse(file_data, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="site_data.xlsx"'
        return response
