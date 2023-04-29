from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView as BaseLogoutView
from django.views.generic import FormView, TemplateView
from django.conf import settings
from django.core.mail import EmailMessage
from .models import UserInfo
import threading


class CheckNewUser(TemplateView):
    template_name = 'accounts/add_phone.html'

    def get(self, request, *args, **kwargs):
        date_joined = request.user.date_joined.strftime('%Y-%m-%d %H:%M')
        last_login = request.user.last_login.strftime('%Y-%m-%d %H:%M')
        if date_joined == last_login:
            print("yes")
            EmailThread("Welcome To ShelterSearch", f"Hey {request.user.first_name},"
                                                    f" Welcome to ShelterSearch", [request.user.email]).start()
            return render(request, self.template_name)
        return redirect('main:taxi')

    def post(self, request):
        user = request.user
        phone = request.POST.get('phone')
        user_info = UserInfo.objects.create(user=user, phone=phone)
        user_info.save()
        return redirect("main:taxi")


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


class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list, html_message=None):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        self.html_message = html_message
        threading.Thread.__init__(self)

    def run(self):
        print("Yo")
        message = EmailMessage(self.subject, self.html_content, settings.DEFAULT_FROM_EMAIL,
                               self.recipient_list)
        print(message)
        message.content_subtype = "html"
        print(message)
        print(message.send(fail_silently=False))

        print(message.to)
