# Generated by Django 3.2.6 on 2021-08-14 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineclass', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helper',
            name='helper_audio',
            field=models.FilePathField(),
        ),
        migrations.AlterField(
            model_name='helper',
            name='helper_csv',
            field=models.FilePathField(),
        ),
        migrations.AlterField(
            model_name='helper',
            name='helper_txt',
            field=models.FilePathField(),
        ),
        migrations.AlterField(
            model_name='imagecapture',
            name='img_file',
            field=models.FilePathField(),
        ),
    ]