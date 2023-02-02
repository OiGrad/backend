from django.contrib import admin
from places.models import City, PlaceCategory, Place, PlaceGallery, PlaceReview

admin.site.register(City)
admin.site.register(PlaceCategory)
admin.site.register(Place)
admin.site.register(PlaceGallery)
admin.site.register(PlaceReview)
