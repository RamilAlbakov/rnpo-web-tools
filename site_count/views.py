from django.http import FileResponse
from django.shortcuts import render

from .src.count_sites import count
from .src.fill_table import fill_table
from .src.select import select


def count_sites(request):
    context = count()
    return render(request, 'site_count/index.html', context)


def download_sites(request):
    sql_data = select('all')
    table_path = fill_table(sql_data)
    kcell_sites = open(table_path, 'rb')
    return FileResponse(kcell_sites)
