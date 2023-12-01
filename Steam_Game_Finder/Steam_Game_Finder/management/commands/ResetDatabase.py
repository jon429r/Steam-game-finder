from django.core.management.base import BaseCommand, CommandError
from django.db import connection

class Command(BaseCommand):
    help = 'Resets the database and applies migrations'

    def handle(self, *args, **options):
        try:
            # Delete the migrations directory
            self.stdout.write(self.style.SUCCESS('Deleting migrations directory'))
            import shutil
            shutil.rmtree('frontend/migrations', ignore_errors=True)

            # Drop and create the database
            self.stdout.write(self.style.SUCCESS('Dropping and creating the database'))
            with connection.cursor() as cursor:
                cursor.execute('DROP DATABASE IF EXISTS databasefinder')
                cursor.execute('CREATE DATABASE databasefinder')

            # Apply migrations
            self.stdout.write(self.style.SUCCESS('Applying migrations...'))
            from django.core.management import call_command
            call_command('makemigrations', 'frontend')
            call_command('migrate')

            self.stdout.write(self.style.SUCCESS('Successfully reset the database'))

        except FileNotFoundError:
            self.stderr.write(self.style.ERROR('Migrations directory not found'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Failed to reset the database. Error: {str(e)}'))
