from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
class PortfolioItem(models.Model):
    # Campos
    image = models.ImageField(upload_to='portfolio')
    caption = models.CharField(max_length=200)
    target_modal = models.CharField(max_length=50)

    def __str__(self):
        return self.caption


class ContactMessage(models.Model):
    # Campos
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name


class SocialLink(models.Model):
    # Campos
    name = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.name

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


class Contact(models.Model):
    # Campos
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.email
    
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