# Generated by Django 4.1.4 on 2023-03-07 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniproject', '0010_alter_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(blank=True, default='error 404 bio not found', max_length=100, null=True),
        ),
    ]
