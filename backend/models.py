# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApiFavouritelocations(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    place_id = models.CharField(max_length=45, blank=True, null=True)
    location = models.GeometryField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'api_favouritelocations'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DublinBusRoutes(models.Model):
    stop_id = models.CharField(max_length=45, blank=True, null=True)
    stop_name = models.CharField(max_length=45, blank=True, null=True)
    stop_lat = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    stop_lon = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    trip_id = models.CharField(max_length=45, blank=True, null=True)
    arrival_time = models.CharField(max_length=45, blank=True, null=True)
    departure_time = models.CharField(max_length=45, blank=True, null=True)
    stop_sequence = models.IntegerField(blank=True, null=True)
    stop_headsign = models.CharField(max_length=45, blank=True, null=True)
    shape_dist_traveled = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    route_id = models.CharField(max_length=45, blank=True, null=True)
    customer_route = models.CharField(max_length=45, blank=True, null=True)
    project_subnet = models.CharField(max_length=45, blank=True, null=True)
    the_geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dublin_bus_routes'


class DublinStops(models.Model):
    stop_id = models.CharField(primary_key=True, max_length=20)
    stop_name = models.CharField(max_length=100, blank=True, null=True)
    stop_lat = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    stop_lon = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    location = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dublin_stops'


class Edges(models.Model):
    edge = models.GeometryField(blank=True, null=True)
    customer_route_name = models.CharField(blank=True, null=True)
    start_node = models.CharField(blank=True, null=True)
    end_node = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edges'


class Routes(models.Model):
    stop_id = models.CharField(max_length=45, blank=True, null=True)
    stop_name = models.CharField(max_length=45, blank=True, null=True)
    stop_lat = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    stop_lon = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    trip_id = models.CharField(max_length=45, blank=True, null=True)
    arrival_time = models.CharField(max_length=45, blank=True, null=True)
    departure_time = models.CharField(max_length=45, blank=True, null=True)
    stop_sequence = models.IntegerField(blank=True, null=True)
    stop_headsign = models.CharField(max_length=45, blank=True, null=True)
    shape_dist_traveled = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    route_id = models.CharField(max_length=45, blank=True, null=True)
    customer_route = models.CharField(max_length=45, blank=True, null=True)
    project_subnet = models.CharField(max_length=45, blank=True, null=True)
    geo_point = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'routes'


class Shapes(models.Model):
    shape_id = models.CharField(max_length=30, blank=True, null=True)
    shape_pt_lat = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    shape_pt_lon = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    shape_pt_sequence = models.IntegerField(blank=True, null=True)
    shape_dist_traveled = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
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
