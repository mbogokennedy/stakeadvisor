# Generated by Django 2.1 on 2018-10-18 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20181001_1240'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='besttips',
            options={'ordering': ['-home_Odd'], 'verbose_name_plural': 'Best Tips'},
        ),
    ]
