# Generated by Django 5.0.3 on 2024-03-27 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='profile_images/default.png', upload_to='profile_images'),
        ),
    ]
