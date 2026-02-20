from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


class RegisterTests(TestCase):
    def test_register_page_loads(self):
        response = self.client.get('/rejestracja/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Rejestracja')

    def test_register_creates_user_and_profile(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'TrudneHaslo123!',
            'password2': 'TrudneHaslo123!',
        }
        response = self.client.post('/rejestracja/', data)
        self.assertEqual(response.status_code, 302)

        user = User.objects.get(username='testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.profile.role, 'user')

    def test_register_passwords_must_match(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'TrudneHaslo123!',
            'password2': 'InneHaslo456!',
        }
        response = self.client.post('/rejestracja/', data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='testuser').exists())