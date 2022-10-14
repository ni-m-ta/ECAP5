from django.shortcuts import render
from django.views.generic import TemplateView
from signup.forms import AccountForm, AddAccountForm
from django.core.files.storage import FileSystemStorage

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Myaccount
@login_required
def myaccount(request):
    params = {"UserID": request.user, }
    return render(request, "myaccount.html", context=params)
