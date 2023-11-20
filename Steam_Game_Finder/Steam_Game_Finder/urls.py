'''yourproject/urls.py:
This file defines the URL patterns for your project. 
It specifies how URLs are mapped to view functions. 
You can create route patterns to determine what views should handle different URLs.'''
"""
URL configuration for Steam_Game_Finder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from django.urls import include


from frontend.views import home_page_view, quiz_page_view, search_page_view, display_resulting_games, display_popular_games, base_temp_view, results_page_view, popular_page_view
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),

    path('Base.html', base_temp_view, name='Base.html'),
    path('Base_Temp/Base.html', base_temp_view, name='Base.html'),

    ##Page that opens by default when the server is started
    path('', home_page_view, name='Home_Page.html'),
    
    path('Home_Page.html', home_page_view, name='Home_Page.html'),
    path('Quiz_Page.html', quiz_page_view, name='Quiz_Page.html'),
    path('Search_Page.html', search_page_view, name='Search_Page.html'),
    
    path('Home_Page/Home_Page.html', home_page_view, name='Home_Page.html'),
    path('Quiz_Page/Quiz_Page.html', quiz_page_view, name='Quiz_Page.html'),
    path('Search_Page/Search_Page.html', search_page_view, name='Search_Page.html'),
    
    ##path('Extras/', display_popular_games, name='Popular_Table.html'),
    path('Extras/Popular_Table.html', display_popular_games, name='Popular_Table.html'),

    ##path('Extras/', display_resulting_games, name='Result_Table.html'),
    path('Extras/Result_Table.html', display_resulting_games, name='Result_Table.html'),

    path('display_popular_games/', display_popular_games, name='display_popular_games'),
    path('display_resulting_games/', display_resulting_games, name='display_resulting_games'),
    ]