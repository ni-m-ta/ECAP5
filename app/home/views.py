from django.views.generic import TemplateView


class home(TemplateView):
    template_name = "home/home.html"


class privacypolicy(TemplateView):
    template_name = "home/privacypolicy.html"
