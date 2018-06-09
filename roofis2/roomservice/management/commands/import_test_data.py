from django.core.management.base import BaseCommand
from roomservice.management.sample_data_creation import data_creator


class Command(BaseCommand):
    help = "Creates sample data and inserts it to db"

    def handle(self, *args, **options):
        data_creator.create()
