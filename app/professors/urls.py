from django.urls import path
from . import views
from django.views import generic

app_name = 'professors'

urlpatterns = [
    path('', views.ProfessorList.as_view(), name='list'),
    path('detail/<int:pk>/', views.ProfessorDetail.as_view(), name='detail'),
    path('create/', views.ProfessorCreateView.as_view(), name='create'),
    path('create2/', views.ProfessorCreateView2.as_view(), name='create2'),
    path('update/<int:pk>', views.ProfessorUpdateView.as_view(), name='update'),
    path('update2/<int:pk>', views.ProfessorUpdateView2.as_view(), name='update2'),
]
