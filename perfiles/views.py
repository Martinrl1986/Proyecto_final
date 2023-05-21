from django.shortcuts import render, redirect
from django.urls import reverse
from perfiles.forms import UserRegisterForm
from blogapp.models import PortfolioItem
from boostrap_blog.forms import SearchForm

def index(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            url_exitosa = reverse('index')
            return redirect(url_exitosa)
    else:  # GET
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='perfiles/index.html',
        context={'form': formulario},
    )

def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            url_exitosa = reverse('index')
            return redirect(url_exitosa)
    else:  # GET
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='perfiles/registro.html',
        context={'form': formulario},
    )

def search(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = PortfolioItem.objects.filter(caption__icontains=query)

    search_form = SearchForm()

    return render(request, 'search_results.html', {'results': results, 'search_form': search_form})
