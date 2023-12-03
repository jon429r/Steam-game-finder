from django.shortcuts import render
from django.db import connection
# import the class to initialiae the search procedures
from search_procedure_initialization import LoadSearchProcedures

config_file = "connectorConfig.json"
class CallSearchProcedures:
    @staticmethod
    def access_db(query, params=None, as_dictionary=False):
        """
        Connect to the database with Django db cursor to execute queries.
        :param query: query to be performed
        :param params: parameters for the query (optional)
        :param as_dictionary: whether results should be in dictionary form for ease of printing
        :return: results in dictionary or SQL table form depending on as_dictionary
        """
        with connection.cursor() as cursor:
            # Determine if tuple or dictionary format
            if as_dictionary:
                cursor.execute(query, params)
            else:
                cursor.execute(query, params)
            results = cursor.fetchall()
            cursor.close()

        return results
    
    @staticmethod
    def search_view(request):
        # determine which search to preform 
        procedure_name = request.GET.get('procedure_name', '')

        search_parameter = request.GET.get('parameters', '')

        if procedure_name == 'game_title_search':
            query = """
                CALL game_title_search(%s);
            """
            params = [search_parameter]
            CallSearchProcedures.acess_db(query, params=params)

        elif procedure_name == 'language_search':
            query = """
                CALL language_search(%s);
            """
            # Set appropriate params
            params = [search_parameter]
            CallSearchProcedures.acess_db(query, params=params)

        elif procedure_name == 'games_by_developer_search':
            query = """
            CALL games_by_developer_search(%s);
            """
            # Set appropriate params
            params = [search_parameter]
            CallSearchProcedures.acess_db(query, params=params)

        elif procedure_name == 'games_by_publisher_search':
            query = """
                CALL games_by_publisher_search(%s);
            """
            # Set appropriate params
            params = [search_parameter]
            CallSearchProcedures.acess_db(query, params=params)

        elif procedure_name == 'reception_search':
            query = """
                CALL reception_search(%s);
            """
            # Set appropriate params
            params = [search_parameter]
            CallSearchProcedures.acess_db(query, params=params)

        elif procedure_name == 'age_rating_search':
            query = """
                CALL age_rating_search(%s);
            """
            # Set appropriate params
            params = [search_parameter]
            CallSearchProcedures.acess_db(query, params=params)

        elif procedure_name == 'devolopers_by_reception_search':
            query = """
            CALL devolopers_by_reception_search();
            """
            CallSearchProcedures.acess_db(query)

        else:
            results = "Invalid procedure name."


        return render(results, 'results.html')
