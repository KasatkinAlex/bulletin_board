from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from notice.models import Ads
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email='test12@mail.ru')
        self.ads= Ads.objects.create(title='test1', author=self.user, price=1)
        self.client.force_authenticate(user=self.user)

    def test_ads_retrieve(self):
        url = reverse("ads:ads_detail", args=(self.ads.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('title'), self.ads.title
        )

    def test_ads_create(self):
        url = reverse("ads:ads_create")
        data = {
            'title': "test2",
            'price': 2
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Ads.objects.all().count(), 2
        )

    def test_ads_update(self):
        url = reverse("ads:ads_update", args=(self.ads.pk,))
        data = {
            'title': "test99"
        }
        response = self.client.patch(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('title'), "test99"
        )

    def test_ads_delete(self):
        url = reverse("ads:ads_delete", args=(self.ads.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Ads.objects.all().count(), 0
        )

    def test_ads_list(self):
        url = reverse("ads:ads_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Ads.objects.all().count(), 1)
