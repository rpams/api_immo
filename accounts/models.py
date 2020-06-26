from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    phone_number = PhoneNumberField()
    description = models.TextField(blank=True,null=True)
    location = models.CharField(max_length=30,blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_creator = models.BooleanField(default=False)
    image = models.ImageField(upload_to='users/', null=True, blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('user', args=[str(self.user.username)])
