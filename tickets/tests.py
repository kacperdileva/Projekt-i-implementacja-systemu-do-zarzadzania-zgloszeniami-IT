from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Ticket


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

class LoginTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='jan',
            password='TrudneHaslo123!'
        )
        Profile.objects.create(user=self.user, role='user')

    def test_login_page_loads(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Logowanie')

    def test_login_with_correct_credentials(self):
        response = self.client.post('/login/', {
            'username': 'jan',
            'password': 'TrudneHaslo123!',
        })
        self.assertEqual(response.status_code, 302)

    def test_login_with_wrong_password(self):
        response = self.client.post('/login/', {
            'username': 'jan',
            'password': 'ZleHaslo',
        })
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        self.client.login(username='jan', password='TrudneHaslo123!')
        response = self.client.post('/logout/')
        self.assertEqual(response.status_code, 302)


class TicketTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='jan', password='TrudneHaslo123!'
        )
        Profile.objects.create(user=self.user, role='user')
        self.tech = User.objects.create_user(
            username='technik', password='TrudneHaslo123!'
        )
        Profile.objects.create(user=self.tech, role='tech')
    def test_ticket_list_requires_login(self):
        """Niezalogowany użytkownik przekierowany na login."""
        response = self.client.get('/zgloszenia/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)
    def test_create_ticket(self):
        """Zalogowany użytkownik może utworzyć zgłoszenie."""
        self.client.login(username='jan', password='TrudneHaslo123!')
        response = self.client.post('/zgloszenia/nowe/', {
            'title': 'Nie dziala drukarka',
            'description': 'Drukarka na 2 pietrze nie drukuje.',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Ticket.objects.filter(title='Nie dziala drukarka').exists())
        ticket = Ticket.objects.get(title='Nie dziala drukarka')
        self.assertEqual(ticket.created_by, self.user)
    def test_ticket_has_default_status_and_priority(self):
        """Nowe zgłoszenie ma domyślny status i priorytet."""
        self.client.login(username='jan', password='TrudneHaslo123!')
        self.client.post('/zgloszenia/nowe/', {
            'title': 'Problem z VPN',
            'description': 'Nie moge sie polaczyc z VPN.',
        })
        ticket = Ticket.objects.get(title='Problem z VPN')
        self.assertEqual(ticket.status, 'new')
        self.assertEqual(ticket.priority, 'medium')
    def test_user_sees_only_own_tickets(self):
        """Użytkownik widzi tylko własne zgłoszenia."""
        Ticket.objects.create(
            title='Zgloszenie Jana', description='Opis', created_by=self.user
        )
        Ticket.objects.create(
            title='Zgloszenie technika', description='Opis', created_by=self.tech
        )
        self.client.login(username='jan', password='TrudneHaslo123!')
        response = self.client.get('/zgloszenia/')
        self.assertContains(response, 'Zgloszenie Jana')
        self.assertNotContains(response, 'Zgloszenie technika')
    def test_tech_sees_all_tickets(self):
        """Pracownik IT widzi wszystkie zgłoszenia."""
        Ticket.objects.create(
            title='Zgloszenie Jana', description='Opis', created_by=self.user
        )
        self.client.login(username='technik', password='TrudneHaslo123!')
        response = self.client.get('/zgloszenia/')
        self.assertContains(response, 'Zgloszenie Jana')
    def test_ticket_detail_page_works(self):
        """Strona szczegółów zgłoszenia zwraca 200 i zawiera treść."""
        ticket = Ticket.objects.create(
            title='Test', description='Opis testowy', created_by=self.user
        )
        self.client.login(username='jan', password='TrudneHaslo123!')
        response = self.client.get(f'/zgloszenia/{ticket.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test')
        self.assertContains(response, 'Opis testowy')