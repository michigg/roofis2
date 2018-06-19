from django.core.management.base import BaseCommand
from roomservice.utils import migrate_data_rooms


class Command(BaseCommand):
    help = "Import room data from univis prg api"

    def handle(self, *args, **options):
        migrate_data_rooms.main()
