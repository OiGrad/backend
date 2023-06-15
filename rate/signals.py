from django.db.models.signals import post_save
from django.dispatch import receiver
from rate.models import RatePlace
from places.models import Place
from django.db.models import Sum


@receiver(post_save, sender=RatePlace)
def clac_rate_place(sender, instance, created, **kwargs):
    if created:
        rated_place = RatePlace.objects.filter(place=instance.place)
        total_rate = rated_place.aggregate(total_rate=Sum("rate"))["total_rate"]
        o = Place.objects.get(pk=instance.place.pk)
        o.rate = total_rate / rated_place.count()
        o.save()
    else:
        rated_place = RatePlace.objects.filter(place=instance.place)
        total_rate = rated_place.aggregate(total_rate=Sum("rate"))["total_rate"]
        o = Place.objects.get(pk=instance.place.pk)
        o.rate = total_rate / rated_place.count()
        o.save()
