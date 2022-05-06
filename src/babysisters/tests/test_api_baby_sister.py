from django.forms.models import model_to_dict
from django.test import TestCase
from babysisters.models.baby_sister import BabySister
from django_dynamic_fixture import N
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from babysisters.serializers import BabySisterListSerializer


class TicketTestCase(TestCase):  # pylint: disable=R0902, R0904

    def setUp(self):
        self.data_baby_sister1 = N(BabySister, name='Marcela', last_name='Castro', document='123456',
                                   phone='3255698541', date_b='2000-05-10')
        self.baby_sister1 = BabySister.objects.create(
            **model_to_dict(self.data_baby_sister1, fields=['name', 'last_name', 'document', 'phone', 'date_b']))

    def test_list(self):
        url = reverse('baby_sister_api:baby_sister-list')
        res = self.client.get(url)
        babysister = [self.baby_sister1]
        serializer = BabySisterListSerializer(babysister, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create(self):
        url = reverse('baby_sister_api:baby_sister-list')
        payload = self.data_baby_sister1
        print(payload)

        res = self.client.post(url, payload, format='json')
        print(res)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

