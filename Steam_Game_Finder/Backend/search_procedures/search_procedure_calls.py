from django.shortcuts import render

# import the class to initialiae the search procedures
from Backend.search_procedures.search_procedure_initialization import LoadSearchProcedures


def call_procedure(procedure_name, parameters):
    # create search procedure initialization object
    search_functions = LoadSearchProcedures()

    if procedure_name == "Name Search":
        results = search_functions.game_title_search(parameters)
    elif procedure_name == "Language Search":
        results = search_functions.language_search(parameters)
    elif procedure_name == "Developer Search":
        results = search_functions.games_by_developer_search(parameters)
    elif procedure_name == "Publisher Search":
        results = search_functions.games_by_publisher_search(parameters)
    elif procedure_name == "Reception Search":
        results = search_functions.reception_search(parameters)
    elif procedure_name == "Age Rating Search":
        results = search_functions.age_rating_search(parameters)
    elif procedure_name == "Developers by Reception Search":
        results = search_functions.developers_by_reception_search()
    elif procedure_name == "Genre Search":
        results = search_functions.genre_search(parameters)
    elif procedure_name == "Tag Search":
        results = search_functions.tag_search(parameters)
    elif procedure_name == "Category Search":
        results = search_functions.category_search(parameters)
    elif procedure_name == "Delete Game":
        search_functions.delete_game(parameters)
        return
    elif procedure_name == "Recommendation Search":
        results = search_functions.recommendation_search(parameters)
    else:
        results = "Invalid procedure name."

    return results
