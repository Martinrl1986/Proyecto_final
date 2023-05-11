from django.shortcuts import render
from boostrap_blog.forms import MiFormulario

# Create your views here.
def index(request):
    return render(request, "blogapp/index.html")

def mi_vista(request):
    if request.method == 'POST':
        form = MiFormulario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            # Procesar los datos del formulario y realizar acciones adicionales
            # ...
            return render(request, 'miapp/exito.html')
    else:
        form = MiFormulario()

    return render(request, 'miapp/mi_vista.html', {'form': form})