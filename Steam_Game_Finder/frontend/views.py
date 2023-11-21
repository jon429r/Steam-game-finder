from django.shortcuts import render

def home_page_view(request):

    resulting_games = [
    {'ID': 3, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 1', 'Price': 39.99},
    {'ID': 4, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 2', 'Price': 49.99},
    # Add more popular game data as needed
    ]

    popular_games = [
    {'ID': 3, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 1', 'Price': 39.99},
    {'ID': 4, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 2', 'Price': 49.99},
    # Add more popular game data as needed
    ]

    print(resulting_games)
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


######################May not need these functions######################

def results_page_view(request):
    resulting_games = [
        {'ID': 3, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 1', 'Price': 39.99},
        {'ID': 4, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 2', 'Price': 49.99},
        # Add more popular game data as needed
    ]
    print(resulting_games)
    return render(request, 'Home_Page/Home_Page.html', {'resulting_games': resulting_games, 'section1': 'Resulting Games'})

def popular_page_view(request):
    popular_games = [
        {'ID': 3, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 1', 'Price': 39.99},
        {'ID': 4, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 2', 'Price': 49.99},
        # Add more popular game data as needed
    ]
    return render(request, 'Base_Temp/Base.html', {'popular_games': popular_games, 'section1': 'Popular Games'})


def display_resulting_games(request):
    games = [
        {'ID': 1, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'The Elder Scrolls V: Skyrim', 'Price': 19.99},
        {'ID': 2, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Game 2', 'Price': 29.99},
        # Add more game data as needed
    ]
    print(games)
    return render(request, 'Home_Page/Home_Page.html', {'games': games, 'section2': 'Games'})

def display_popular_games(request):
    popular_games = [
        {'ID': 3, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 1', 'Price': 39.99},
        {'ID': 4, 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'Title': 'Popular Game 2', 'Price': 49.99},
        # Add more popular game data as needed
    ]
    print(popular_games)
    return render(request, 'Base_Temp/Base.html', {'popular_games': popular_games, 'section1': 'Popular Games'})
