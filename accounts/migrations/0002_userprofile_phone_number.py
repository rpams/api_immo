# Generated by Django 2.2.12 on 2020-06-26 13:55

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default=22968004523, max_length=128, region=None),
            preserve_default=False,
        ),
    ]