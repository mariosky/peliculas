from django.shortcuts import render
from django.http import HttpResponse
from movies.models import Movie
from movies.forms import MoviewReviewForm

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = { 'movies':movies, 'message':'welcome' }
    return render(request,'movies/index.html', context=context )
    
def movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    review_form = MoviewReviewForm()
    context = { 'movie':movie, 'saludo':'welcome', 'review_form':review_form }
    return render(request,'movies/movie.html', context=context )
    