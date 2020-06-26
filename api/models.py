from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models import Q

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

STATUS_CHOICES = {
    ('To_Read', 'To Read'),
    ('Reading', 'Reading'),
    ('Read', 'Read')
}

class User(AbstractUser):
    pass

class Book(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='books', null=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='')


class Note(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE, related_name='notes')
    time_stamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    note = models.TextField(max_length=1000)
    page_number = models.CharField(max_length=5, null=True, blank=True)


def get_available_books_for_user(queryset, user):
    if user.is_authenticated:
        books = queryset.filter(Q(user=user))
    else:
        books = None
    return books