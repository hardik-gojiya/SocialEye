# Generated by Django 5.1.5 on 2025-02-04 13:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_content_post_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='reel',
            name='description',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='reel',
            name='reel',
            field=models.FileField(upload_to='static/reels/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])]),
        ),
    ]
