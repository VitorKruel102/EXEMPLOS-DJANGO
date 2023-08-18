from django.shortcuts import render

# Create your views here.
def home(request):
    return render(
        request,
        'app_exemplo06/pages/home.html',
        context={}
    )