# Generated by Django 3.2.6 on 2021-09-21 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='enable',
            new_name='enabled',
        ),
    ]
