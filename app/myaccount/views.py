from django.shortcuts import render
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required


# Myaccount
@login_required
def myaccount(request):
    params = {"UserID": request.user, }
    return render(request, "myaccount.html", params)
