# Generated by Django 3.2.23 on 2024-02-05 13:12

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]
