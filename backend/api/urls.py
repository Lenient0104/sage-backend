from . import views
from django.urls import path
from .views import DublinStopsList, FavouriteLocationsListCreateAPIView, EdgesList

urlpatterns = [
    path('busstops/', DublinStopsList.as_view(), name='busstop-list'),
    path('favourite_locations/', FavouriteLocationsListCreateAPIView.as_view(),
         name='favourite_locations'),
    path('shortest_path/', EdgesList.as_view(), name='shortest_path')
]
