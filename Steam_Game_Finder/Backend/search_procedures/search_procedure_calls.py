from django.shortcuts import render

# import the class to initialiae the search procedures
from Backend.search_procedures.search_procedure_initialization import LoadSearchProcedures


def call_procedure(procedure_name, parameters):
    # create search procedure initialization object
    search_functions = LoadSearchProcedures()

    if procedure_name == "Game":
        results = search_functions.game_title_search(parameters)
    elif procedure_name == "language_search":
        results = search_functions.language_search(parameters)
    elif procedure_name == "Developer":
        results = search_functions.games_by_developer_search(parameters)
    elif procedure_name == "Publisher":
        results = search_functions.games_by_publisher_search(parameters)
    elif procedure_name == "reception_search":
        results = search_functions.reception_search(parameters)
    elif procedure_name == "age_rating_search":
        results = search_functions.age_rating_search(parameters)
    elif procedure_name == "Devoloper_By_Reception":
        results = search_functions.devolopers_by_reception_search(parameters)
    elif procedure_name == "Genre":
        results = search_functions.genre_search(parameters)
    elif procedure_name == "Tag":
        results = search_functions.tag_search(parameters)
    elif procedure_name == "category_search":
        results = search_functions.category_search(parameters)
    elif procedure_name == "Recommendation":
        results = search_functions.recomendation_search(parameters)
    else:
        results = "Invalid procedure name."

    return results
