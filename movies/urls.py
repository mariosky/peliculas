from django.urls import path
from .views import *

urlpatterns = [
    path('<int:movie_id>/', movie),
    path('movie_review/add/<int:movie_id>/', add_review),
    path('', index)
]