from django.core.management.base import BaseCommand
from roomservice.utils import migrate_data_rooms
from roomservice.models import LectureSpecifiaction

import logging

logger = logging.getLogger(__name__)

UNIVIS_IDS_MAP = [{'id': 'OBLIG', 'name': 'obligatorische Lehrveranstaltung'},
                  {'id': 'GENERALE', 'name': 'Studium Generale'},
                  {'id': 'ENGLISH', 'name': 'Englischsprachig'},
                  {'id': 'ETCS', 'name': 'ECTS-Studium'},
                  {'id': 'WOMSPE', 'name': 'Frauenspezifisch/Geschlechtervergl'},
                  {'id': 'ANPFLICHT', 'name': 'Anwesenheitspflicht'},
                  {'id': 'MODULSTUD', 'name': 'Modulstudium'},
                  {'id': 'FRUEH', 'name': 'Frühstudium'},
                  {'id': 'ZENIS', 'name': 'Zentrum für Interreligiöse Studien'},
                  {'id': 'BENSCHEIN', 'name': 'benoteter Schein'},
                  {'id': 'ERWEI', 'name': 'Erweiterungsbereich'},
                  {'id': 'ZENMAS', 'name': ' Zentrum für Mittelalterstudien'},
                  ]


class Command(BaseCommand):
    help = "Import room data from univis prg api"

    def handle(self, *args, **options):
        logger.info("Start:\nLecture Specs: {}".format(LectureSpecifiaction.objects.count()))
        for elem in UNIVIS_IDS_MAP:
            equip, _ = LectureSpecifiaction.objects.update_or_create(univis_id=elem['id'], name=elem['name'])
        logger.info("Start:\nLecture Specs: {}".format(LectureSpecifiaction.objects.count()))
