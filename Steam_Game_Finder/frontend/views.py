from django.shortcuts import render
from django.http import JsonResponse
from .models import Liked_Disliked
from .forms import SearchForm, LikeDislikeForm
from django.db import connection
import Backend.search_procedures.search_procedure_calls as CallProcedures
from django.contrib.sessions.models import Session
import logging
import numpy as np
import random

logger = logging.getLogger(__name__)

cur = connection.cursor()

liked_disliked_games = []
# For use with the recommendation algorithm
# holds disliked and liked game
liked_games = []
disliked_games = []
search_games_result = {}

def dictfetchall(cursor):
    """For having results from DB returned as a dictionary
   
    Args:
        cursor (Django): Django cursor
    Returns:
        Dictionary: Results from query returned as dictionary
    """
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def prepare_recommendation():
    """gather tags, genres, and categories randomly from the liked games list to preform a search based on those


    Args:
        liked_games (List): all the games a user has liked

    Returns:
        String: Returns a string of cat/genre/tag seperated by space
    """
    liked_games_copy = liked_games
    
    if len(liked_games) < 1:
        return
    
    # Shuffle array for random tags/cat/genre chosen
    np.random.shuffle(liked_games_copy)
    i = len(liked_games_copy)-1
    
    cur.execute("SELECT genre FROM GameGenre WHERE AppID = %s", [liked_games_copy[i][0]])
    genre = cur.fetchone()
    
    if i-1 != -1: i -= 1

    cur.execute("SELECT tag FROM GameTag WHERE AppID = %s", [liked_games_copy[i][0]])
    
    tag = cur.fetchone()

    if i-1 != -1: i-= 1

    cur.execute("SELECT category FROM GameCategory WHERE AppID = %s",[liked_games_copy[i][0]])

    category = cur.fetchone()

    result_string = f"{genre[0]} {tag[0]} {category[0]}"
    
    return result_string
    

def results(request):
    """Handles gathering user input data from front end then sends request to backend to have procedures done

    Args:
        request (Django): Request is Django data gathered from frontend

    Returns:
        Dictionary: Returns a dictionary of games to be send to Django html to be printed
    """
    global search_games_result, liked_games
    current_path = request.get_full_path
    current_path = str(current_path)

    search_form = SearchForm(request.GET)
    Liked_Disliked_Form = Liked_Disliked(request.GET)

    search_games_result = {}
    search_term_required = False

    if search_form.is_valid() and request.method == "GET":
        search_term = search_form.cleaned_data.get('search_term')
        field_choice = search_form.cleaned_data.get('field_choice')
        print(f"Search Term: {search_term}, Field Choice: {field_choice}")

        # Availble search options
        allowed_choices = ['Name Search', 'Genre Search', 'Developer Search',
                               'Reception Search', 'Publisher Search', 'Tag Search',
                               'Developers by Reception Search', 'Recommendation Search',
                               'Language Search', 'Age Rating Search', 'Category Search']
        
        if search_term and field_choice and field_choice != 'Developers by Reception Search' and field_choice != 'Recommendation Search':
            if field_choice in allowed_choices:
                search_games_result = CallProcedures.call_procedure(field_choice, search_term)
                search_term_required = True

        # Devolopers by Reception search no search_term
        elif field_choice == 'Developers by Reception Search': 
            if field_choice in allowed_choices:
                search_games_result = CallProcedures.call_procedure(field_choice, search_term)
                search_term_required = False

        elif field_choice == 'Recommendation Search':
            if field_choice in allowed_choices and len(liked_games) > 1:
                search_term = prepare_recommendation()
                search_games_result = CallProcedures.call_procedure(field_choice, search_term)
                search_term_required = False
        
        # Reduce results size to 100
        if search_games_result:
            search_games_result = search_games_result[:100]

        print(search_term_required) 
        return render(request, 'Search_Page/Search_Page.html', {
        'games': search_games_result,
        'form': SearchForm,
        'LikeDislikeForm': Liked_Disliked_Form,
        'liked_games': liked_games,
        'section1': 'Liked Games',
        'search_term_required': search_term_required,
    })

def info_page_view(request):
    """Handles rendering of the info page

    Args:
        request:

    Returns:
    the return statement renders the info_page/info.html and passes in the liked disliked form, liked games array and liked games as the section name
    """
    global popular_games_records
    
    return render(request, 'Info_Page/Info_Page.html', {'Liked_Disliked_Form': LikeDislikeForm, 'liked_games': liked_games, 'section1': 'Liked Games'})

