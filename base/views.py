from django.shortcuts import render
from django.http import HttpResponse


rooms = [
    {
        'id': 1,
        'name': 'Eck'
    },
    {
        'id': 2,
        'name': 'Eok'
    },
    {
        'id': 3,
        'name': 'Eoink'
    },
    {
        'id': 4,
        'name': 'Eoirick'
    },
    {
        'id': 5,
        'name': 'EoCa'
    },
    {
        'id': 6,
        'name': 'Eoin V'
    },
    {
        'id': 7,
        'name': 'Essel'
    }
]


# Create your views here.
def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    return render(request, 'base/room.html')
