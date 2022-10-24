from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.views import generic

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q


class IndexView(generic.ListView):
    model = Article

    def get_queryset(self):
        q_word = self.request.GET.get('query')

        selected_college = self.request.GET.get('college')
        selected_professor = self.request.GET.get('professor')
        selected_course = self.request.GET.get('course')

        if q_word:
            if selected_college and selected_professor and selected_course:
                object_list = Article.objects.filter(
                    Q(college__icontains=q_word) | Q(professor__icontains=q_word) | Q(course__icontain=q_word)
                )
            elif selected_college and selected_professor:
                object_list = Article.objects.filter(
                    Q(college__icontains=q_word) | Q(professor__icontains=q_word)
                )
            elif selected_professor and selected_course:
                object_list = Article.objects.filter(
                    Q(professor__icontains=q_word) | Q(course__icontain=q_word)
                )
            elif selected_course and selected_college:
                object_list = Article.objects.filter(
                    Q(course__icontain=q_word) | Q(college__icontains=q_word)
                )
            elif selected_college:
                object_list = Article.objects.filter(
                    Q(college__icontains=q_word)
                )
            elif selected_professor:
                object_list = Article.objects.filter(
                    Q(professor__icontains=q_word)
                )
            else:
                object_list = Article.objects.filter(
                    Q(course__icontains=q_word)
                )
        else:
            object_list = Article.objects.all()

        return object_list


class DetailView(generic.DetailView):
    model = Article


class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Article
    fields = ['college', 'comment', 'professor_first', 'professor_last', 'course', 'textbook', 'attendance', 'satisfaction', 'hard', ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)


class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Article
    fields = ['college', 'comment', 'professor_first', 'professor_last', 'course', 'textbook', 'attendance', 'satisfaction', 'hard', ]

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.author != self.request.user:
            raise PermissionDenied('You do not have permission to edit.')

        return super(UpdateView, self).dispatch(request, *args, **kwargs)


class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Article
    success_url = reverse_lazy('classes:index')
