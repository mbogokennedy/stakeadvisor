from django.test import TestCase
from ..forms import SignUpForm, UserForm, ProfileForm

class SignUpFormTest(TestCase):
    def test_form_has_fields(self):
        form = SignUpForm()
        expected = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'phone_number']
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)

class UserFormTest(TestCase):
    def test_form_has_fields(self):
        form = SignUpForm()
        expected = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'phone_number']
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)
class ProfileFormTest(TestCase):
    def test_form_has_fields(self):
        form = SignUpForm()
        expected = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'phone_number']
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)


