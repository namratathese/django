#from django.contrib import admin
from django.urls import path,include
#from watchlist_app.api.views import movie_list,movie_details   #=======fun based views name========
from watchlist_app.api.views import MovieListAV,MovieDetailAV  #=======class views name========
urlpatterns = [
    path('list/', MovieListAV.as_view(),name='movie-list'),
    path('<int:pk>',MovieDetailAV.as_view(),name='movie-detail'),
]
