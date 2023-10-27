'''HomePage/views.py:
This file contains view functions, which handle HTTP requests and return HTTP responses. 
You define how data is presented to the user in these functions.'''
from django.shortcuts import render

##create your views here

def home_page_view(request):
    return render(request, 'Home_Page/Home_Page.html')