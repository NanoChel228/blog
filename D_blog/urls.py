from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<slug:slug>', views.post_detail, name='post_detail_url'),
    path('register/', views.register, name='register'),
    path('login/', views.login_site, name='login_url'),
    path('logout/', views.logout_site, name='logout_url'),
    path('posts/<slug:slug>/comment', views.comment, name='comment'),
    path('categories/<slug:slug>', views.category_detail, name='category_detail_url'),
    path('search/', views.search_function, name = 'search_url'),
    path('posts/', views.posts, name = 'posts_url'),
    path('categories/', views.categories, name = 'categories_url')
]
