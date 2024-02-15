# Generated by Django 4.2.7 on 2024-01-06 22:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='video_uploaded_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
