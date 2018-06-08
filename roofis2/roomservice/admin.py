from django.contrib import admin
from .models import Staff, Room, RoomType, BookingGroup, Booking, Equipment, Location, Buildings, NumEquipment

# Register your models here.
admin.site.register(Staff)
admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(BookingGroup)
admin.site.register(Booking)
admin.site.register(Equipment)
admin.site.register(Location)
admin.site.register(Buildings)
admin.site.register(NumEquipment)
