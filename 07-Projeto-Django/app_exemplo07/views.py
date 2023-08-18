from django.shortcuts import render

# Create your views here.
def home(request):
    return render(
        request,
        'app_exemplo07/pages/home.html',
        context={
            'exemplo': 1
        }
    )