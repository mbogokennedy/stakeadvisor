# Generated by Django 2.1 on 2018-11-29 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id_No',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='opt_phone_number',
        ),
    ]
