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
from django.urls import path, include
from django.contrib import admin
from frontend.views import (
    home_page_view, quiz_page_view, search_page_view, like_view, dislike_view,
    base_temp_view,  error_page_view, results, info_page_view
)
app_name = 'frontend'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_page_view, name='home_page'),

    path('', home_page_view, name='Home_Page.html'),
    path('Templates/Home_Page/Home_Page.html', home_page_view, name='Home_Page.html'),

    path('Quiz_Page.html', quiz_page_view, name='Quiz_Page.html'),
    path('Search_Page.html', search_page_view, name='Search_Page.html'),
    path('results/', results, name='results'),

    path('Extras/Quiz_Table.html', quiz_page_view, name='quiz_page_view'),

    path('Extras/Error_Page.html', error_page_view, name='error_page_view'),

    path('Info_Page.html', info_page_view, name='info_page_view'),

    path('like_game/', like_view, name='like_game'),
    path('dislike_game/', dislike_view, name='dislike_game'),

    path('results', results, name='results'),
]