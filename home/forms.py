from django.forms import ModelForm
from .models import Contacts


class ContactForm(ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'
