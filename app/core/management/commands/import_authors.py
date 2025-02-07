import csv
import argparse

from django.core.management.base import BaseCommand
from core.models import Author


class Command(BaseCommand):
    """
    Custom Django command to import the
    full name of the authors into the database
    via a CSV file
    """

    help = 'import CSV data'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='?', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        with open(options['csv_file']) as csv_file:
            dict_reader = csv.DictReader(csv_file)
            for row in dict_reader:
                Author.objects.create(
                    name=f"{row['First Name']} {row['Last Name']}"
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        'Created author {} {}'.format(
                            row['First Name'],
                            row['Last Name']
                        )
                    )
                )
