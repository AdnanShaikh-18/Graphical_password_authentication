# Generated by Django 4.1.4 on 2023-03-10 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniproject', '0017_profile_bio_profile_gender_profile_social_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='social_url',
        ),
    ]
