from django import forms
from .models import ContactModel
from captcha.fields import CaptchaField
class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = ContactModel
        fields = '__all__'