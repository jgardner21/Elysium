# Generated by Django 5.0.3 on 2024-04-03 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_remove_playlist_profile_playlist_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='playlist_thumbnail_location',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]