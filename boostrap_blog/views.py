from django.shortcuts import render, redirect
from django.urls import reverse
from boostrap_blog.forms import UserRegisterForm
from boostrap_blog.forms import PortfolioItem
from boostrap_blog.forms import ContactMessage
from boostrap_blog.forms import AboutForm
from blogapp.models import PortfolioItem
from boostrap_blog.forms import SearchForm

def base(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            url_exitosa = reverse('base')
            return redirect(url_exitosa)
    else:  # GET
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='blogapp/base.html',
        context={'form': formulario},
    )

def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            url_exitosa = reverse('base')
            return redirect(url_exitosa)
    else:  # GET
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='blogapp/registro.html',
        context={'form': formulario},
    )

def search(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = PortfolioItem.objects.filter(caption__icontains=query)

    search_form = SearchForm()

    return render(request, 'search_results.html', {'results': results, 'search_form': search_form})

def portfolio(request):
    # Lógica de la vista para portfolio.html
    # Puedes obtener los objetos del modelo PortfolioItem y pasarlos al template
    portfolio_items = PortfolioItem.objects.all()
    return render(request, 'portfolio.html', {'portfolio_items': portfolio_items})

def about(request):
    # Lógica de la vista para about.html
    return render(request, 'about.html')

def contact(request):
    # Lógica de la vista para contact.html
    if request.method == 'POST':
        # Si se envió un formulario de contacto
        # Puedes procesar los datos del formulario y guardarlos en el modelo ContactMessage
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact_message = ContactMessage(name=name, email=email, phone=phone, message=message)
        contact_message.save()
        # Puedes realizar otras acciones, como enviar un correo electrónico de notificación, etc.
        return render(request, 'contact.html', {'success_message': 'Message sent successfully!'})
    else:
        return render(request, 'contact.html')