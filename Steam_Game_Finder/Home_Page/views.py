'''HomePage/views.py:
This file contains view functions, which handle HTTP requests and return HTTP responses. 
You define how data is presented to the user in these functions.'''
from django.shortcuts import render

##create your views here

def home_page_view(request):
    return render(request, 'Home_Page/Home_Page.html')

def quiz_page_view(request):
    return render(request, 'Quiz_Page/Quiz_Page.html')

def search_page_view(request):
    return render(request, 'Search_Page/Search_Page.html', {})