from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home/home.html"


class PrivacyPolicyView(TemplateView):
    template_name = "home/privacypolicy.html"


class ContactFormView(TemplateView):
    template_name = "home/contactform.html"


class SiteMapView(TemplateView):
    template_name = "home/sitemap.html"
