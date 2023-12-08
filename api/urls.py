#from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
#from watchlist_app.api.views import movie_list,movie_details   #=======fun based views name========
from watchlist_app.api.views import (WatchListAV,WatchDetailAV,
                                     StreamPlatformAV,
                                     StreamPlatformDetailAV,StreamPlatformVS,
                                     ReviewList,ReviewDetail,ReviewCreate) #=======class views name========

#========[MovieListAV,MovieDetailAV]=============

#=================================use of routers instead of urls-paths==================================
router = DefaultRouter()
router.register('stream',StreamPlatformVS,basename='streamplatform')

#====================================urls paths==========================================================
urlpatterns = [
    path('list/', WatchListAV.as_view(),name='movie-list'),
    path('<int:pk>/',WatchDetailAV.as_view(),name='movie-detail'),
    
    path('',include(router.urls)),
    
    #path('stream/',StreamPlatformAV.as_view(),name='stream'),
    #path('stream/<int:pk>',StreamPlatformDetailAV.as_view(),name='streamplatform-detail'),
    
    # path('stream/<int:pk>/review-create',ReviewCreate.as_view(),name='review-create'),

    # path('stream/<int:pk>/review',ReviewList.as_view(),name='review-list'),
    # path('stream/review/<int:pk>',ReviewDetail.as_view(),name='review-detail'),
    
    
    path('<int:pk>/review-create/',ReviewCreate.as_view(),name='review-create'),

    path('<int:pk>/reviews/',ReviewList.as_view(),name='review-list'),
    path('review/<int:pk>/',ReviewDetail.as_view(),name='review-detail'),
]   

