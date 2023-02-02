from django.db import models

# Create your models here.


class Places(models.Model):
    id = models.AutoField(primary_key=True)

    slug = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    address = models.CharField(max_length=150)
    location = models.CharField(max_length=100)
    gallery = models.JSONField()

    create_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    def __str__(self):
        return self.name


class Categories(models.Model):
    id = models.AutoField(primary_key=True)

    slug = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    address = models.CharField(max_length=150)
    location = models.CharField(max_length=100)
    gallery = models.JSONField()

    create_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    def __str__(self):
        return self.name


class Countries(models.Model):
    id = models.AutoField(primary_key=True)

    slug = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    create_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    def __str__(self):
        return self.name


class Cities(models.Model):
    id = models.AutoField(primary_key=True)

    slug = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    country_id = models.ForeignKey(
        "Countries", on_delete=models.CASCADE)
    parent_id = models.ForeignKey(
        "Categories", on_delete=models.CASCADE)

    create_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    def __str__(self):
        return self.name
