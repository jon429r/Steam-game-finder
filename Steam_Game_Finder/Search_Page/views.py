from django.shortcuts import render

# Create your views here.
def search_page_view(request):
    return render(request, 'Search_Page/Search_Page.html', {})