from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from boostrap_blog.forms import UserRegisterForm, SearchForm, ContactMessageForm
from blogapp.models import PortfolioItem, ContactMessage
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect


def base(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            url_exitosa = reverse('base')
            return redirect(url_exitosa)
    else:
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='base.html',
        context={'form': formulario},
    )

def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            url_exitosa = reverse('base')
            return redirect(url_exitosa)
    else:
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='registro.html',
        context={'form': formulario},
    )

def search(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = PortfolioItem.objects.filter(caption__icontains=query)

    search_form = SearchForm()

    return render(request, 'search.html', {'results': results, 'search_form': search_form})

def portfolio(request):
    portfolio_items = PortfolioItem.objects.all()
    return render(request, 'portfolio.html', {'portfolio_items': portfolio_items})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html', {'success_message': 'Message sent successfully!'})
    else:
        form = ContactMessageForm()
    return render(request, 'contact.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirige a la página de inicio o a cualquier otra página deseada
            return redirect('home')
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')