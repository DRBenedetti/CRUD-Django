from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Pessoa

def criar_pessoa(request):
    if request.method == "GET":
        pessoas = Pessoa.objects.all()
        return render(request, 'criar_pessoa.html', {'pessoas':pessoas})
    
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        nasc = request.POST.get('nasc')

        user = Pessoa(
            nome=nome,
            email=email,
            data_nasc=nasc,
        )

        user.save()

        return redirect('criar_pessoa')
    
def deletar_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    pessoa.delete()

    return redirect('criar_pessoa')

def atualizar_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)

    nome = request.POST.get('nome')
    email = request.POST.get('email')
    nasc = request.POST.get('nasc')

    pessoa.nome = nome
    pessoa.email = email
    pessoa.data_nasc = nasc

    pessoa.save()
    return redirect('criar_pessoa')
    