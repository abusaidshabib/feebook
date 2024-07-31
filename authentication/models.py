from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CustomUser(BaseModel, AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True, blank=False, null=False)
    phone = models.CharField(max_length=15, null=True, blank=True)
    dateOfBirth = models.DateField(null=True, blank=True)
    address = models.TextField()
    friends = models.ManyToManyField("self", symmetrical=False, related_name="user_friends", blank=True)
    followers = models.ManyToManyField("self", symmetrical=False, related_name="user_followers", blank=True)
    friends_request = models.ManyToManyField("self", symmetrical=False, related_name="user_friend_requests", blank=True)

    is_active = models.BooleanField(default=True)
    is_seller = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return True