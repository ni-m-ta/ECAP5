from django.urls import path
from . import views
from .models import Class, Evaluation
from django.views import generic

app_name = 'classes'

urlpatterns = [
    path('', views.ClassListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.ClassDetailView.as_view(), name='detail'),
    path('create/', views.ClassCreateView.as_view(), name='create'),
    path('create2/', views.ClassCreateView2.as_view(), name='create2'),
    path('update/<int:pk>', views.ClassUpdateView.as_view(), name='update'),
    path('update2/<int:pk>', views.ClassUpdateView2.as_view(), name='update2'),
    path('delete/<int:pk>', views.ClassDeleteView.as_view(), name='delete'),
]
