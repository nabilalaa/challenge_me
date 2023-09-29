from django import forms
# from .models import Form


class Forms(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    # email = forms.EmailField(placeholder="name")
    # phone = forms.CharField(placeholder="name")
    # messages = forms.TextField(placeholder="name")
