from django.shortcuts import render
from django.http import HttpResponse


rooms = [
    {
        'id': 1,
        'name': 'Eoin Carrick'
    },    {
        'id': 1,
        'name': 'Eoin Carrick'
    },    {
        'id': 1,
        'name': 'Eoin Carrick'
    },    {
        'id': 1,
        'name': 'Eoin Carrick'
    },    {
        'id': 1,
        'name': 'Eoin Carrick'
    },    {
        'id': 1,
        'name': 'Eoin Carrick'
    }
]


# Create your views here.
def home(request):
    return render(request, 'home.html')


def room(request):
    return render(request, 'room.html')
