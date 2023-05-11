from django import forms

class MiFormulario(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea)