import pandas as pd
from rest_framework import generics, status
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon, Point
from django.contrib.gis.measure import D
import json
import networkx as nx

from rest_framework.response import Response

from rest_framework_gis.pagination import GeoJsonPagination

from .models import DublinStops, FavouriteLocations, Edges
from .serializers import DublinStopsSerializer, FavouriteLocationsSerializer, EdgeSerializer
import os
from django.core.serializers import serialize
from rest_framework.renderers import JSONRenderer

import networkx as nx

#  create a multidigraph
G = nx.MultiDiGraph()

# use pandas to read the csv file

stops = pd.read_csv("dublin_stops.csv")

# loop over the stops and add them to the graph
for row in stops.itertuples():
    G.add_node(row[1], stop_name=row[2], stop_lat=row[3], stop_lon=row[4])

for dir in os.listdir("seperated_routes"):
    # print the path of the folder
    dir_path = os.path.join("seperated_routes", dir)
    if not os.path.isdir(dir_path):
        continue

    # loop over the files in the folder
    for file in os.listdir(dir_path):
        # read the data as a dataframe
        data = pd.read_csv(os.path.join(dir_path, file))
        for i, row in enumerate(data.itertuples()):
            if i == 0:
                continue
            # get the previous row
            prev_row = data.iloc[i-1]
            # add the edge to the graph
            # print(prev_row[1],row[2])
            G.add_edge(prev_row[1], row[2], cost=1, stop_sequence=row[9],
                       trip_id=row[6], customer_route_name=row[13], type="bus")


def calculate_weight(nodeA, nodeB, edge):
    nodeA_buses = set()
    for neighbor, edge_attrs in G[nodeA].items():
        for edge in edge_attrs.values():
            if edge["type"] == "bus":
                nodeA_buses.add(edge["trip_id"])

    nodeB_buses = set()
    for neighbor, edge_attrs in G[nodeB].items():
        for edge in edge_attrs.values():
            if edge["type"] == "bus":
                nodeB_buses.add(edge["trip_id"])

    if nodeA_buses.intersection(nodeB_buses).__len__() > 0:
        return 0

    return 1000


class DublinStopsList(generics.ListAPIView):
    serializer_class = DublinStopsSerializer
    pagination_class = GeoJsonPagination
    distance_filter_field = 'location'
    bbox_filter_include_overlapping = True
    """
    A view that returns a list of all bus stops within a specified radius of a location.

    Parameters:
    - lat (float): The latitude of the location to search for bus stops.
    - lng (float): The longitude of the location to search for bus stops.
    - radius (float): The radius (in meters) around the location to search for bus stops.

    Returns:
    A JSON response containing a list of all bus stops within the specified radius of the location.

    Example:
    GET /api/busstops/?lat=37.7749&lng=-122.4194&radius=1000

    This will return a list of all bus stops within a 1000 meter radius of San Francisco, CA.
    """

    def get_queryset(self):
        """
        Returns a queryset of all bus stops within a specified radius of a location.
        """
        # Get the 'lat', 'lng', and 'radius' parameters from the query string
        lat_str = self.request.query_params.get('lat', None)
        lng_str = self.request.query_params.get('lng', None)
        radius_str = self.request.query_params.get('radius', None)

        # parse the lat, lng, and radius parameters as floats
        try:
            lat = float(lat_str) if lat_str is not None else None
            lng = float(lng_str) if lng_str is not None else None
            radius = float(radius_str) if radius_str is not None else None
        except ValueError:
            return DublinStops.objects.none()

        # If any of the parameters are missing, return an empty queryset
        if lat is None or lng is None or radius is None:
            return DublinStops.objects.none()

        # Convert the lat and lng parameters to a Point object
        location = Point(lng, lat)

        # Filter the BusStop queryset to include only stops within the radius of the specified location
        queryset = DublinStops.objects.filter(
            location__distance_lte=(location, D(m=radius)))

        return queryset


class FavouriteLocationsListCreateAPIView(generics.ListCreateAPIView):
    queryset = FavouriteLocations.objects.all()
    serializer_class = FavouriteLocationsSerializer


def create_feature_collection(features):
    return {
        "type": "FeatureCollection",
        "features": features,
    }


def convert_to_geojson_feature(edge_data):
    geom = edge_data.pop('edge').geojson
    return {
        "type": "Feature",
        "geometry": geom,
        "properties": edge_data,
    }

# given a list of polygons that are geojson, return a list of edges that are within the polygons


class EdgesList(generics.CreateAPIView):
    serializer_class = EdgeSerializer
    pagination_class = GeoJsonPagination
    queryset = Edges.objects.all()

    def create(self, request, *args, **kwargs):
        feature_collection = request.data
        polygons = [GEOSGeometry(json.dumps(feature['geometry']))
                    for feature in feature_collection['features']]

        multipolygon = MultiPolygon(*polygons)

        intersecting_edges_queryset = Edges.objects.filter(
            edge__intersects=multipolygon)

        intersecting_edges = serialize('json', intersecting_edges_queryset)
        return Response(intersecting_edges, status=status.HTTP_201_CREATED)
