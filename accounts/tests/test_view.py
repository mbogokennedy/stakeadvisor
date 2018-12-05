from django.contrib.auth.models import User
from ..forms import SignUpForm,  UserForm, ProfileForm
from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from ..views import Signup, ProfileSettings
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from ..models import Profile
from django.contrib.auth import views as auth_views
from django.core import mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

class SignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEquals(view.func, Signup)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, SignUpForm)
    def test_form_inputs(self):
        self.assertContains(self.response, '<input', 8)
        self.assertContains(self.response, 'type="text"', 4)
        self.assertContains(self.response, 'type="email"', 1)
        self.assertContains(self.response, 'type="password"', 2)


class SuccessfulSignUpTests(TestCase):
    def setUp(self):
            url = reverse('signup')
            data = {
                'first_name': 'john',
                'last_name': 'moses',
                'email': 'mbogokennedymn@gmail.com',
                'username': 'john',
                'password1': 'abcdef123456',
                'password2': 'abcdef123456',
                'phone_number': '0705171999'
            }
            self.response = self.client.post(url, data)
            self.index_url = reverse('index')
    def test_redirection(self):
        self.assertRedirects(self.response, self.index_url)

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())

    def test_user_authentication(self):
        response = self.client.get(self.index_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)


class InvalidSignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.post(url, {})  
    def test_signup_status_code(self):
        
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

    def test_dont_create_user(self):
        self.assertFalse(User.objects.exists())


class PasswordResetTests(TestCase):
    def setUp(self):
        url = reverse('password_reset')
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/accounts/reset/')
        self.assertEquals(view.func.view_class, auth_views.PasswordResetView)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, PasswordResetForm)

    def test_form_inputs(self):
        '''
        The view must contain two inputs: csrf and email
        '''
        self.assertContains(self.response, '<input', 3)
        self.assertContains(self.response, 'type="email"', 1)


class InvalidPasswordResetTests(TestCase):
    def setUp(self):
        url = reverse('password_reset')
        self.response = self.client.post(url, {'email': 'donotexist@email.com'})

    def test_redirection(self):
        '''
        Even invalid emails in the database should
        redirect the user to `password_reset_done` view
        '''
        url = reverse('password_reset_done')
        self.assertRedirects(self.response, url)

    def test_no_reset_email_sent(self):
        self.assertEqual(0, len(mail.outbox))

class PasswordResetDoneTests(TestCase):
    def setUp(self):
        url = reverse('password_reset_done')
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/accounts/reset/done/')
        self.assertEquals(view.func.view_class, auth_views.PasswordResetCompleteView)


class PasswordResetConfirmTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='john', email='john@doe.com', password='123abcdef')

        
        self.uid = urlsafe_base64_encode(force_bytes(user.pk)).decode()
        self.token = default_token_generator.make_token(user)

        url = reverse('password_reset_confirm', kwargs={'uidb64': self.uid, 'token': self.token})
        self.response = self.client.get(url, follow=True)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/accounts/reset/{uidb64}/{token}/'.format(uidb64=self.uid, token=self.token))
        self.assertEquals(view.func.view_class, auth_views.PasswordResetConfirmView)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, SetPasswordForm)

    def test_form_inputs(self):
        '''
        The view must contain two inputs: csrf and two password fields
        '''
        self.assertContains(self.response, '<input', 3)
        self.assertContains(self.response, 'type="password"', 2)


class InvalidPasswordResetConfirmTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='john', email='john@doe.com', password='123abcdef')
        uid = urlsafe_base64_encode(force_bytes(user.pk)).decode()
        token = default_token_generator.make_token(user)

        '''
        invalidate the token by changing the password
        '''
        user.set_password('abcdef123')
        user.save()

        url = reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_html(self):
        password_reset_url = reverse('password_reset')
        self.assertContains(self.response, 'invalid password reset link')
        self.assertContains(self.response, 'href="{0}"'.format(password_reset_url))


class PasswordResetCompleteTests(TestCase):
    def setUp(self):
        url = reverse('password_reset_complete')
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/accounts/reset/complete/')
        self.assertEquals(view.func.view_class, auth_views.PasswordResetCompleteView)

# class SuccessfulPasswordResetTests(TestCase):
#     def setUp(self):
#         email = 'john@doe.com'
#         User.objects.create_user(username='john', email=email, password='123abcdef')
#         url = reverse('password_reset')
#         self.response = self.client.post(url, {'email': email})

#     def test_redirection(self):
#         '''
#         A valid form submission should redirect the user to `password_reset_done` view
#         '''
#         url = reverse('password_reset_done')
#         self.assertRedirects(self.response, url)

#     def test_send_password_reset_email(self):
#         self.assertEqual(1, len(mail.outbox))

# class PasswordResetMailTests(TestCase):
#     def setUp(self):
#         User.objects.create_user(username='john', email='john@doe.com', password='123')
#         self.response = self.client.post(reverse('password_reset'), { 'email': 'john@doe.com' })
#         self.mail = mail.outbox[0]

#     def test_email_subject(self):
#         self.assertEqual(self.mail.subject, '[Stake Advisor] Please reset your password')

#     def test_email_body(self):
#         context = self.response.context
#         token = context.get('token')
#         uid = context.get('uid')
#         password_reset_token_url = reverse('password_reset_confirm', kwargs={
#             'uidb64': uid,
#             'token': token
#         })
#         self.assertIn(self.mail.body, password_reset_token_url)
#         self.assertIn(self.mail.body, 'john')
#         self.assertIn( self.mail.body,'john@doe.com',)

#     def test_email_to(self):
#         self.assertEqual(self.mail.to, ['john@doe.com',])

# class LoginRequiredPasswordChangeTests(TestCase):
#     def test_redirection(self):
#         self.url = reverse('password_change')
#         self.response = self.client.get(self.url)
#         login_url = reverse('login')
#         self.assertRedirects(self.response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))

class PasswordChangeTestCase(TestCase):
    def setUp(self, data={}):
        self.user = User.objects.create_user(username='john', email='john@doe.com', password='old_password')
        self.url = reverse('password_change')
        self.client.login(username='john', password='old_password')
        self.response = self.client.post(self.url, data)


class SuccessfulPasswordChangeTests(PasswordChangeTestCase):
    def setUp(self):
        super().setUp({
            'old_password': 'old_password',
            'new_password1': 'new_password',
            'new_password2': 'new_password',
        })

    def test_redirection(self):
        '''
        A valid form submission should redirect the user
        '''
        self.assertRedirects(self.response, reverse('password_change_done'))

    def test_password_changed(self):
        '''
        refresh the user instance from database to get the new password
        hash updated by the change password view.
        '''
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('new_password'))

    def test_user_authentication(self):
        '''
        Create a new request to an arbitrary page.
        The resulting response should now have an `user` to its context, after a successful sign up.
        '''
        response = self.client.get(reverse('index'))
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)


class InvalidPasswordChangeTests(PasswordChangeTestCase):
    def test_status_code(self):
        '''
        An invalid form submission should return to the same page
        '''
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

    def test_didnt_change_password(self):
        '''
        refresh the user instance from the database to make
        sure we have the latest data.
        '''
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('old_password'))



