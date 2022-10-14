from django.shortcuts import render
from django.views.generic import TemplateView
from signup.forms import AccountForm, AddAccountForm
from django.core.files.storage import FileSystemStorage

from django.contrib.auth import authenticate, login, logout
from myaccount.views import myaccount
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def Login(request):
    # POST
    if request.method == 'POST':
        # To get userID & password
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        # The fanction to validate in Django
        user = authenticate(username=ID, password=Pass)

        # To validate users
        if user:
            # To check whether the user is activated or not
            if user.is_activate:
                # login
                login(request, user)
                # To go to homepage
                return HttpResponseRedirect(reverse('myaccount'))
            else:
                # Not users
                return HttpResponse("Your account is not validated.")
        # Fail to validate users
        else:
            return HttpResponse("Your loginID or password is wrong.")
    # To get
    else:
        return render(request, 'login.html')


# Logout
@login_required
def Logout(request):
    logout(request)
    # To go to the login screen
    return HttpResponseRedirect(reverse('Login'))
