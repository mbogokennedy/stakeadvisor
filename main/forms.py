from django import forms

class ContactForm (forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    phone = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)