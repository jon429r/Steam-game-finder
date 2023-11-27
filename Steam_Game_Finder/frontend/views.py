from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Game
from .models import Game, Liked_Disliked

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

liked_disliked_records = []

def fill_liked_disliked(request):
    global liked_disliked_records

    # Your logic to fetch data from the database and fill liked_disliked_records
    liked_disliked_records = Liked_Disliked.objects.values('app_id', 'title', 'header_image', 'action').all()

    print(liked_disliked_records)


# Function to populate resulting_games with data from Liked_Disliked table
def populate_resulting_games():
    global resulting_games  # Declare that you're using the global variable

    # Check if there are any records in the Liked_Disliked table
def populate_resulting_games():
    # Your logic to fetch data from the database and populate resulting_games
    resulting_games = Game.objects.values('app_id', 'name', 'header_image', 'price')[:7]

    return [
        {
            'ID': game['app_id'],
            'IMG': game['header_image'],
            'Title': game['name'],
            'Price': game['price'],
        }
        for game in resulting_games
    ]
# Call the function to populate resulting_games

# Now you can use the resulting_games variable globally in your application
print(liked_disliked_records)


def home_page_view(request):
    template_name = 'Home_Page/Home_Page.html'

    # Access liked_disliked_records globally
    global liked_disliked_records

    # Fill liked_disliked_records when home_page_view is called
    fill_liked_disliked(request)

    # Access liked_disliked_records and resulting_games
    return render(request, template_name, {'liked_disliked_records': liked_disliked_records, 'popular_games': popular_games, 'section1': 'Resulting Games', 'section2': 'Popular Games'})

def quiz_page_view(request):
    return render(request, 'Quiz_Page/Quiz_Page.html', {'popular_games': popular_games, 'section1': 'Popular Games'})

def search_page_view(request):
    return render(request, 'Search_Page/Search_Page.html', {'popular_games': popular_games, 'section1': 'Popular Games'})

def base_temp_view(request):
    return render(request, 'Base_Temp/Base.html', {'popular_games': popular_games, 'section1': 'Popular Games'})

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
