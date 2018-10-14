from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Building(models.Model):
    key = models.CharField(max_length=8, unique=True)
    address = models.CharField(max_length=32)

    def __str__(self):
        return '{}'.format(self.key)


class RoomType(models.Model):
    type = models.CharField(max_length=32)

    def __str__(self):
        return '{}'.format(self.type)


#
#
# class BookingGroup(models.Model):
#     name = models.CharField(max_length=64)
#
#     def __str__(self):
#         return '{}'.format(self.name)
#
#
class Staff(models.Model):
    # booking_group = models.ManyToManyField(BookingGroup)
    # username = ba - Nummer
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)


class OrgUnit(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return '{}'.format(self.title)


class Equipment(models.Model):
    univis_id = models.CharField(max_length=8)
    name = models.CharField(max_length=32)

    def __str__(self):
        return '{}'.format(self.univis_id)


class Room(models.Model):
    building = models.ForeignKey('Building', on_delete=models.CASCADE, null=True, blank=True)
    room_number = models.CharField(max_length=16)
    capacity = models.IntegerField(null=True, blank=True)
    floor = models.SmallIntegerField(null=True, blank=True)
    univis_id = models.IntegerField(unique=True)
    univis_key = models.CharField(unique=True, max_length=64)
    room_type = models.ForeignKey(RoomType, on_delete=models.PROTECT, null=True, blank=True)
    # TODO: extract equipment
    description = models.CharField(max_length=64, null=True, blank=True)
    equipment = models.ManyToManyField(Equipment)

    orgname = models.ForeignKey(OrgUnit, on_delete=models.PROTECT, related_name='room_orgname', null=True, blank=True)
    orgunits = models.ManyToManyField(OrgUnit)

    # seating = models.BooleanField()
    # barrier_free = models.BooleanField()
    # cooling = models.BooleanField()

    # admin = models.ForeignKey(BookingGroup, on_delete=models.SET_DEFAULT, default=1)
    # service_staff = models.ForeignKey(Staff, on_delete=models.PROTECT)

    def __str__(self):
        if self.building == None:
            return '{}/{}'.format(None, self.room_number)
        else:
            return '{}/{} - {}'.format(self.building.key, self.room_number, self.orgname)


#
# class NumEquipment(models.Model):
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
#     count = models.SmallIntegerField()
#
#     def __str__(self):
#         return '{} - {} - {}'.format(self.room.room_number, self.equipment.name, self.count)
#
# class Exclude_Term(models.Model):
#     date = models.DateField()

class LectureSpecifiaction(models.Model):
    univis_id = models.CharField(max_length=8)
    name = models.CharField(max_length=32)

    def __str__(self):
        return '{}'.format(self.univis_id)


class LectureType(models.Model):
    #univis_id = models.CharField(max_length=8)
    name = models.CharField(max_length=32)

    def __str__(self):
        return '{}'.format(self.name)


class Lecture(models.Model):
    univis_id = models.IntegerField(unique=True)
    univis_key = models.CharField(unique=True, max_length=64)
    type = models.ForeignKey(LectureType, on_delete=models.PROTECT, null=True, blank=True)
    title = models.CharField(max_length=64)
    short = models.CharField(max_length=16, null=True, blank=True)
    ects = models.FloatField(null=True, blank=True)
    sws = models.FloatField(null=True, blank=True)
    estimated_visitor = models.PositiveIntegerField(null=True, blank=True)
    specification = models.ManyToManyField(LectureSpecifiaction)
    orgname = models.ForeignKey(OrgUnit, on_delete=models.PROTECT, related_name='lecture_orgname', null=True,
                                blank=True)
    orgunits = models.ManyToManyField(OrgUnit)
    url_description = models.URLField(null=True, blank=True)

    organizational = models.TextField(max_length=64, null=True, blank=True)
    time_description = models.TextField(max_length=64, null=True, blank=True)
    summary = models.TextField(max_length=64, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.title)


class LectureTerm(models.Model):
    # room = models.ForeignKey(Room, on_delete=models.CASCADE)
    room = models.CharField(max_length=64, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    exclude = models.CharField(max_length=128, null=True, blank=True)
    repeat = models.CharField(max_length=16, null=True, blank=True)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.lecture.title)

# class Booking(models.Model):
#     DAY = 0
#     WEEK = 1
#     EVERY_TWO_WEEKS = 2
#     MONTH = 3
#
#     TYPE_CHOICES = ((DAY, 'DAY'), (WEEK, 'WEEK'), (EVERY_TWO_WEEKS, 'EVERY_TWO_WEEKS'), (MONTH, 'MONTH'))
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     intervall = models.IntegerField(choices=TYPE_CHOICES)
#
#     def __str__(self):
#         return '{} - {} - {}'.format(self.room.room_number, self.start_date.strftime('%Y - %m - %d'),
#                                      self.end_date.strftime('%Y - %m - %d'))
#
#
# class AccessPoint(models.Model):
#     mac_address = models.CharField(max_length=12)
#     rooms = models.ManyToManyField(Room)
#
#     def __str__(self):
#         return '{}'.format(self.mac_address)
#
#
# class Favorite(models.Model):
#     staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return '{} - {}'.format(self.staff.user.username, self.room.room_number)
