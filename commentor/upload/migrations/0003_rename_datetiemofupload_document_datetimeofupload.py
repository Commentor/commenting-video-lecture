# Generated by Django 3.2.6 on 2021-08-13 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_auto_20210813_2229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='dateTiemOfUpload',
            new_name='dateTimeOfUpload',
        ),
    ]
