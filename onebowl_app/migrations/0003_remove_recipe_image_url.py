# Generated by Django 4.2.20 on 2025-04-30 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onebowl_app', '0002_recipe_image_url_recipe_instructions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='image_url',
        ),
    ]
