from django.core.management.base import BaseCommand
from roomservice.utils import migrate_data_rooms
from roomservice.models import LectureType

import logging

logger = logging.getLogger(__name__)

UNIVIS_IDS_MAP = [{'id': 'V', 'name': 'Vorlesung'},

                  {'id': 'Vorlesung', 'name': 'Vorlesung'},
                  {'id': 'Vorlesung/Seminar', 'name': 'Vorlesung/Seminar'},

                  {'id': 'Seminar', 'name': 'Seminar'},
                  {'id': 'Hauptseminar', 'name': 'Hauptseminar'},
                  {'id': 'Oberseminar', 'name': 'Oberseminar'},
                  {'id': 'Blockseminar', 'name': 'Blockseminar'},
                  {'id': 'Seminar/Oberseminar', 'name': 'Seminar/Oberseminar'},
                  {'id': 'Seminaristischer Unterricht', 'name': 'Seminaristischer Unterricht'},
                  {'id': 'Vertiefungsseminar', 'name': 'Vertiefungsseminar'},
                  {'id': 'Proseminar', 'name': 'Proseminar'},
                  {'id': 'Seminar/Hauptseminar', 'name': 'Seminar/Hauptseminar'},
                  {'id': 'Forschungsseminar', 'name': 'Forschungsseminar'},

                  {'id': 'Ü', 'name': 'Übung'},
                  {'id': 'Übung', 'name': 'Übung'},
                  {'id': 'Übung/Blockseminar', 'name': 'Übung/Blockseminar'},
                  {'id': 'Übung/Tutorium', 'name': 'Übung/Tutorium'},

                  {'id': 'Praktikum', 'name': 'Praktikum'},
                  {'id': 'Forschungspraktikum', 'name': 'Forschungspraktikum'},
                  {'id': 'Sonstige Lehrveranstaltung', 'name': 'Sonstige Lehrveranstaltung'},
                  {'id': 'Tutorien', 'name': 'Tutorien'},

                  {'id': 'Kolloquium', 'name': 'Kolloquium'},
                  {'id': 'Repetitorium', 'name': 'Repetitorium'},

                  {'id': 'Vorlesung und Übung', 'name': 'Vorlesung und Übung'},
                  {'id': 'Seminar/Proseminar', 'name': 'Seminar/Proseminar'},
                  {'id': 'Seminar/Übung', 'name': 'Seminar/Übung'},
                  {'id': 'feldarchäologisches Praktikum', 'name': 'feldarchäologisches Praktikum'},
                  {'id': 'Exkursion', 'name': 'Exkursion'},
                  # {'id': 'Klausurenkurs', 'name': 'Klausurenkurs'},
                  # {'id': 'Klausurenkurs', 'name': 'Klausurenkurs'},
                  ]


class Command(BaseCommand):
    help = "Import room data from univis prg api"

    def handle(self, *args, **options):
        logger.info("Start:\nLecture Types: {}".format(LectureType.objects.count()))
        for elem in UNIVIS_IDS_MAP:
            equip, _ = LectureType.objects.update_or_create(univis_id=elem['id'], name=elem['name'])
        logger.info("Start:\nLecture Types: {}".format(LectureType.objects.count()))
