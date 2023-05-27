from django.contrib import admin
from django.urls import path
from blogapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base, name='base'),
    path('registro/', views.registro, name='registro'),
    path('search/', views.search, name='search'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('articles/', views.articles, name='articles'),
    path('create_article/', views.create_article, name='create_article'),
    path('delete/', views.delete_view, name='delete'),
    path('article_delete/', views.ArticleDeleteView.as_view(), name='article_delete'),
    path('article_edit/', views.article_edit, name='article_edit'),
    path('article_confirm_delete/', views.article_confirm_delete, name='article_confirm_delete'),
    path('logout/', views.logout_view, name='logout'),
]

urlpatterns += staticfiles_urlpatterns()
