from django.test import TestCase
from account.models import Accont
from .models import Address 

# Create your tests here.
class TestView(TestCase):
    def test_address_list_page_returns_only_owned(self):
        user1 = Account.objects.create_user(
            "user1", "pw432joij"
        )
        user2 = Account.objects.create_user(
            "user2", "pw432joij"
        )
        Address.objects.create(
            account=user1,
            name="john kimball",
            address1="flat 2",
            address2="12 Stralz avenue",
            city="London",
            country="ir",
        )
        Address.objects.create(
            account=user2,
            name="marc kimball",
            address1="123 Deacon road",
            city="London",
            country="us",
        )
        self.client.force_login(user2)
        response = self.client.get(reverse("address_list"))
        self.assertEqual(response.status_code, 200)
        
        address_list = Address.objects.filter(account=user2)
        self.assertEqual(
            list(response.context["object_list"]),
            list(address_list),
        )
    def test_address_create_stores_user(self):
        user1 = models.User.objects.create_user(
            "user1", "pw432joij"
        )
        post_data = {
            "name": "john kercher",
            "address1": "1 av st",
            "address2": "",
            "zip_code": "MA12GS",
            "city": "Manchester",
            "country": "ir",
        }
        self.client.force_login(user1)
        self.client.post(
            reverse("address_create"), post_data
        )
        self.assertTrue(
            Address.objects.filter(account=user1).exists()
        )