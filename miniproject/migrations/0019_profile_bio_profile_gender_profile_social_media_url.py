# Generated by Django 4.1.4 on 2023-03-10 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniproject', '0018_remove_profile_bio_remove_profile_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(default='male', max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_media_url',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
