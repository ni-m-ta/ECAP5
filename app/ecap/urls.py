"""ecap_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from home.views import home
from login.views import Login
from signup.views import AccountRegistration
from login.views import Logout
from myaccount.views import myaccount

urlpatterns = [
    path('', home, name='home'),
    path('login/', Login, name='Login'),
    path('logout/', Logout, name='Logout'),
    path('signup/', AccountRegistration.as_view(), name='signup'),
    path('myaccount/', myaccount, name='myaccount'),
    path('admin/', admin.site.urls),
]


if bool(settings.DEBUG):
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
