from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Game, Resulting_Games
from .models import Game, Liked_Disliked, Resulting_Games, Popular_Games
from .forms import SearchForm, LikeDislikeForm
from django.db import connection
import Backend.search_procedures.search_procedure_calls as CallProcedures


liked_disliked_games = []
liked_games = []
disliked_games = []
popular_games_records = []
liked_disliked_records = []
search_games_result = {}

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def results(request):
    global search_games_result, liked_games
    current_path = request.get_full_path
    current_path = str(current_path)
    print("entering results function")
    search_form = SearchForm(request.GET)
    Liked_Disliked_Form = Liked_Disliked(request.GET)

    search_games_result = {}

    if search_form.is_valid() and request.method == "GET":
        search_term = search_form.cleaned_data.get('search_term')
        field_choice = search_form.cleaned_data.get('field_choice')
        print(f"Search Term: {search_term}, Field Choice: {field_choice}")

        if search_term and field_choice:
            allowed_choices = ['Name Search', 'Genre Search', 'Developer Search',
                               'Reception Search', 'Publisher Search', 'Tag Search',
                               'Developer by Reception Search', 'Recommendation Search',
                               'Language Search', 'Age Rating Search', 'Category Search']
            if field_choice in allowed_choices:
                search_games_result = CallProcedures.call_procedure(field_choice, search_term)
    print(search_games_result)
    return render(request, 'Search_Page/Search_Page.html', {'games': search_games_result, 'form': SearchForm, 'LikeDislikeForm': Liked_Disliked_Form, 'liked_games': liked_games, 'section1': 'Liked Games'})

def info_page_view(request):
    global popular_games_records
    
    return render(request, 'Info_Page/Info_Page.html', {'Liked_Disliked_Form': LikeDislikeForm, 'liked_games': liked_games, 'section1': 'Liked Games'})

def home_page_view(request):
    template_name = 'Home_Page/Home_Page.html'


    # Access liked_disliked_records and resulting_games
    return render(request, template_name, {'Liked_Disliked_Form': LikeDislikeForm, 'liked_games': liked_games, 'section1': 'Liked Games'})

def quiz_page_view(request):
    return render(request, 'Quiz_Page/Quiz_Page.html', {'Liked_Disliked_Form': LikeDislikeForm, 'liked_games': liked_games, 'section1': 'Liked Games'})

def search_page_view(request):
    return render(request, 'Search_Page/Search_Page.html', {'Liked_Disliked_Form': LikeDislikeForm, 'liked_games': liked_games, 'section1': 'Liked Games'})

def base_temp_view(request):
    return render(request, 'Base_Temp/Base.html', {'Liked_Disliked_Form': LikeDislikeForm, 'liked_games': liked_games, 'section1': 'Liked Games'})

def error_page_view(request):
    return render(request, 'Extras/Error_Page.html')

    



# views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from .forms import LikeDislikeForm
from .models import Game
from django.http import JsonResponse

from django.shortcuts import get_object_or_404


import logging

logger = logging.getLogger(__name__)

cur = connection.cursor()

def like_view(request):
    global liked_games, search_games_result
    if request.method == 'POST':
        form = LikeDislikeForm(request.POST)


        if form.is_valid():
            game_id = form.cleaned_data['game_id']
            action = form.cleaned_data['action']
            print(f"game_id: {game_id}, action: {action}")

            cur.execute("SELECT AppID, Name, Price, Header_image FROM Game WHERE AppID = %s", [game_id])
            game = cur.fetchone()

            if game:
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

            try:
                print("Liked Games: ")
                for liked_game in liked_games:
                    print(f"app_id: {liked_game[0]}, name: {liked_game[1]}, price: {liked_game[2]}, Header_Image: {liked_game[3]}")
            except:
                print("liked_games is empty")

            return render(request, 'Search_Page/Search_Page.html', {'games': search_games_result, 'form': SearchForm, 'Liked_Disliked_Form': LikeDislikeForm, 'liked_games': liked_games, 'section1': 'Liked Games'})

        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


def dislike_view(request):
    global disliked_games, search_games_result

    if request.method == 'POST':
        form = LikeDislikeForm(request.POST)
        if form.is_valid():
            game_id = form.cleaned_data['game_id']
            action = form.cleaned_data['action']

            cur.execute("SELECT AppID, Name, Price, Header_image FROM Game WHERE AppID = %s", [game_id])    
            game = cur.fetchone()

            if game:
                if game not in disliked_games:
                    disliked_games.append(game)
                    print('Adding game to disliked_games')

                    print('disliked_games:')
                    for disliked_game in disliked_games:
                        print(f"game_id: {disliked_game[0]}, name: {disliked_game[1]}, price: {disliked_game[2]}, Header_Image: {disliked_game[3]}")
                    # here
                else:
                    disliked_games.remove(game)
                    print('Removing game from disliked_games')
                    # here


            return render(request, 'Search_Page/Search_Page.html', {'games': search_games_result, 'form': SearchForm, 'Liked_Disliked_Form': LikeDislikeForm, 'liked_games': liked_games, 'section1': 'Liked Games'})
        else: 
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})