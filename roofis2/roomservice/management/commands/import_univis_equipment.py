from django.core.management.base import BaseCommand
from roomservice.utils import migrate_data_rooms
from roomservice.models import Equipment

import logging

logger = logging.getLogger(__name__)

UNIVIS_IDS_MAP = [{'id': 'LOSE', 'name': 'Lose Bestuhlung'},
                  {'id': 'FEST', 'name': 'Feste Bestuhlung'},
                  {'id': 'ANST', 'name': 'Sitzreihen ansteigend'},
                  {'id': 'DARK', 'name': 'Verdunklung'},
                  {'id': 'VISU', 'name': 'DocCam'},
                  {'id': 'DBEAM', 'name': 'Doppelprojektion'},
                  {'id': 'PC', 'name': 'Interner PC'},
                  {'id': 'MIKR', 'name': 'Pultmikrofon'},
                  {'id': 'FUNK', 'name': 'Funkmikrofon'},
                  {'id': 'INDUK', 'name': 'Induktive Höranlage'},
                  {'id': 'DVD', 'name': 'DVD-Player'},
                  {'id': 'BLURAY', 'name': 'BluRay-Player'},
                  {'id': 'PRUEF', 'name': 'Prüfungsraum'},
                  {'id': 'OHEAD', 'name': 'Overheadprojektor'}]


class Command(BaseCommand):
    help = "Import room data from univis prg api"

    def handle(self, *args, **options):
        logger.info("Start:\nEquipment: {}".format(Equipment.objects.count()))
        for elem in UNIVIS_IDS_MAP:
            equip, _ = Equipment.objects.update_or_create(univis_id=elem['id'], name=elem['name'])
        logger.info("Start:\nEquipment: {}".format(Equipment.objects.count()))
