from django.shortcuts import render, HttpResponse
from asgiref.sync import sync_to_async
from django.views.generic import TemplateView
from .models import Partners, Testimonials, ServiceInfo
from django.conf import settings
from django.core.mail import EmailMessage
from .forms import ContactForm
import asyncio
import threading


class HomeView(TemplateView):
    template_name = "home/index.html"

    def get(self, request, **kwargs):
        partners = Partners.objects.all()
        testimonials = Testimonials.objects.all()
        for t in testimonials:
            z = []
            z.extend(iter(range(1, t.rating + 1)))
            t.rating = z
        service_info = ServiceInfo.objects.first()
        context = {'partners': partners, 'testimonials': testimonials, 'service_info': service_info}
        return render(request, "home/index.html", context)

    @sync_to_async
    def get_partners(self):
        return Partners.objects.all()

    @sync_to_async
    def get_serviceInfo(self):
        return ServiceInfo.objects.first()

    @sync_to_async
    def get_testimonials(self):
        testimonials = Testimonials.objects.all()
        for t in testimonials:
            z = []
            z.extend(iter(range(1, t.rating + 1)))
            t.rating = z
        return testimonials


class ContactView(TemplateView):
    template_name = "home/contact.html"
    form_class = ContactForm

    def get(self, request, **kwargs):
        return render(request, self.template_name)

    def post(self, request):
        form = self.form_class(request.POST)
        if not form.is_valid():
            return render(request, self.template_name)
        form.save()
        email_subject = f'New contact: {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
        email_message = f'Name: {form.cleaned_data["name"]} \nMessage: {form.cleaned_data["message"]}'
        EmailThread(email_subject, email_message, ["srivardhan.singh.rathore@gmail.com"]).start()
        return HttpResponse(status=200)


class PolicyView(TemplateView):
    template_dir = "home/policies/"

    def get(self, request, called):
        if called == "terms_of_service":
            return render(request, f"{self.template_dir}terms_of_service.html")
        elif called == "privacy_policy":
            return render(request, f"{self.template_dir}privacy_policy.html")
        elif called == "refund_policy":
            return render(request, f"{self.template_dir}refund_policy.html")
        else:
            return render(request, "home/404.html")


class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list, html_message=None):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        self.html_message = html_message
        threading.Thread.__init__(self)

    def run(self):
        message = EmailMessage(self.subject, self.html_content, settings.CONTACT_EMAIL,
                               self.recipient_list)
        message.content_subtype = "html"
        message.send(fail_silently=False)
        print(message.to)
