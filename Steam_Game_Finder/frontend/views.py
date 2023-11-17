from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return render(request, 'Home_Page/Home_Page.html')

def quiz_page_view(request):
    return render(request, 'Quiz_Page/Quiz_Page.html')

def search_page_view(request):
    return render(request, 'Search_Page/Search_Page.html', {})

def display_games(request):
    # Your Python list containing game data
    games = [
        {'ID': 1, 'Title': 'Game 1', 'Price': 19.99},
        {'ID': 2, 'Title': 'Game 2', 'Price': 29.99},
        # Add more game data as needed
    ]

    return render(request, 'Home_Page/Home_Page.html', {'games': games})

def display_popular_games(request):
    # Your Python list containing game data
    games = [
        {'ID': 1, 'Title': 'Game 1', 'Price': 19.99},
        {'ID': 2, 'Title': 'Game 2', 'Price': 29.99},
        # Add more game data as needed
    ]

    return render(request, 'Home_Page/Home_Page.html', {'games': games})