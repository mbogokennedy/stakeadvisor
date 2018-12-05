from random import choice, randint

from django import forms
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from pagedown.widgets import PagedownWidget
from simplemathcaptcha.fields import MathCaptchaField
from django.contrib.auth.models import User
from .models import Comment
from .settings import MAX_LENGTH_TEXTAREA


class UserCommentForm(forms.ModelForm):
    error_msg = _(
        'Cannot be empty nor only contain spaces. Please fill in the field.')

    bodytext = forms.Textarea()

    class Meta:
        model = Comment
        fields = ["bodytext"]
        if MAX_LENGTH_TEXTAREA is not None:
            widgets = {
                'bodytext': forms.Textarea(attrs={'maxlength': MAX_LENGTH_TEXTAREA})
            }

    def clean_bodytext(self):
        bodytext = self.cleaned_data.get('bodytext')
        if bodytext:
            if not bodytext.strip():
                raise forms.ValidationError(self.error_msg)
        return bodytext
