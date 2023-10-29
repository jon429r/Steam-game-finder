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
from Home_Page import views
from django.contrib import admin

from Home_Page.views import home_page_view
from Quiz_Page.views import quiz_page_view
from Search_Page.views import search_page_view
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page_view, name='Home_Page'),
    path('', quiz_page_view, name='Quiz_Page'),
    path('', search_page_view, name='Search_Page'),
    path('Steam_Game_Finder/Quiz_Page/templates/Quiz_Page/Quiz_Page.html', quiz_page_view, name='Quiz_Page'),
    path('Quiz/templates/Quiz_Page/Quiz_Page.html', quiz_page_view, name='Quiz_Page'),
    path('Steam_Game_Finder/Home_Page/templates/Home_Page/Home_Page.html', home_page_view, name='Home_Page'),
    path('', search_page_view, name='Search_Page'),
    path('Home_Page.html', home_page_view, name='Home_Page.html'),
    path('Steam_Game_Finder/Search_Page/templates/Search_Page/Search_Page.html', search_page_view, name='Search_Page'),
]

