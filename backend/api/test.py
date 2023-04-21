from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import DublinStops, FavouriteLocations, Edges
from .serializers import DublinStopsSerializer, FavouriteLocationsSerializer, EdgeSerializer


# class DublinStopsListTestCase(TestCase):

#     def test_dublin_stops_list(self):
#         response = self.client.get(reverse("busstop-list"), {
#                                    "lat": 53.32156775855333, "lng": -6.427001806684125, "radius": 1000})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data["features"]) > 0, True)


# class EdgesListTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()

#     def test_shortest_path(self):
#         request_data = {
#             "feature_collection": {
#                 "type": "FeatureCollection",
#                 "features": []
#             },
#             "from_point": [-6.26031, 53.349805],
#             "to_point": [-6.26131, 53.348805]
#         }
#         response = self.client.post(
#             reverse("shortest_path"), data=request_data, format="json")
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertIsNotNone(response.data["coordinates"])


class FavouriteLocationsListCreateAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create some sample FavouriteLocations objects
        self.favourite_location1 = FavouriteLocations.objects.create(
            user_id="1", name="Location 1", place_id="123", location="POINT(-6.26031 53.349805)"
        )
        self.favourite_location2 = FavouriteLocations.objects.create(
            user_id="2", name="Location 2", place_id="124", location="POINT(-6.26131 53.348805)"
        )

    def test_favourite_locations_list(self):
        response = self.client.get(reverse("favourite_locations"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_favourite_locations_create(self):
        new_location_data = {
            "user_id": "3",
            "name": "Location 3",
            "place_id": "125",
            "location": {"type": "Point", "coordinates": [-6.26231, 53.347805]},
        }
        response = self.client.post(
            reverse("favourite_locations"), data=new_location_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FavouriteLocations.objects.count(), 3)
