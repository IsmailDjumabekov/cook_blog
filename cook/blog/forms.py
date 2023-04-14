from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Comment

# Атрибут widgets используется для изменения отображения полей формы
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # eхclude исключеням потому что эти поля должны заполняться автоматически на серверной стороне.
        exclude = ['create_at', 'post']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email'}),
            'website': forms.TextInput(attrs={'placeholder': 'website'}),
            'message': forms.Textarea(attrs={'placeholder': 'message'}),

        }