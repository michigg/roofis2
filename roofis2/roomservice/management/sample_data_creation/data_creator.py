from roomservice.models import RoomType, Room, NumEquipment, Building, Location, Equipment, Booking, BookingGroup, \
    Staff, AccessPoint
from django.contrib.auth.models import User
import logging
import random
import datetime

logger = logging.getLogger(__name__)

LOCATIONS = ['Bamberg', 'Erlangen', 'Crailsheim', 'Hamburg', 'Chemnitz', 'Dresden', 'Sebnitz', 'Gunzenhausen',
             'Nürnberg']
BUILDINGS = ['253', '274', '134', '256', '142', '432', '652', '333', '233', '444', '332']
ROOMTYPE = ['Office', 'Conference Room', 'Teaching Room']
BOOKING_GROUP = ['Boss', 'SectionA', 'SectionB', 'SectionC', 'Standard']
EQUIPMENT = ['Beamer', 'Flipchart']


def create():
    logger.info('Location Count: {}'.format(Location.objects.count()))
    create_locations(LOCATIONS)
    logger.info('Location Count: {}'.format(Location.objects.count()))

    logger.info('Building Count: {}'.format(Building.objects.count()))
    create_buildings(BUILDINGS)
    logger.info('Building Count: {}'.format(Building.objects.count()))

    logger.info('RoomType Count: {}'.format(RoomType.objects.count()))
    create_room_type(ROOMTYPE)
    logger.info('RoomType Count: {}'.format(RoomType.objects.count()))

    logger.info('BookingGroup Count: {}'.format(BookingGroup.objects.count()))
    create_booking_group(BOOKING_GROUP)
    logger.info('BookingGroup Count: {}'.format(BookingGroup.objects.count()))

    logger.info('Equipment Count: {}'.format(Equipment.objects.count()))
    create_equipment(EQUIPMENT)
    logger.info('Equipment Count: {}'.format(Equipment.objects.count()))

    logger.info('Staff Count: {}'.format(Staff.objects.count()))
    create_staff()
    logger.info('Staff Count: {}'.format(Staff.objects.count()))

    logger.info('Room Count: {}'.format(Room.objects.count()))
    create_room()
    logger.info('Room Count: {}'.format(Room.objects.count()))

    logger.info('Booking Count: {}'.format(Booking.objects.count()))
    create_booking()
    logger.info('Booking Count: {}'.format(Booking.objects.count()))

    logger.info('NumEquipment Count: {}'.format(NumEquipment.objects.count()))
    create_num_equipment()
    logger.info('NumEquipment Count: {}'.format(NumEquipment.objects.count()))

    logger.info('AccessPoint Count: {}'.format(AccessPoint.objects.count()))
    create_access_point()
    logger.info('AccessPoint Count: {}'.format(AccessPoint.objects.count()))


def create_locations(names):
    for name in names:
        location, _ = Location.objects.get_or_create(name=name)


def create_buildings(names):
    for name in names:
        building, _ = Building.objects.get_or_create(name=name, location=random.choice(Location.objects.all()))


def create_room_type(types):
    for type in types:
        building, _ = RoomType.objects.get_or_create(type=type)


def create_booking_group(names):
    for name in names:
        booking_group, _ = BookingGroup.objects.get_or_create(name=name)


def create_equipment(names):
    for name in names:
        equipment, _ = Equipment.objects.get_or_create(name=name)


def create_staff():
    for i in range(1, 30):
        user, _ = User.objects.get_or_create(username='MannFrau{}'.format(i), email='mann{}@frau.de'.format(i),
                                             password='1234abcdef#')
        staff, _ = Staff.objects.get_or_create(user=random.choice(User.objects.all()))
        staff.booking_group.add(random.choice(BookingGroup.objects.all()))
        # booking_group = random.choice(BookingGroup.objects.all())
        staff.save()


def create_room():
    for i in range(1, 40):
        room, _ = Room.objects.get_or_create(building=random.choice(Building.objects.all()),
                                             room_number=random.randint(100, 956),
                                             capacity=random.randint(10, 400), seating=random.randint(0, 1),
                                             barrier_free=random.randint(0, 1), cooling=random.randint(0, 1),
                                             room_type=random.choice(RoomType.objects.all()),
                                             floor=random.randint(1, 6),
                                             admin=random.choice(BookingGroup.objects.all()),
                                             service_staff=random.choice(Staff.objects.all()))


def create_booking():
    for i in range(1, 80):
        year = random.choice(range(2018, 2019))
        month = random.choice(range(1, 12))
        day = random.choice(range(1, 28))
        random_start_date = datetime.datetime(year, month, day)

        delta = random.choice(range(0, 2))
        random_enddate_date = random_start_date + datetime.timedelta(delta)

        hour = random.choice(range(6, 22))
        minute = random.choice(range(1, 59))
        start_time = datetime.datetime(year, month, day, hour=hour, minute=minute)

        delta = random.choice(range(0, 3))
        end_time_time = start_time + datetime.timedelta(hours=delta)

        booking, _ = Booking.objects.get_or_create(room=random.choice(Room.objects.all()),
                                                   staff=random.choice(Staff.objects.all()),
                                                   start_date=random_start_date, end_date=random_enddate_date,
                                                   start_time=start_time, end_time=end_time_time,
                                                   intervall=random.choice(range(0, 3)))


def create_num_equipment():
    for i in range(1, 80):
        num_equipment = NumEquipment.objects.get_or_create(room=random.choice(Room.objects.all()),
                                                           equipment=random.choice(Equipment.objects.all()),
                                                           count=random.choice(range(1, 3)))


def create_access_point():
    for i in range(1, 25):
        access_point, _ = AccessPoint.objects.get_or_create(mac_address=''.join(
            random.choices(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'], k=12)), )
        for i in range(1, random.randint(1, 4)):
            access_point.rooms.add(random.choice(Room.objects.all()))
        access_point.save()
