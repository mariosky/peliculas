
# Register your models here.
from django.contrib import admin

from movies.models import Movie, Genre, Job, Person, MovieCredit 

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Job)
admin.site.register(Person)
admin.site.register(MovieCredit)