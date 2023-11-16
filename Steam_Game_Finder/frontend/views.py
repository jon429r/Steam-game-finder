from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return render(request, 'Home_Page/Home_Page.html')

def quiz_page_view(request):
    return render(request, 'Quiz_Page/Quiz_Page.html')

def search_page_view(request):
    return render(request, 'Search_Page/Search_Page.html', {})