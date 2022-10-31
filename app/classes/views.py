from django.shortcuts import render
from django.http import HttpResponse
from .models import Class, Evaluation
from django.views import generic
from django.urls import reverse

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q, Avg, Prefetch


class ClassListView(generic.ListView):
    template_name = "classes/class_list.html"
    model = Class

    def get_queryset(self):
        q_word = self.request.GET.get('query')

        selected_class = self.request.GET.get('class')
        selected_college = self.request.GET.get('college')

        if q_word:
            if selected_class and selected_college:
                class_list = Class.objects.filter(
                    Q(class__icontains=q_word) | Q(college__icontains=q_word)
                )
            elif selected_college:
                class_list = Class.objects.filter(
                    Q(college__icontains=q_word)
                )
            else:
                class_list = Class.objects.filter(
                    Q(class__icontains=q_word)
                )
        else:
            class_list = Class.objects.all()

        return class_list


class ClassDetailView(generic.DetailView):
    model = Class
    context_object_name = "class_detail"
    template_name = "classes/class_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['avgs'] = Class.objects.all().evaluation_set.all().annotate(avg_satisfactions=Avg('satisfaction'))
        return context


class ClassCreateView(LoginRequiredMixin, generic.CreateView):
    model = Class
    fields = ("course", "college")
    template_name = "classes/class_form.html"

    def get_success_url(self):
        return reverse('classes:detail', kwargs={'pk': self.object.pk})


class ClassCreateView2(LoginRequiredMixin, generic.CreateView):
    model = Evaluation
    fields = ("name", "satisfaction", "hard", "attendance", "comment")
    template_name = "classes/class_form.html"
    success_url = reverse_lazy("classes:list")

    def form_valid(self, form):
        form.instance.evaluator = self.request.user
        return super(ClassCreateView2, self).form_valid(form)


class ClassUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Class
    fields = ("course", "college")
    template_name = "classes/class_form.html"

    def get_success_url(self):
        return reverse('classes:detail', kwargs={'pk': self.object.pk})


class ClassUpdateView2(LoginRequiredMixin, generic.UpdateView):
    model = Evaluation
    fields = ("satisfaction", "hard", "attendance", "comment")
    template_name = "classes/class_form.html"
    success_url = reverse_lazy("classes:list")

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.evaluator != self.request.user:
            raise PermissionDenied('You do not have permission to edit.')

        return super(ClassUpdateView2, self).dispatch(request, *args, **kwargs)


class ClassDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Evaluation
    template_name = "classes/class_delete.html"
    success_url = reverse_lazy("classes:list")
