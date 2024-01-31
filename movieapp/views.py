from django.http import JsonResponse
from .models import  Genre, Person, Movie

def genre_list(request):
    genres = list(Genre.objects.values())
    return JsonResponse(genres, safe=False)

def person_list(request):
    persons = list(Person.objects.values())
    return JsonResponse(persons, safe=False)

def movie_list(request):
    movies = list(Movie.objects.values())
    return JsonResponse(movies, safe=False)