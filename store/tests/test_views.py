from unittest import skip
from ..views import *
from django.http import HttpRequest
from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from store.models import Category, Product
from django.urls import reverse



class TestViewResponses(TestCase):
    def setUp(self) -> None:
        self.c = Client()
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data = Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                                           slug='django-beginners', price='20.00', image='django')
        self.factory = RequestFactory()

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts..
        To test the home page working
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test the get_absolut_url of product detail model
        """
        response = self.c.get(reverse("store:product_details", args=['django-beginners']))
        self.assertEqual(response.status_code, 200)


    def test_category_detail_url(self):
        """
        Test the get_absolut_url of Category detail model
        """
        response = self.c.get(reverse("store:category_list", args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        """
        To test the view directly by sending hhtp request.
        """
        request = HttpRequest()
        response = all_products(request)   #view of store's views.py file
        html = response.content.decode('utf8')
        # print(html)
        self.assertIn('<title>Home</title>',html)
        self.assertEqual(response.status_code, 200)


    def test_view_function(self):
        request = self.factory.get('/item/django-beginners')
        response = all_products(request)
        self.assertEqual(response.status_code, 200)
# def test_homepage_url(self):
#     """
#     Test home page response status..
#     """
#     response = self.Client.get('/')