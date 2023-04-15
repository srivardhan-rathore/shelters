from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # App Urls
    path('', include('home.urls')),
    path('app/', include(('main.urls', 'main'), namespace='main')),
    path('accounts/', include('accounts.urls')),

    # Auth Provider
    path('auth/', include('social_django.urls', namespace='social')),
]

