# Generated by Django 4.2.20 on 2025-05-01 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onebowl_app', '0009_alter_ingredient_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
    ]
