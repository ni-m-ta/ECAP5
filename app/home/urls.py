from django.urls import path
from . import views


app_name = 'home'

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("privacypolicy/", views.PrivacyPolicyView.as_view(), name="privacypolicy"),
    path("contactform/", views.ContactFormView.as_view(), name="contactform"),
    path("sitemap/", views.SiteMapView.as_view(), name="sitemap")
]
