from django import forms
from django.contrib.auth.forms import UserCreationForm
from blogapp.models import PortfolioItem, ContactMessage, SocialLink, SearchForm
from blogapp.models import CustomUser
from blogapp.models import About
from blogapp.models import Article

class PortfolioItemForm(forms.ModelForm):
    class Meta:
        model = PortfolioItem
        fields = ['image', 'caption', 'target_modal']
        
        
class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']

class SocialLinkForm(forms.ModelForm):
    class Meta:
        model = SocialLink
        fields = ['name', 'url']

class PortfolioItemForm(forms.ModelForm):
    class Meta:
        model = PortfolioItem
        fields = ('image', 'caption', 'target_modal')

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'phone', 'message')

class SearchForm(forms.Form):
    query = forms.CharField(max_length=200)
    
class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['title', 'description']
        
class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    
class SignUpForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
        
class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']
        
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'subtitle', 'body', 'author', 'date']
        
class ArticleDeleteForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = []
        