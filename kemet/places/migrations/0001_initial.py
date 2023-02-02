# Generated by Django 4.1.3 on 2023-02-02 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.JSONField()),
                ('bio', models.TextField()),
                ('location_text', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='cities')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.JSONField()),
                ('bio', models.TextField()),
                ('location_text', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PlaceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.ImageField(upload_to='icons')),
            ],
        ),
        migrations.CreateModel(
            name='PlaceReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('rating', models.IntegerField()),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.place')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlaceGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='places')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.place')),
            ],
        ),
        migrations.AddField(
            model_name='place',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.placecategory'),
        ),
    ]
