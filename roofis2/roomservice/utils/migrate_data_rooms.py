import json
from pprint import pprint
from django.db.utils import IntegrityError

from roomservice.models import Room, Building, RoomType, OrgUnit, Equipment
from .parser import univis_rooms_parser
from .parser import univis_lectures_parser
import ast

import logging

logger = logging.getLogger(__name__)

# CONFIG Fakultaet
FAKULTAET_GuK = "Fakult%E4t%20Geistes-%20und%20Kulturwissenschaften"
FAKULTAET_SoWi = "Fakult%E4t%20Sozial-%20und%20Wirtschaftswissenschaften"
FAKULTAET_HuWi = "Fakult%E4t%20Humanwissenschaften"
FAKULTAET_WIAI = "Fakult%E4t%20Wirtschaftsinformatik"

# CONFIG Locations
RZ = "http://univis.uni-bamberg.de/prg?search=rooms&name=rz&show=xml"
WEBEREI = "http://univis.uni-bamberg.de/prg?search=rooms&name=we&show=xml"
FEKI = "http://univis.uni-bamberg.de/prg?search=rooms&name=f&show=xml"
MARKUSHAUS = "http://univis.uni-bamberg.de/prg?search=rooms&name=m&show=xml"
UNIVERSITAET = "http://univis.uni-bamberg.de/prg?search=rooms&name=u&show=xml"
KAPUZINERSTR = "http://univis.uni-bamberg.de/prg?search=rooms&name=k&show=xml"
ZWINGER = "http://univis.uni-bamberg.de/prg?search=rooms&name=z&show=xml"
AULA = "http://univis.uni-bamberg.de/prg?search=rooms&name=a&show=xml"


# CONFIG ROOMS
def univis_rooms(fakultaet):
    return "http://univis.uni-bamberg.de/prg?search=rooms&department=" + fakultaet + "&show=xml"


# CONFIG LECTURES
def univis_lectures(fakultaet):
    return "http://univis.uni-bamberg.de/prg?search=lectures&department=" + fakultaet + "&show=exml"


def univis_rooms_loc(kuerzel):
    return "http://univis.uni-bamberg.de/prg?search=rooms&name=" + kuerzel + "&show=xml"


def getJsonFromFile(path):
    with open(path, "r") as file:
        return json.load(file)


def writeUnivisRoomDataInDB(rooms):
    for room in rooms:
        try:
            building = None
            if 'address' in room and 'buildingkey' in room:
                building_address = room['address']
                building_key = room['buildingkey']
                building, _ = Building.objects.get_or_create(key=building_key, address=building_address)

            short = str(room['short']).split(sep='/')[-1]
            univis_id = room['id']
            univis_key = room['@key']

            capacity = None
            if 'size' in room:
                capacity = room['size']

            floor = None
            if 'floor' in room:
                floor = room['floor']

            room_type = None
            if 'name' in room:
                room_type, _ = RoomType.objects.get_or_create(type=room['name'])

            description = None
            if 'description' in room:
                description = room['description']

            orgname = None
            if 'orgname' in room:
                orgname, _ = OrgUnit.objects.get_or_create(title=room['orgname'])

            room_db_obj, _ = Room.objects.update_or_create(building=building,
                                                           room_number=short,
                                                           capacity=capacity,
                                                           floor=floor,
                                                           univis_id=univis_id,
                                                           univis_key=univis_key,
                                                           room_type=room_type,
                                                           description=description,
                                                           orgname=orgname)

            equipment_options = Equipment.objects.all()
            for equipment in equipment_options:
                univis_id = equipment.univis_id.lower()
                if univis_id in room and room[univis_id] == 'ja':
                    room_db_obj.equipment.add(equipment)

            orgunits = None
            if 'orgunits' in room:
                for orgunit in room['orgunits']:
                    if len(orgunit) > 0:
                        for orgunit in str(room['orgunits']['orgunit']).strip("[]").split(','):
                            cleaned_orgunit = orgunit.strip().strip("'").strip("'")
                            orgunit, _ = OrgUnit.objects.get_or_create(title=cleaned_orgunit)
                            room_db_obj.orgunits.add(orgunit)

                        # TODO: Check xml syntax #orgunit problem
                        pass
                    else:
                        orgunit, _ = OrgUnit.objects.get_or_create(title=orgunit)
                        room_db_obj.orgunits.add(orgunit)

            # room_db_obj.save()
            logger.info('ROOM: {}'.format(room_db_obj.room_number))


        except IntegrityError as err:
            logger.warning(err)
            logger.warning('Room already exists')


def delete():
    rooms = Room.objects.all()
    logger.info("Deleted following Rooms:")
    for room in rooms:
        logger.info("Room: {name}".format(
            name=room.short)
        )
        room.delete()


def main():
    # get food jsons
    logger.info("\nStart:\nRoom: {}\nOrgunits: {}\nBuildings: {}\nRoomTypes: {}"
                .format(Room.objects.count(),
                        OrgUnit.objects.count(),
                        Building.objects.count(),
                        RoomType.objects.count()))

    writeUnivisRoomDataInDB(univis_rooms_parser.parsePage(univis_rooms(FAKULTAET_GuK)))
    writeUnivisRoomDataInDB(univis_rooms_parser.parsePage(univis_rooms(FAKULTAET_SoWi)))
    writeUnivisRoomDataInDB(univis_rooms_parser.parsePage(univis_rooms(FAKULTAET_HuWi)))
    writeUnivisRoomDataInDB(univis_rooms_parser.parsePage(univis_rooms(FAKULTAET_WIAI)))
    writeUnivisRoomDataInDB(univis_rooms_parser.parsePage(univis_rooms_loc("k")))
    writeUnivisRoomDataInDB(univis_rooms_parser.parsePage(univis_rooms_loc("z")))
    writeUnivisRoomDataInDB(univis_rooms_parser.parsePage(univis_rooms_loc("u")))
    writeUnivisRoomDataInDB(univis_rooms_parser.parsePage(univis_rooms_loc("w")))
    writeUnivisRoomDataInDB(univis_rooms_parser.parsePage(univis_rooms_loc("f")))
    writeUnivisRoomDataInDB(univis_rooms_parser.parsePage(univis_rooms_loc("r")))
    writeUnivisRoomDataInDB(univis_rooms_parser.parsePage(univis_rooms_loc("h")))
    writeUnivisRoomDataInDB(univis_rooms_parser.parsePage(univis_rooms_loc("l")))
    writeUnivisRoomDataInDB(univis_rooms_parser.parsePage(univis_rooms_loc("m")))
    writeUnivisRoomDataInDB(univis_rooms_parser.parsePage(univis_rooms_loc("o")))
    writeUnivisRoomDataInDB(univis_rooms_parser.parsePage(univis_rooms_loc("p")))
    writeUnivisRoomDataInDB(univis_rooms_parser.parsePage(univis_rooms_loc("v")))
    writeUnivisRoomDataInDB(univis_rooms_parser.parsePage(univis_rooms_loc("w")))
    writeUnivisRoomDataInDB(univis_rooms_parser.parsePage(univis_rooms_loc("d")))
    writeUnivisRoomDataInDB(univis_rooms_parser.parsePage(univis_rooms_loc("x")))

    logger.info("\nFinished:\nRoom: {}\nOrgunits: {}\nBuildings: {}\nRoomTypes: {}"
                .format(Room.objects.count(),
                        OrgUnit.objects.count(),
                        Building.objects.count(),
                        RoomType.objects.count()))


if __name__ == '__main__':
    main()
