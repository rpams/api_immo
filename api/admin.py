from django.contrib import admin
from .models import ServiceImmobilier, CategoryImmobilier, PriceNature

admin.site.register(ServiceImmobilier)
admin.site.register(CategoryImmobilier)
admin.site.register(PriceNature)
