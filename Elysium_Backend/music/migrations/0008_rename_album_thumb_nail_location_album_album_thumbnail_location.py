# Generated by Django 5.0.1 on 2024-04-16 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_rename_thumb_nail_album_album_thumb_nail_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='album_thumb_nail_location',
            new_name='album_thumbnail_location',
        ),
    ]
