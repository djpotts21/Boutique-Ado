# Generated by Django 3.2.23 on 2024-01-25 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20240116_1915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='hassize',
            new_name='has_sizes',
        ),
    ]