def home_page_view(request):
    """handles rendering the home page

    Args:
        request:

    Returns:
    the return statement renders the homePage/Home_Page.html and passes in the liked disliked form, liked games array and liked games as the section name

    """
    template_name = 'Home_Page/Home_Page.html'


    # Access liked_disliked_records and resulting_games
    return render(request, template_name, {'Liked_Disliked_Form': LikeDislikeForm, 'liked_games': liked_games, 'section1': 'Liked Games'})

def quiz_page_view(request):
    """handles rendering the quiz page

    Args:
        request:

    Returns:
    the return statement renders the quiz_page/quiz_page.html and passes in the liked disliked form, liked games array and liked games as the section name

    """
    return render(request, 'Quiz_Page/Quiz_Page.html', {'Liked_Disliked_Form': LikeDislikeForm, 'liked_games': liked_games, 'section1': 'Liked Games'})

def search_page_view(request):
    """handles rendering the search page

    Args:
        request:

    Returns:
    the return statement renders the Search_Page/Search_Page.html and passes in the liked disliked form, liked games array and liked games as the section name

    """
    return render(request, 'Search_Page/Search_Page.html', {'Liked_Disliked_Form': LikeDislikeForm, 'liked_games': liked_games, 'section1': 'Liked Games'})

def base_temp_view(request):
    """handles rendering the base temp page

    Args:
        request:

    Returns:
    the return statement renders the Base_Temp/Base.html and passes in the liked disliked form, liked games array and liked games as the section name

    """
    return render(request, 'Base_Temp/Base.html', {'Liked_Disliked_Form': LikeDislikeForm, 'liked_games': liked_games, 'section1': 'Liked Games'})

def error_page_view(request):
    """Handles the rendering for an error page

    Args:
        request:

    Returns:
    the return statement renders the Base_Temp/Base.html file
    """
    return render(request, 'Extras/Error_Page.html')

def like_dislike_view(request):
    """Handle liking and disliking a game. Move game data to corresponding lists.

    Args:
        request (Django Html Data): Dynamic html info gathered

    Returns:
        View: Returns a django view to update the data in the table. 
    """
    global liked_games, search_games_result
    if request.method == 'POST':
        # getting the form
        form = LikeDislikeForm(request.POST)

        #checking if form is valid and starts to execute
        if form.is_valid():
            game_id = form.cleaned_data['game_id']
            action = form.cleaned_data['action']
            print(f"game_id: {game_id}, action: {action}")

            # sql command to get the game from the database by searching with the game id
            cur.execute("SELECT AppID, Name, Price, Header_image FROM Game WHERE AppID = %s", [game_id])
            game = cur.fetchone()

            # checks the action (like or dislike) then adds or removes from the coresponing array
            if game and action == "like":
                if game not in liked_games:
                    liked_games.append(game)
                    print('Adding game to liked_games')
                    response_data = {
                        'status': 'success',
                        'game': {

                            'Liked or Disliked': action,
                            'app_id': game[0],
                            'name': game[1],
                            'price': game[2],
                            'Header_image': game[3],
                        }
                    }
                    print(f'response_data: {response_data}')

                else:
                    liked_games.remove(game)
                    print('Removing game from liked_games')

            elif game and action == "dislike":
                 if game not in disliked_games:
                    disliked_games.append(game)
                    
                    # Remove the game from the DB 
                    CallProcedures.call_procedure("Delete Game", game_id)
                    delete_game_from_results(game[0], search_games_result)
                    
            # renders
            return render(request, 'Search_Page/Search_Page.html', {'games': search_games_result, 'form': SearchForm, 'Liked_Disliked_Form': LikeDislikeForm, 'liked_games': liked_games, 'section1': 'Liked Games'})

        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    
def delete_game_from_results(game_id, results):
    """Remove a game from the results table if disliked

    Args:
        game_id (game info): AppID of particular game to be deleted
        results (Dictionary): Update the results dictionary by removing specefied entry

    Returns:
        _type_: _description_
    """
    for game in results:
        if game['AppID'] == game_id:
            results.remove(game)
            return True
    # game not found - shoudn't happen
    return False