from django.shortcuts import render

# import the class to initialiae the search procedures
from search_procedure_initialization import LoadSearchProcedures


def search_view(request: str):
    # determine which search to preform
    procedure_name = request.GET.get("procedure_name", "")
    search_parameter = request.GET.get("parameters", "")
    # create search procedure initialization object
    search_functions = LoadSearchProcedures()

    if procedure_name == "game_title_search":
        results = search_functions.game_title_search(search_parameter)
    elif procedure_name == "language_search":
        results = search_functions.language_search(search_parameter)
    elif procedure_name == "games_by_developer_search":
        results = search_functions.games_by_developer_search(search_parameter)
    elif procedure_name == "games_by_publisher_search":
        results = search_functions.games_by_publisher_search(search_parameter)
    elif procedure_name == "reception_search":
        results = search_functions.reception_search(search_parameter)
    elif procedure_name == "age_rating_search":
        results = search_functions.age_rating_search(search_parameter)
    elif procedure_name == "devolopers_by_reception_search":
        results = search_functions.devolopers_by_reception_search(search_parameter)
    elif procedure_name == "genre_search":
        results = search_functions.genre_search(search_parameter)
    elif procedure_name == "tag_search":
        results = search_functions.tag_search(search_parameter)
    elif procedure_name == "category_search":
        results = search_functions.category_search(search_parameter)
    else:
        results = "Invalid procedure name."



    return render(results, "results.html")
