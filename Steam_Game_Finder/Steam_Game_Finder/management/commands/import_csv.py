import csv
from django.core.management.base import BaseCommand
from Home_Page.models import Language, Developer, Publisher, Game

class Command(BaseCommand):
    help = 'Import data from a CSV file into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file to import')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Create and populate instances of your models
                Language.objects.create(
                    name=row['Language'],
                    # Add other fields as needed
                )
                Developer.objects.create(
                    name=row['Developer'],
                    # Add other fields as needed
                )
                Publisher.objects.create(
                    name=row['Publisher'],
                    # Add other fields as needed
                )
                Game.objects.create(
                    title=row['Game Title'],
                    developer=Developer.objects.get(name=row['Developer']),
                    publisher=Publisher.objects.get(name=row['Publisher']),
                    language=Language.objects.get(name=row['Language']),
                    # Add other fields as needed
                )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
