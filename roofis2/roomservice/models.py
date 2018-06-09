from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return '{}'.format(self.name)


class Building(models.Model):
    name = models.CharField(max_length=16)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)


class RoomType(models.Model):
    type = models.CharField(max_length=32)

    def __str__(self):
        return '{}'.format(self.type)


class BookingGroup(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return '{}'.format(self.name)


class Staff(models.Model):
    booking_group = models.ManyToManyField(BookingGroup)
    # username = personal_id
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.user.username)


class Room(models.Model):
    building = models.ForeignKey('Building', on_delete=models.CASCADE)
    room_number = models.CharField(max_length=16)
    capacity = models.IntegerField()
    seating = models.BooleanField()
    barrier_free = models.BooleanField()
    cooling = models.BooleanField()
    room_type = models.ForeignKey(RoomType, on_delete=models.PROTECT)
    floor = models.SmallIntegerField()
    admin = models.ForeignKey(BookingGroup, on_delete=models.SET_DEFAULT, default=1)
    service_staff = models.ForeignKey(Staff, on_delete=models.PROTECT)

    def __str__(self):
        return '{} - {}'.format(self.building.name, self.room_number)


class Equipment(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return '{}'.format(self.name)


class NumEquipment(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    count = models.SmallIntegerField()

    def __str__(self):
        return '{} - {} - {}'.format(self.room.room_number, self.equipment.name, self.count)


class Booking(models.Model):
    DAY = 0
    WEEK = 1
    EVERY_TWO_WEEKS = 2
    MONTH = 3

    TYPE_CHOICES = ((DAY, 'DAY'), (WEEK, 'WEEK'), (EVERY_TWO_WEEKS, 'EVERY_TWO_WEEKS'), (MONTH, 'MONTH'))
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    intervall = models.IntegerField(choices=TYPE_CHOICES)

    def __str__(self):
        return '{} - {} - {}'.format(self.room.room_number, self.start_date.strftime('%Y - %m - %d'),
                                     self.end_date.strftime('%Y - %m - %d'))


class AccessPoint(models.Model):
    mac_address = models.CharField(max_length=12)
    rooms = models.ManyToManyField(Room)

    def __str__(self):
        return '{}'.format(self.mac_address)


class Favorite(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.staff.user.username, self.room.room_number)
