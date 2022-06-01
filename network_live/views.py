"""network_live app views."""

from django.http import HttpResponse
from django.shortcuts import render

from .src.excel import create_excel
from .src.select import select_data


def network_live(request):
    """
    For GET request render form for selecting technologies.

    For POST request send an excel file with cells for requested technologies.

    Args:
        request: http request from client

    Returns:
        http response
    """
    if request.method == 'POST':
        technologies = request.POST.getlist('technologies[]')
        network_live_data = select_data(technologies)
        file_path = create_excel(network_live_data)

        with open(file_path, 'rb') as attachment:
            file_data = attachment.read()
            response = HttpResponse(file_data, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="kcell_cells.xlsx"'
            return response
    return render(request, 'network_live/tables_form.html')
