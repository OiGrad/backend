# Generated by Django 4.0 on 2023-06-17 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_place_gallery'),
        ('rate', '0003_alter_rateplace_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rateplace',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='places.place'),
        ),
    ]