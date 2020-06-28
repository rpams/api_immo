from django.db import models
from django.conf import settings
from django.utils import timezone
from jsonfield import JSONField



# ------------------------------------------------------ #
class CategoryImmobilier(models.Model):
    category = models.CharField(max_length=255)
    sous_category = models.CharField(max_length=255)
    def __str__(self):
        return self.category
    def get_absolute_url(self):
        return reverse('category-immobilier', args=[str(self.category)])

# ------------------------------------------------------ #
class ImageAnnonceImmobilier(models.Model):
    image1 = models.ImageField(upload_to='media/immobilier/%Y-%m-%d/', null=True, blank=True)
    image2 = models.ImageField(upload_to='media/immobilier/%Y-%m-%d/', null=True, blank=True)
    image3 = models.ImageField(upload_to='media/immobilier/%Y-%m-%d/', null=True, blank=True)
    image4 = models.ImageField(upload_to='media/immobilier/%Y-%m-%d/', null=True, blank=True)
    image5 = models.ImageField(upload_to='media/immobilier/%Y-%m-%d/', null=True, blank=True)


# ------------------------------------------------------ #
class PriceNature(models.Model):
    price_nature = models.CharField(max_length=120)
    def __str__(self):
        return self.price_nature
    def get_absolute_url(self):
        return reverse('price-nature', args=[str(self.price_nature)])

# ------------------------------------------------------ #
class ServiceImmobilier(models.Model):
    publisher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Ownner", null=True)
    title = models.CharField(max_length=1024, help_text="Title")
    image = models.ManyToManyField(ImageAnnonceImmobilier)
    cateroy = models.ForeignKey(CategoryImmobilier, on_delete=models.CASCADE)
    description = models.TextField(help_text="Describe it")
    price = models.IntegerField(help_text="price fcfa")
    price_nature = models.ForeignKey(PriceNature, on_delete=models.CASCADE, help_text="Price nature")
    coordinate = models.CharField(max_length=255, help_text="Coord getting with GMap")
    document = models.FileField(help_text="relatice document url")
    date_created = models.DateTimeField(default=timezone.now, editable=False)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('service-immobilier', args=[str(self.title)])


# ------------------------------------------------------ #
class AnnonceurImmobilier(models.Model):
    annonce = models.ForeignKey(ServiceImmobilier, on_delete=models.CASCADE, related_name="ServiceImmoAnnounce")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="UserAnnonceur")

    def __str__(self):
        return self.user.username + " : " + self.annonce.title


# ------------------------------------------------------ #
class ContracteurImmobilier(models.Model):
    annonce = models.ForeignKey(ServiceImmobilier, on_delete=models.CASCADE, related_name="serviceImmoContract")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="UserContracteur")

    def __str__(self):
        return self.user.username + " -> " + self.annonce.title

