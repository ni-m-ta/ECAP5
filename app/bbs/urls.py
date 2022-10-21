from django.urls import path
from . import views
from .models import Article
from django.views import generic

app_name = 'bbs'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
