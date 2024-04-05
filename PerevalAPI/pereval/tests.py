from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, resolve
from rest_framework import status

from . import views
import json
from .models import *
from rest_framework.test import APITestCase
from .serializers import PerevalSerializer


class TestViews(TestCase):
    def test_list_perevals(self):
        client = Client()

        response = client.get(reverse('perevaladd-list'))

        self.assertEqual(response.status_code, 200)


class SubmitDataAPITests(APITestCase):
    def setUp(self):
        self.pereval_1 = Pereval.objects.create(
            user_id=MyUser.objects.create(
                email='emailtest@gmail.com',
                full_name='testName',
                phone='+8615711349804'
            ),
            beauty_title='test BT',
            title='test title',
            other_titles='tests other titles',
            connect='test connect',
            status='new',
            coords_id=Coord.objects.create(
                latitude=23.123,
                longitude=87.789,
                height=234
            ),
            level_diff=Level.objects.create(
                winter="2B",
                summer="2A",
                autumn="1B",
                spring="1B",
            )
        )
        self.image_1 = Images.objects.create(
            data='',
            title='test-title',
            pereval_id=self.pereval_1
        )

        self.pereval_2 = Pereval.objects.create(
            user_id=MyUser.objects.create(
                email='emailtesttwo@gmail.com',
                full_name='testNametwo',
                phone='+8615711397604'
            ),
            beauty_title='test two BT',
            title='test two title',
            other_titles='tests other titles two',
            connect='test connect two',
            status='new',
            coords_id=Coord.objects.create(
                latitude=23.983,
                longitude=97.789,
                height=224
            ),
            level_diff=Level.objects.create(
                winter="2B",
                summer="1A",
                autumn="2B",
                spring="1A",
            )
        )
        self.image_2 = Images.objects.create(
            data='',
            title='test-title-two',
            pereval_id=self.pereval_2
        )

    def test_list(self):
        response = self.client.get(reverse('perevaladd-list'))
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2], many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Pereval.objects.count(), 2)
        self.assertEqual(serializer_data, response.data)
        pereval_object_1 = Pereval.objects.filter(beauty_title='test BT').first()
        self.assertEqual(pereval_object_1.beauty_title, 'test BT')
        pereval_object_2 = Pereval.objects.filter(beauty_title='test two BT').first()
        self.assertEqual(pereval_object_2.beauty_title, 'test two BT')

    def test_detail(self):
        response = self.client.get(reverse('perevaladd-detail', kwargs={'pk': self.pereval_1.pk}))
        serializer_data = PerevalSerializer(self.pereval_1).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_two(self):
        response = self.client.get(reverse('perevaladd-detail', kwargs={'pk': self.pereval_2.pk}))
        serializer_data = PerevalSerializer(self.pereval_2).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
