from django.urls import path, include
from social_django.urls import urlpatterns as social_django_urlpatterns
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.LogInView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('profile/', views.ProfileView.as_view(), name="profile")
]

urlpatterns += social_django_urlpatterns
