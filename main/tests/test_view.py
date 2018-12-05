from django.test import TestCase
from django.urls import reverse
from django.urls import resolve
from ..views import IndexListView, LiveListView, AllTipsListView, BestTipsListView, contact
from ..models import BestTips, OurFavouritePick
from ..forms import ContactForm

class IndexListViewTests(TestCase):

    def setUp(self):
        self.besttips = BestTips.objects.create(kick_of_Time='18:00', home_Team='Chelsea', home_Percent='70', home_Odd='1.66', draw_Odd='4', away_Odd='3', away_Team='Watford', away_Percent='32', prediction='home win')
        url = reverse('index')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, IndexListView)

class AllTipsListViewTests(TestCase):

    def setUp(self):
        self.besttips = BestTips.objects.create(kick_of_Time='18:00', home_Team='Chelsea', home_Percent='70', home_Odd='1.66', draw_Odd='4', away_Odd='3', away_Team='Watford', away_Percent='32', prediction='home win')
        url = reverse('alltips')
        self.response = self.client.get(url)

    def test_alltips_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_alltips_url_resolves_home_view(self):
        view = resolve('/footballtips/')
        self.assertEquals(view.func.view_class, AllTipsListView)

class BestTipsListViewTests(TestCase):

    def setUp(self):
        self.favouritetips = OurFavouritePick.objects.create(kick_of_Time='18:00', home_Team='Chelsea', win_Percent='70', win_Odd='1.66', league='England', our_Pick='Chelsea', away_Team='Watford', result='home win')
        url = reverse('besttips')
        self.response = self.client.get(url)

    def test_best_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_best_url_resolves_home_view(self):
        view = resolve('/favouritetips/')
        self.assertEquals(view.func.view_class, BestTipsListView)


class LiveListViewTest(TestCase):
    def setUp(self):
        url = reverse('livescore')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/livescore/')
        self.assertEquals(view.func, LiveListView)

class contactTests(TestCase):
    def setUp(self):
        url = reverse('contact')
        self.response = self.client.get(url)

    def test_contact_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_contact_url_resolves_signup_view(self):
        view = resolve('/contact/')
        self.assertEquals(view.func, contact)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, ContactForm)
    def test_form_inputs(self):
        self.assertContains(self.response, '<input', 4)
        self.assertContains(self.response, 'type="text"', 2)
        self.assertContains(self.response, 'type="email"', 1)


class SuccessfulSignUpTests(TestCase):
    def setUp(self):
            url = reverse('contact')
            data = {
                'name': 'john',
                'email': 'mbogokennedymn@gmail.com',
                'phone': '0705171999',
                'message': 'test message'
            }
            self.response = self.client.post(url, data)
            self.contact_url = reverse('contact')


class InvalidContactTests(TestCase):
    def setUp(self):
        url = reverse('contact')
        self.response = self.client.post(url, {})  
    def test_contact_status_code(self):
        
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertFalse(form.errors)



