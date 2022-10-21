from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.views import generic


class IndexView(generic.ListView):
    model = Article


class DetailView(generic.DetailView):
    model = Article
