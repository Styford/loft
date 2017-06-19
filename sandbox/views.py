from django.shortcuts import redirect
from django.shortcuts import render_to_response
import os


# Create your views here.
def widget(request):

    return render_to_response("sandbox.html")


def open_extprog(request, id_prog):

    if id_prog == "1":
        os.startfile(r'c:/igel.jpg')
    if id_prog == "2":
        os.startfile(r'c:/igel.jpg')
    if id_prog == "3":
        os.startfile(r'c:/igel.jpg')
    return redirect ('/sandbox/')
