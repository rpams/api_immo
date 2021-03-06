# Generated by Django 2.2.12 on 2020-06-28 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryImmobilier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('sous_category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ImageAnnonceImmobilier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='media/immobilier/%Y-%m-%d/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='media/immobilier/%Y-%m-%d/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='media/immobilier/%Y-%m-%d/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='media/immobilier/%Y-%m-%d/')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='media/immobilier/%Y-%m-%d/')),
            ],
        ),
        migrations.CreateModel(
            name='PriceNature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_nature', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceImmobilier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title', max_length=1024)),
                ('description', models.TextField(help_text='Describe it')),
                ('price', models.IntegerField(help_text='price fcfa')),
                ('coordinate', models.CharField(help_text='Coord getting with GMap', max_length=255)),
                ('document', models.FileField(help_text='relatice document url', upload_to='')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('cateroy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.CategoryImmobilier')),
                ('image', models.ManyToManyField(to='api.ImageAnnonceImmobilier')),
                ('price_nature', models.ForeignKey(help_text='Price nature', on_delete=django.db.models.deletion.CASCADE, to='api.PriceNature')),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Ownner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContracteurImmobilier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annonce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='serviceImmoContract', to='api.ServiceImmobilier')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserContracteur', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnnonceurImmobilier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annonce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ServiceImmoAnnounce', to='api.ServiceImmobilier')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserAnnonceur', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
