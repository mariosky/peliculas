from django.shortcuts import render
from django.http import HttpResponse
from movies.models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = { 'movies':movies, 'message':'welcome' }
    return render(request,'movies/index.html', context=context )
    
def movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    
    context = { 'movie':movie, 'saludo':'welcome' }
    return render(request,'movies/movie.html', context=context )
    