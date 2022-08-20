from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
from .forms import FormRoom


# rooms = [
#     {
#         'id': 1,
#         'name': 'Eck'
#     },
#     {
#         'id': 2,
#         'name': 'Eok'
#     },
#     {
#         'id': 3,
#         'name': 'Eoink'
#     },
#     {
#         'id': 4,
#         'name': 'Eoirick'
#     },
#     {
#         'id': 5,
#         'name': 'EoCa'
#     },
#     {
#         'id': 6,
#         'name': 'Eoin V'
#     },
#     {
#         'id': 7,
#         'name': 'Essel'
#     }
# ]


# Create your views here.

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}

    return render(request, 'base/room.html', context)


def create_room(request):
    form = FormRoom()
    if request.method == 'POST':
        print(request.POST)
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

# the view.py is used to render a function that get viewed by the user.
# 1. Templates(html,css,and javascript)
# 2. we can pass data inside the function to be rendered.
# 3. the fucntion takes one by default, in this case, is the "request"
