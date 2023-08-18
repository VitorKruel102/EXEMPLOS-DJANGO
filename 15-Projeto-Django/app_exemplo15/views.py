from django.shortcuts import render
from django.urls import reverse

from app_exemplo15.models import Produtos
from app_exemplo15.forms import ContatoForm


def home(request):
    registro_do_contato = request.session.get('registro_do_contato', None)

    form = ContatoForm(registro_do_contato)
    _produto = Produtos.objects.all()
    
    print(form.is_valid())
    
    return render(
        request,
        'exemplo15/pages/home.html',
        context={
            'produtos': _produto,
            'form': form,
            'form_action': reverse('exemplo15:create')
        }
    )

def register_create(request):
    if not request.POST:
        raise Http404()  

    POST = request.POST
    print('ola')
    request.session['registro_do_contato'] = POST

    form = ContatoForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.senha)
        user.save()

        messages.success(request,'Your user is created, please log in.')

        del(request.session['register_form_data']) 

    print(form.is_valid())
    return redirect('exemplo15:home')    