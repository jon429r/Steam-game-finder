from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Game, Resulting_Games
from .models import Game, Liked_Disliked, Resulting_Games, Popular_Games
from .forms import SearchForm
from django.db import connection
import Backend.search_procedures.search_procedure_calls as CallProcedures

resulting_games_records = []    

popular_games_records = []

liked_disliked_records = []

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def results(request):
    print("entering results function")
    search_form = SearchForm(request.GET)
    games = {}

    if search_form.is_valid() and request.method == "GET":
        search_term = search_form.cleaned_data.get('search_term')
        field_choice = search_form.cleaned_data.get('field_choice')
        print(f"Search Term: {search_term}, Field Choice: {field_choice}")

        if search_term and field_choice:
            allowed_choices = ['Name Search', 'Genre Search', 'Developer Search', 'Publisher Search', 'Tag Search','Developer_by_Reception Search', 'Recommendation Search', 'Language Search', 'Age Rating Search', 'Category Search']
            if field_choice in allowed_choices:
                games = CallProcedures.call_procedure(field_choice, search_term)
    print(games)
    return render(request, 'Search_Page/Search_Page.html', {'games': games, 'form': search_form})


def fill_popular_games(request):      
    global popular_games_records

    popular_games_records = Popular_Games.objects.values('app_id', 'title', 'header_image', 'action').all()

    print(popular_games_records)

def fill_resulting_games(request):
    global resulting_games_records

    resulting_games_records = Resulting_Games.objects.values('app_id', 'title', 'header_image', 'action').all()


def fill_liked_disliked(request):
    global liked_disliked_records

    # Your logic to fetch data from the database and fill liked_disliked_records
    liked_disliked_records = Liked_Disliked.objects.values('app_id', 'title', 'header_image', 'action').all()

def info_page_view(request):
    global popular_games_records
    
    return render(request, 'Info_Page/Info_Page.html', {'popular_games': popular_games_records, 'section1': 'Popular Games'})

def home_page_view(request):
    template_name = 'Home_Page/Home_Page.html'

    # Access liked_disliked_records globally
    global liked_disliked_records

    # Fill liked_disliked_records when home_page_view is called
    fill_resulting_games(request)
    fill_popular_games(request)

    # Access liked_disliked_records and resulting_games
    return render(request, template_name, {'resulting_games': resulting_games_records, 'popular_games': popular_games_records, 'section1': 'Resulting Games', 'section2': 'Popular Games'})

def quiz_page_view(request):
    return render(request, 'Quiz_Page/Quiz_Page.html', {'popular_games': popular_games_records, 'section1': 'Popular Games'})

def search_page_view(request):
    return render(request, 'Search_Page/Search_Page.html', {'popular_games': popular_games_records, 'section1': 'Popular Games'})

def base_temp_view(request):
    return render(request, 'Base_Temp/Base.html', {'popular_games': popular_games_records, 'section1': 'Popular Games'})

def error_page_view(request):
    return render(request, 'Extras/Error_Page.html')


def liked_disliked_popup_view(request):
    ## Access the value from the URL parameter 'request'
    disliked_value = request.GET.get('request', '')

    ## For example, you might pass it to the template
    context = {'disliked_value': disliked_value}
    return render(request, 'LikedDisliked_popup.html', context)

from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Game

def game_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    likes = game.liked_disliked_set.filter(action='like').count()
    dislikes = game.liked_disliked_set.filter(action='dislike').count()
    return render(request, 'game_detail.html', {'game': game, 'likes': likes, 'dislikes': dislikes})

def like_game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    liked_disliked, created = Liked_Disliked.objects.get_or_create(title=game.title, action='like')
    game.liked_disliked = liked_disliked
    print(game.liked_disliked)
    game.save()
    return JsonResponse({'likes': game.liked_disliked_set.count()})

def dislike_game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    liked_disliked, created = Liked_Disliked.objects.get_or_create(title=game.title, action='dislike')
    game.liked_disliked = liked_disliked
    print(game.liked_disliked)
    game.save()
    return JsonResponse({'dislikes': game.liked_disliked_set.count()})

def liked_game_view(request):
    if request.method == 'POST':
        game_title = request.POST.get('game_title')
        # Rest of your logic...
        return render(request, 'Extras/Liked_Games.html', {'game_title': game_title})
    else:
        # Handle GET requests or other cases...
        return render(request, 'Extras/Liked_Games.html')
