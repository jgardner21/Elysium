# Generated by Django 5.0.1 on 2024-02-13 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id_user',
        ),
    ]
