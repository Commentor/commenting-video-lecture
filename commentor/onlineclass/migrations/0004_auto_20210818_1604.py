# Generated by Django 3.2.6 on 2021-08-18 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineclass', '0003_auto_20210815_0201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='helper',
            name='helper_csv',
        ),
        migrations.RemoveField(
            model_name='helper',
            name='helper_txt',
        ),
        migrations.AlterField(
            model_name='helper',
            name='helper_audio',
            field=models.FileField(upload_to='%Y-%m-%d-%H-%M-%S\\mix\\'),
        ),
        migrations.DeleteModel(
            name='ImageCapture',
        ),
    ]
