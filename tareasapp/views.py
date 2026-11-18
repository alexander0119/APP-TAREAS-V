from django.shortcuts import render
from .models import Tarea
from django.http import HttpResponse

# def inicio(request):
#     return HttpResponse("Hola, esta es mi aplicación de tareas")


def inicio(request):
    tareas = Tarea.objects.all()

    return render(request, "tareasapp/inicio.html", {"tareas": tareas})
