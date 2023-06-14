from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, User
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django import forms

class PortfolioItem(models.Model):
    # Campos
    image = models.ImageField(upload_to='portfolio')
    caption = models.CharField(max_length=200)
    target_modal = models.CharField(max_length=50)

    def __str__(self):
        return self.caption

class SearchForm(models.Model):
    query = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query
    
class Portfolio(models.Model):
    # Campos
    title = models.CharField(max_length=200)
    description = models.TextField()
    items = models.ManyToManyField('PortfolioItem')

    def __str__(self):
        return self.title


class About(models.Model):
    # Campos
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    # Atributos adicionales para tu modelo CustomUser

    # Relación many-to-many con Group utilizando el modelo intermedio CustomUserGroup
    groups = models.ManyToManyField(Group, through='CustomUserGroup', related_name='custom_users', blank=True)

    # Relación many-to-many con Permission utilizando el modelo intermedio CustomUserPermission
    user_permissions = models.ManyToManyField(Permission, through='CustomUserPermission', related_name='custom_users', blank=True)

    class Meta:
        # Otras opciones de configuración del modelo
        pass

# Modelo intermedio para la relación many-to-many entre CustomUser y Group
class CustomUserGroup(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        # Otras opciones de configuración del modelo
        pass

# Modelo intermedio para la relación many-to-many entre CustomUser y Permission
class CustomUserPermission(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        # Otras opciones de configuración del modelo
        pass
    
class Login(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.username
    
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    body = models.TextField()
    author = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.title

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'subtitle', 'body', 'author', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'readonly': 'readonly'})
        }  
class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('articles')
    template_name = 'article_confirm_delete.html'