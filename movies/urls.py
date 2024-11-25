from django.urls import path
from .views import *

urlpatterns = [
    path('<int:movie_id>/', movie),
    path('', index)
]