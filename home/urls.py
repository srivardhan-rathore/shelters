from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("policy/<called>", views.PolicyView.as_view(), name="policies"),
    path("contact/", views.ContactView.as_view(), name="contact"),
]