from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse


def login(request):
    params = {
        'title': 'login',
    }
    return render(request, "login.html", params)
