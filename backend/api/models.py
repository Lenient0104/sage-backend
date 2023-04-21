
from django.contrib.gis.db import models


class FavouriteLocations(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=45, blank=False, null=False)

    name = models.CharField(max_length=45, blank=True, null=True)
    place_id = models.CharField(max_length=45, blank=True, null=True)
    location = models.PointField(blank=False, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Edges(models.Model):
    edge = models.LineStringField(blank=False, null=False)
    customer_route_name = models.CharField(blank=False, null=False)
    start_node = models.CharField(blank=False, null=False)
    end_node = models.CharField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'edges'


class DublinStops(models.Model):
    stop_id = models.CharField(primary_key=True, max_length=20)
    stop_name = models.CharField(max_length=100, blank=True, null=True)
    stop_lat = models.DecimalField(
        max_digits=10, decimal_places=8, blank=True, null=True)
    stop_lon = models.DecimalField(
        max_digits=10, decimal_places=8, blank=True, null=True)
    location = models.PointField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'dublin_stops'


class DublinBusRoutes(models.Model):
    stop_id = models.CharField(max_length=45, blank=True, null=True)
    stop_name = models.CharField(max_length=45, blank=True, null=True)
    stop_lat = models.DecimalField(
        max_digits=10, decimal_places=8, blank=True, null=True)
    stop_lon = models.DecimalField(
        max_digits=10, decimal_places=8, blank=True, null=True)
    trip_id = models.CharField(max_length=45, blank=True, null=True)
    arrival_time = models.CharField(max_length=45, blank=True, null=True)
    departure_time = models.CharField(max_length=45, blank=True, null=True)
    stop_sequence = models.IntegerField(blank=True, null=True)
    stop_headsign = models.CharField(max_length=45, blank=True, null=True)
    shape_dist_traveled = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    route_id = models.CharField(max_length=45, blank=True, null=True)
    customer_route = models.CharField(max_length=45, blank=True, null=True)
    project_subnet = models.CharField(max_length=45, blank=True, null=True)
    the_geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dublin_bus_routes'


class Routes(models.Model):
    stop_id = models.CharField(max_length=45, blank=True, null=True)
    stop_name = models.CharField(max_length=45, blank=True, null=True)
    stop_lat = models.DecimalField(
        max_digits=10, decimal_places=8, blank=True, null=True)
    stop_lon = models.DecimalField(
        max_digits=10, decimal_places=8, blank=True, null=True)
    trip_id = models.CharField(max_length=45, blank=True, null=True)
    arrival_time = models.CharField(max_length=45, blank=True, null=True)
    departure_time = models.CharField(max_length=45, blank=True, null=True)
    stop_sequence = models.IntegerField(blank=True, null=True)
    stop_headsign = models.CharField(max_length=45, blank=True, null=True)
    shape_dist_traveled = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    route_id = models.CharField(max_length=45, blank=True, null=True)
    customer_route = models.CharField(max_length=45, blank=True, null=True)
    project_subnet = models.CharField(max_length=45, blank=True, null=True)
    geo_point = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'routes'


class Shapes(models.Model):
    shape_id = models.CharField(max_length=30, blank=True, null=True)
    shape_pt_lat = models.DecimalField(
        max_digits=10, decimal_places=8, blank=True, null=True)
    shape_pt_lon = models.DecimalField(
        max_digits=10, decimal_places=8, blank=True, null=True)
    shape_pt_sequence = models.IntegerField(blank=True, null=True)
    shape_dist_traveled = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    routes_point = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shapes'


class ShpShp(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    file = models.CharField(max_length=100)
    upload_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'shp_shp'
