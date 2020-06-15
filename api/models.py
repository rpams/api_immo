from django.db import models
from django.contrib.auth.models import User
# from api_immo import settings

class OwnedModel(models.Model):
    owner = models.ForeignKey(User,
    on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Belonging(OwnedModel):
    name = models.CharField(max_length=100)


class Category(models.Model):
    category = models.CharField(max_length=255, help_text="Enter category type")
    sous_category = models.CharField(max_length=255, help_text="Enter subcategory type")
    def __str__(self):
        return self.category
    def get_absolute_url(self):
        # Returns the url to access a particular instance of Product.
        return reverse('category-detail-view', args=[str(self.id)])


class Sujet(models.Model):
    context = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, help_text="Name of the context")
    description = models.TextField()
    ville = models.CharField(max_length=255, help_text="Town for context")
    coordonnees = models.CharField(max_length=255, help_text="Coord getting with GMap")
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        # Returns the url to access a particular instance of Product.
        return reverse('context-detail-view', args=[str(self.id)])


class User(models.Model):
    login_id = models.CharField(max_length=300, help_text="Login id")
    username = models.CharField(max_length=255, help_text="Username")
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    # sujet = models.ManyToManyField(Sujet)
    sujet = models.ForeignKey(Sujet, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Owns", null=True)
    def __str__(self):
        return self.username
    def get_absolute_url(self):
        # Returns the url to access a particular instance of Product.
        return reverse('user-detail-view', args=[str(self.id)])