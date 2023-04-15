from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView as BaseLogoutView
from django.views.generic import FormView
from django.conf import settings


class LogInView(LoginView):
    template_name = 'accounts/login.html'

    def get(self, request, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            return render(request, self.template_name)


class LogoutView(LoginRequiredMixin, BaseLogoutView):
    template_name = 'accounts/logout.html'


class ProfileView(LoginRequiredMixin, FormView):
    template_name = 'accounts/profile.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name)

    # def get_initial(self):
    #     user = self.request.user
    #     initial = super().get_initial()
    #     initial['first_name'] = user.first_name
    #     initial['last_name'] = user.last_name
    #     return initial
