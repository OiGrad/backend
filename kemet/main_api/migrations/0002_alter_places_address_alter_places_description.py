# Generated by Django 4.1.3 on 2023-01-31 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='address',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='places',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]
