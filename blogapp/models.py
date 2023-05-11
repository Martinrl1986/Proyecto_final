from django.db import models

# Create your models here.
from django.db import models

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
