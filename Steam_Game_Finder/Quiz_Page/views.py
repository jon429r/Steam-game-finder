from django.shortcuts import render

# Create your views here.
def quiz_page_view(request):
    return render(request, 'Quiz_Page/Quiz_Page.html')
