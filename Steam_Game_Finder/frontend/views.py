from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Game
from .models import Game, Liked_Disliked


def home_page_view(request):

    resulting_games = [
        {'ID': 1, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 1', 'Price': 39.99},
        {'ID': 2, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 2', 'Price': 49.99},
        {'ID': 3, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 3', 'Price': 29.99},
        {'ID': 4, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 4', 'Price': 19.99},
        {'ID': 5, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 5', 'Price': 39.99},
        {'ID': 6, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 6', 'Price': 49.99},
        {'ID': 7, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 7', 'Price': 29.99},
    ]    

    popular_games = [
        {'ID': 1, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 1', 'Price': 39.99},
        {'ID': 2, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 2', 'Price': 49.99},
        {'ID': 3, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 3', 'Price': 29.99},
        {'ID': 4, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 4', 'Price': 19.99},
        {'ID': 5, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 5', 'Price': 39.99},
        {'ID': 6, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 6', 'Price': 49.99},
        {'ID': 7, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 7', 'Price': 29.99},
        {'ID': 8, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 8', 'Price': 19.99},
        {'ID': 9, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 9', 'Price': 39.99},
        {'ID': 10, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 10', 'Price': 49.99},
        {'ID': 11, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 11', 'Price': 29.99},
    ]

    return render(request, 'Home_Page/Home_Page.html', {'resulting_games': resulting_games, 'popular_games': popular_games, 'section1': 'Resulting Games', 'section2': 'Popular Games'})


def quiz_page_view(request):
    popular_games = [
        {'ID': 3, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 1', 'Price': 39.99},
        {'ID': 4, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 2', 'Price': 49.99},
        # Add more popular game data as needed
    ]
    return render(request, 'Quiz_Page/Quiz_Page.html', {'popular_games': popular_games, 'section1': 'Popular Games'})

def search_page_view(request):
    popular_games = [
        {'ID': 3, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 1', 'Price': 39.99},
        {'ID': 4, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 2', 'Price': 49.99},
        # Add more popular game data as needed
    ]
    return render(request, 'Search_Page/Search_Page.html', {'popular_games': popular_games, 'section1': 'Popular Games'})

def base_temp_view(request):
    popular_games = [
        {'ID': 3, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 1', 'Price': 39.99},
        {'ID': 4, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 2', 'Price': 49.99},
        # Add more popular game data as needed
    ]
    return render(request, 'Base_Temp/Base.html', {'popular_games': popular_games, 'section1': 'Popular Games'})

def error_page_view(request):
    return render(request, 'Extras/Error_Page.html')

def liked_game_view(request):
    return render(request, 'Extras/Liked_Games.html')

"""def liked_disliked_popup_view(request):
    # Access the value from the URL parameter 'request'
    disliked_value = request.GET.get('request', '')

    # You can now use the 'disliked_value' in your view logic
    # For example, you might pass it to the template
    context = {'disliked_value': disliked_value}
    return render(request, 'LikedDisliked_popup.html', context)"""

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
