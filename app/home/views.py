from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
    params = {
        'title': 'This is home',
    }
    return render(request, "home.html", params)
