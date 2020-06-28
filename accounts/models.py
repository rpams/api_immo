from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    image = models.ImageField(upload_to="profile/%Y/%m/")
    option = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.user.username

# class CustomUser(AbstractUser):

#     username = models.CharField(max_length=255, blank=True, unique=True)
#     email = models.EmailField(_('Email-adress'), unique=True)
#     option = models.CharField('Last-Name', max_length=255, blank=True, null=True)
#     image = models.ImageField(upload_to="profile/%Y/%m/")

#     groups = models
#     user_permissions = models

#     USERNAME_FIELD = 'username'

#     REQUIRED_FIELDS = ['password']

#     def __str__(self):
#         return f"{self.email} - {self.first_name} {self.last_name}"
