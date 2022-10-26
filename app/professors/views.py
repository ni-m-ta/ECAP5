from django.shortcuts import render
from django.http import HttpResponse
from .models import Professor, Evaluation
from django.views import generic
from django.urls import reverse

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q, Avg


class ProfessorList(generic.ListView):
    model = Professor
    template_name = "professors/professor_list.html"

    def get_queryset(self):
        q_word = self.request.GET.get('query')

        selected_name = self.request.GET.get('name')
        selected_college = self.request.GET.get('college')

        if q_word:
            if selected_name and selected_college:
                professor_list = Professor.objects.filter(
                    Q(name__icontains=q_word) | Q(college__icontains=q_word)
                )
            elif selected_college:
                professor_list = Professor.objects.filter(
                    Q(college__icontains=q_word)
                )
            else:
                professor_list = Professor.objects.filter(
                    Q(name__icontains=q_word)
                )
        else:
            professor_list = Professor.objects.all()

        return professor_list


class ProfessorDetail(generic.DetailView):
    model = Professor
    context_object_name = "professor_detail"
    template_name = "professors/professor_detail.html"


class ProfessorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Professor
    fields = ("name", "college")
    template_name = "professors/professor_form.html"

    def get_success_url(self):
        return reverse('professors:detail', kwargs={'pk': self.object.pk})


class ProfessorCreateView2(LoginRequiredMixin, generic.CreateView):
    model = Evaluation
    fields = ("name", "satisfaction", "hard", "attendance", "comment")
    template_name = "professors/professor_form.html"
    success_url = reverse_lazy("professors:list")


class ProfessorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Professor
    fields = ("name", "college")
    template_name = "professors/professor_form.html"

    def get_success_url(self):
        return reverse('professors:detail', kwargs={'pk': self.object.pk})


class ProfessorUpdateView2(LoginRequiredMixin, generic.UpdateView):
    model = Evaluation
    fields = ("satisfaction", "hard", "attendance", "comment")
    template_name = "professors/professor_form.html"
    success_url = reverse_lazy("professors:list")


class ProfessorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Professor
    template_name = "professors/professor_delete.html"
    success_url = reverse_lazy("professors:list")
