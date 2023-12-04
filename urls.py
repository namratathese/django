#from django.contrib import admin
from django.urls import path,include
#from watchlist_app.api.views import movie_list,movie_details   #=======fun based views name========
from watchlist_app.api.views import WatchListAV,WatchDetailAV,StreamPlatformAV,StreamPlatformDetailAV #=======class views name========

#========[MovieListAV,MovieDetailAV]=============


urlpatterns = [
    path('list/', WatchListAV.as_view(),name='movie-list'),
    path('<int:pk>',WatchDetailAV.as_view(),name='movie-detail'),
    path('stream/',StreamPlatformAV.as_view(),name='stream'),
    path('stream/<int:pk>',StreamPlatformDetailAV.as_view(),name='stream-detail'),

]   

