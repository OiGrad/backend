from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)
    location = models.JSONField()
    bio = models.TextField()
    location_text = models.CharField(max_length=255)
    image = models.ImageField(upload_to='cities')

    def __str__(self):
        return self.name


class PlaceCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='icons')

    def __str__(self):
        return self.name


class Place(models.Model):
    category = models.ForeignKey(PlaceCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.JSONField()
    bio = models.TextField()
    location_text = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PlaceGallery(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='places')

    def __str__(self):
        return self.place.name


class PlaceReview(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.place.name
