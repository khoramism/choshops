from django.test import TestCase
from . import forms
# Create your tests here.
class TestForm(TestCase):
    pass


class TestPage(TestCase):
    def test_user_signup_page_loads_correctly(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/register.html")
        self.assertContains(response, "Account")
        self.assertIsInstance(
            response.context["form"], forms.UserCreationForm
        )
    def test_user_signup_page_submission_works(self):
        post_data = {
            "email": "user@domain.com",
            "password1": "abcabcabc",
            "password2": "abcabcabc",
        }
        with patch.object(
            forms.UserCreationForm, "send_mail"
        ) as mock_send:
            response = self.client.post(
                reverse("register"), post_data
            )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            models.User.objects.filter(
                email="user@domain.com"
            ).exists()
        )
        self.assertTrue(
            auth.get_user(self.client).is_authenticated
        )
        mock_send.assert_called_once()

### TEST WITH FACTORY BOY 
'''
import factory
import factory.fuzzy
from . import models

class UserFactory(factory.django.DjangoModelFactory):
    email="user@site.com"
    class Meta:
        model = models.Account
        django_get_or_create = ('email',)
class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.fuzzy.FuzzyDecimal(1.0, 1000.0, 2)
    class Meta:
        model = models.Product
class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Address'''