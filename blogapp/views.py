from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from boostrap_blog.forms import UserRegisterForm, SearchForm, ContactMessageForm
from blogapp.models import PortfolioItem
from django.contrib.auth import login, authenticate, logout
from blogapp.models import Login
from .models import Article
from boostrap_blog.forms import ArticleForm
from django.views.generic import DeleteView




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

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirige a la página de inicio o a cualquier otra página deseada
            return redirect('base')
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
    
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')  # Redirigir a la vista de la lista de artículos    
    else:
        form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})

def article_delete(request, id):
    article = get_object_or_404(Article, pk=id)
    if request.method == 'POST':
        article.delete()
        return redirect('home')  # Redirige a la página de inicio después de eliminar el artículo
    return render(request, 'article_delete.html', {'article': article})

def article_confirm_delete(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    if request.method == 'POST':
        # El usuario ha confirmado la eliminación del artículo
        article.delete()
        return redirect('articles')

    return render(request, 'article_confirm_delete.html', {'article': article})


def article_edit(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            # Obtener el pk del artículo guardado
            pk = article.pk
            edit_url = reverse('article_edit', kwargs={'pk': pk})
            return redirect(edit_url)  # Redirige a la vista de edición del artículo
    else:
        form = ArticleForm()
    return render(request, 'article_edit.html', {'form': form})
class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'articles/article_confirm_delete.html'
    success_url = reverse_lazy('articles.html')

def logout_view(request):
    logout(request)
    return redirect('base')

def articles(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})

def delete_view(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        article.delete()
        return redirect('articles.html')
    return render(request, 'articles/article_confirm_delete.html', {'article': article})
