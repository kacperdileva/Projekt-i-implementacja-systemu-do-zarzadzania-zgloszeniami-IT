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

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('new', 'Nowe'),
        ('in_progress', 'W trakcie'),
        ('resolved', 'Rozwiązane'),
        ('closed', 'Zamknięte'),
    ]
    PRIORITY_CHOICES = [
        ('low', 'Niska'),
        ('medium', 'Średnia'),
        ('high', 'Wysoka'),
        ('critical', 'Krytyczna'),
    ]

    title = models.CharField(max_length=200, verbose_name='Tytuł')
    description = models.TextField(verbose_name='Opis')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new',
        verbose_name='Status'
    )
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='medium',
        verbose_name='Priorytet'
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='created_tickets',
        verbose_name='Utworzył'
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_tickets',
        verbose_name='Przypisany do'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Utworzono')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Zaktualizowano')

    def __str__(self):
        return self.title