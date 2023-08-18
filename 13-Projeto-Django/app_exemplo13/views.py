from django.shortcuts import render

# Create your views here.
def home(request):
    
    return render(
        request,
        'app_exemplo13/pages/home.html',
        context={
            'exemplo13': 'Exemplo13',
        }
    )