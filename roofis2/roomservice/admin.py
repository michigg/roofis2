from django.contrib import admin
from .models import Room, Building, RoomType, OrgUnit, Equipment, Staff, Lecture, LectureSpecifiaction, LectureType

# Register your models here.
admin.site.register(Lecture)
admin.site.register(LectureSpecifiaction)
admin.site.register(LectureType)
admin.site.register(Staff)
admin.site.register(Room)
admin.site.register(RoomType)
# admin.site.register(BookingGroup)
# admin.site.register(Booking)
admin.site.register(Equipment)
admin.site.register(Building)
# admin.site.register(NumEquipment)
# admin.site.register(AccessPoint)
# admin.site.register(Favorite)
admin.site.register(OrgUnit)
