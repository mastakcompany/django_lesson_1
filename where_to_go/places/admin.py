from django.contrib import admin
from places.models import Place, Coordinate, Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass


@admin.register(Coordinate)
class CoordinateAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
