import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Receitas, Ingrediente

# Create your views here.
#CREATE

def criar_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST.get('nome_receita')
        passos = request.POST.get('passos')
        tempo_preparo = request.POST.get('tempo_preparo')
        receita = Receitas.objects.create(
            nome_receita=nome_receita,
            passos=passos,
            tempo_preparo=tempo_preparo
        )
        id_ingredientes = request.POST.getlist('ingredientes')
        for id in id_ingredientes:
            receita.ingredientes.add(Ingrediente.objects.get(id=id))
        return redirect('detalhe_receita', pk=receita.pk)
    ingredientes = Ingrediente.objects.all()
    return render(request, 'receita/form_receita.html', {'ingredientes': ingredientes})
        

#READ
def listar_receitas(request):
    receitas = Receitas.objects.all()
    return render(request, 'receita/listar_receitas.html', {'receitas': receitas})

def detalhe_receita(request, pk):
    receita = get_object_or_404(Receitas, pk=pk)
    return render(request, 'receita/detalhe_receitas.html', {'receita': receita})


def editar_receita(request, pk):
    receita = get_object_or_404(Receitas, pk=pk)
    if request.method == 'POST':
        receita.nome_receita = request.POST.get('nome_receita')
        receita.passos = request.POST.get('passos')
        receita.tempo_preparo = request.POST.get('tempo_preparo')
        receita.save()
        receita.ingredientes.clear()
        id_ingredientes = request.POST.getlist('ingredientes')
        for ing_id in id_ingredientes:
            ingrediente = Ingrediente.objects.get(id=ing_id)
            receita.ingredientes.add(ingrediente)
        return redirect('detalhe_receita', pk=receita.pk)
    ingredientes = Ingrediente.objects.all()
    return render(request, 'receita/form_receita.html', {'receita': receita, 'ingredientes': ingredientes})
        
#DELETE
def deletar_receita(request, pk):
    receita = get_object_or_404(Receitas, pk=pk)
    if request.method == 'POST':
        receita.delete()
        return redirect('listar_receitas')
    return render(request, 'receita/deletar_receitas.html', {'receita': receita})

#import
def importar_receita(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        url = f'https://www.themealdb.com/api/json/v1/1/search.php?s={search}'
        response = requests.get(url)
        data = response.json()

        if data['meals']:
            receita_id = data['meals'][0]
            nova_receita = Receitas.objects.create(
                nome_receita=receita_id['strMeal'],
                passos=receita_id['strInstructions'],
                tempo_preparo=45
            )
            for ing in range(1, 21):
                nome_ingrediente = receita_id.get(f'strIngredient{ing}')
                if nome_ingrediente and nome_ingrediente.strip():
                    ingrediente, created = Ingrediente.objects.get_or_create(nome=nome_ingrediente)
                    nova_receita.ingredientes.add(ingrediente)
        else:
            return render(request, 'receita/importar_receita.html', {'erro': 'A receita não foi encontrada.'})
        return redirect('detalhe_receita', pk=nova_receita.pk)
    return render(request, 'receita/importar_receita.html')