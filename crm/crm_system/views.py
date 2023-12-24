from django.shortcuts import render

from crm_system.models import Device, DeviceInField
from crm_system.forms import SearchForm

def mainpage(request):
    data = {
        "title": "Welcome to DjangoCRM Project",
        "data": [
            {
                "button_link": "admin",
                "name": "Заявки",
                "overview": "Работа с заявками на оборудование"
            },
            {
                "button_link": "devices",
                "name": "Оборудование",
                "overview": "Поиск Оборудования"
            },
            {
                "button_link": "devpage",
                "name": "Персонал",
                "overview": "Работа с базой персонала"
            },
            {
                "button_link": "devpage",
                "name": "Финансы",
                "overview": "Работа с финансами"
            },
        ]
    }
    return render(request, "crm_system/mainpage.html", data)


def get_devices(request):
    devices = DeviceInField.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            search_res = []
            data_for_search = form.data['data_for_search']

            if data_for_search.isdigit():
                search_res = list(DeviceInField.objects.filter(analyzer_id=int(data_for_search)))
            search_res = set(list(DeviceInField.objects.filter(customer__customer_name__contains=data_for_search)) + \
                             list(DeviceInField.objects.filter(analyzer__manufacturer__contains=data_for_search)) + \
                             list(DeviceInField.objects.filter(analyzer__model__contains=data_for_search)) + \
                             list(DeviceInField.objects.filter(owner_status__contains=data_for_search)) + search_res)

            return render(request, "crm_system/table_part.html", {"devices": search_res, "form": form})

    return render(request, "crm_system/table_part.html", {"devices": devices})


def devpage(request):
    return render(request, "crm_system/devpage.html", {"title": "Ошибка!"})