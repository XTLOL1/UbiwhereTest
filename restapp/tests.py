from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from restapp.models import SpeedTier

class PermissionTests(APITestCase):
    def test_anon_perms(self):
        url = "http://localhost:8000/restapp/roadSegments/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = {"longStart": 1234.1234, "latStart": 897.1245, "longEnd": 234.12334, "latEnd": 234.12354, "length": 1234}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_perms(self):
        url = "http://localhost:8000/restapp/roadSegments/"
        user = User.objects.create_superuser('admin', "admin@example.com", "something123!")
        self.assertTrue(self.client.login(username="admin", password="something123!"))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = {"longStart": 1234.1234, "latStart": 897.1245, "longEnd": 234.12334, "latEnd": 234.12354, "length": 1234}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class SpeedTiersTests(APITestCase):
    def test_safety_mechanisms(self):
        url = "http://localhost:8000/restapp/speedTiers/"
        user = User.objects.create_superuser('admin', "admin@example.com", "something123!")
        self.assertTrue(self.client.login(username="admin", password="something123!"))
        response = self.client.get(url)
        self.assertEqual(len(response.data), 0)
        lowerTier = SpeedTier(upperLimit=20, designation="elevada") # <= 20
        lowerTier.save()
        midTier = SpeedTier(lowerLimit=20, upperLimit=50, designation="média") # > 20 && <= 50
        midTier.save()
        higherTier = SpeedTier(lowerLimit=50, designation="baixa") # > 50
        higherTier.save()
        response = self.client.get(url)
        self.assertEqual(len(response.data), 3)
        for speedTier in response.data:
            if speedTier["lowerLimit"] is None:
                response = self.client.put(speedTier["url"], {"lowerLimit": -726, "designation": "griefing"}, format="json")
                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            elif speedTier["upperLimit"] is None:
                response = self.client.patch(speedTier["url"], {"designation": "something"}, format="json")
                self.assertEqual(response.status_code, status.HTTP_200_OK)
            else:
                response = self.client.put(speedTier["url"], {"upperLimit": 100}, format="json")
                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



