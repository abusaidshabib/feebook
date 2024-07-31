from django.db import models
from django.contrib.auth.models import AbstractUser

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CustomUser(AbstractUser, BaseModel):
    phone = models.CharField(max_length=15, null=True, blank=True)
    dateOfBirth = models.DateField(null=True, blank=True)
    address = models.TextField()
    is_seller = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    friends = models.ManyToManyField("self", symmetrical=False, related_name="user_friends", blank=True)
    followers = models.ManyToManyField("self", symmetrical=False, related_name="user_followers", blank=True)
    friends_request = models.ManyToManyField("self", symmetrical=False, related_name="user_friend_requests", blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
