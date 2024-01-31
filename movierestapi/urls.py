from django.contrib import admin
from django.urls import path
from movieapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', views.genre_list, name='genre-list'),
    path('persons/', views.person_list, name='person-list'),
    path('movies/', views.movie_list, name='movie-list'),
]
