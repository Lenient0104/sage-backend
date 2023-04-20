from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import DublinStops, FavouriteLocations, Edges


class DublinStopsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = DublinStops
        geo_field = "location"
        id_field = "stop_id"
        fields = "__all__"


class EdgeSerializer(serializers.Serializer):
    class Meta:
        model = Edges
        geo_field = "edge"
        fields = "__all__"


class FavouriteLocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteLocations
        fields = ('id', 'user_id', 'name', 'place_id',
                  'location', 'created_at', 'updated_at')
