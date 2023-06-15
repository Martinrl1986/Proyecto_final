from django.contrib import admin
from django.urls import path
from blogapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base, name='base'),
    path('search/', views.search, name='search'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('articles/', views.articles, name='articles'),
    path('article_list/', views.article_list, name='article_list'),
    path('create_article/', views.create_article, name='create_article'),
    path('article_delete/', views.article_delete, name='article_delete'),
    path('article_edit/', views.article_edit, name='article_edit'),
    path('logout/', views.logout_view, name='logout'),
]

urlpatterns += staticfiles_urlpatterns()