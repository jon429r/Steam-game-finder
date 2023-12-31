from django.core.management.base import BaseCommand
from Backend.search_procedures.search_procedure_initialization import LoadSearchProcedures

class Command(BaseCommand):
    help = 'Initialize stored procedures'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Initializing stored procedures...'))

        # Class for initializing procedures and interacting with the DB
        search_functions = LoadSearchProcedures()

        # Initialize all procedures
        search_functions.create_game_title_search_procedure()
        search_functions.create_language_search_procedure()
        search_functions.create_developer_search_procedure()
        search_functions.create_publisher_search_procedure()
        search_functions.create_reception_search_procedure()
        search_functions.create_age_rating_search_procedure()
        search_functions.create_developers_by_reception_search_procedure()
        search_functions.create_delete_trigger()

        self.stdout.write(self.style.SUCCESS('Stored procedures initialized successfully.'))