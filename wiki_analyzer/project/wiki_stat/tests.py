from django.test import SimpleTestCase, TestCase, Client
from .views import get_data
from django.urls import reverse, resolve
from django.core import serializers
import json

# Test will be run to primarly check my own code.

class TestViews(TestCase):
    def test_wiki_stat_GET(self):
        client = Client()
        response = client.get(reverse('detail', args = ['string_']))
        self.assertEqual(response.status_code,200)

class TestUrls(SimpleTestCase):
    # Check if the actual url named detail is attached to the view function get_data
    def test_detail_url_resolved(self):
        url = reverse('detail', args = ['string_'])
        self.assertEquals(resolve(url).func,get_data)

class TestService(SimpleTestCase):
    # Check the response of service from an exemple and the status code for an exemple
    def setUp(self):
        self.client = Client()
        self.detail_url = reverse('detail',args = ['otan'])
    def test_service_respnse(self):
        self.assertEquals(self.client.get(self.detail_url).status_code, 200)
        tester = True
        if not '"quotient":0.4444444444444444' in str(self.client.get(self.detail_url).content):
            tester = False
        self.assertEquals(True,tester)
        