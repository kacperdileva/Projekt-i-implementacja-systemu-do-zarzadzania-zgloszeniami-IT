from django.db import models
from django.contrib.auth.models import User

ROLE_CHOICES = [
    ('user', 'Użytkownik końcowy'),
    ('tech', 'Pracownik IT'),
    ('admin', 'Administrator'),
    ('manager', 'Kierownik'),
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"