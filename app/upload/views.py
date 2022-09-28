from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse


def index1(request):
    params = {
        'title': 'No.1',
        'msg': 'Hello world!',
        'link': 'Another',
        'page': 'go to page2',
    }
    return render(request, 'upload.html', params)


def index2(request):
    params = {
        'title': 'No.2',
        'msg': 'Welcome to Japan!',
        'link': 'Index',
        'page': 'go to page1',
    }
    return render(request, 'upload.html', params)
