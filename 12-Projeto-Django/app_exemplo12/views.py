from django.shortcuts import render

# Create your views here.
def home(request):
    return render(
        request,
        'app_exemplo12/pages/home.html',
        context={
            'exemplo12': 12,
        }
    )