# Generated by Django 5.0.2 on 2025-03-23 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileHub', '0005_user_information'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_Information',
        ),
    ]
