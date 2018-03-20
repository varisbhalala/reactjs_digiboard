# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

#Updated 7-3-2018

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DataAdvertisement(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    advertiser = models.ForeignKey('DataAdvertiser', models.DO_NOTHING, db_column='Advertiser_id')  # Field name made lowercase.
    board = models.ForeignKey('DataBoard', models.DO_NOTHING, db_column='Board_id')  # Field name made lowercase.
    slot = models.ForeignKey('DataSlot', models.DO_NOTHING)
    upload = models.ForeignKey('DataUpload', models.DO_NOTHING, db_column='Upload_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_advertisement'


class DataAdvertiser(models.Model):
    name = models.TextField()
    contact = models.BigIntegerField(blank=True, null=True)
    avatar = models.CharField(max_length=100)
    company_name = models.TextField()
    company_address = models.TextField()
    city = models.TextField()
    state = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('DataUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'data_advertiser'


class DataBoard(models.Model):
    lat = models.DecimalField(max_digits=10, decimal_places=8)
    lng = models.DecimalField(max_digits=11, decimal_places=8)
    street = models.TextField()
    area = models.TextField()
    city = models.TextField()
    state = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    publisher = models.ForeignKey('DataPublisher', models.DO_NOTHING, db_column='Publisher_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_board'


class DataCities(models.Model):
    name = models.CharField(max_length=30)
    state_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'data_cities'


class DataLog(models.Model):
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField()
    advertisement = models.ForeignKey(DataAdvertisement, models.DO_NOTHING, db_column='Advertisement_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_log'


class DataPayment(models.Model):
    price = models.FloatField()
    service_tax_ratio = models.FloatField()
    service_tax = models.FloatField()
    total_amount = models.FloatField()
    token = models.TextField()
    transaction_type = models.TextField()
    pay_log = models.TextField()
    created_at = models.DateTimeField()
    advertiser = models.ForeignKey(DataAdvertiser, models.DO_NOTHING, db_column='Advertiser_id')  # Field name made lowercase.
    publisher = models.ForeignKey('DataPublisher', models.DO_NOTHING, db_column='Publisher_id')  # Field name made lowercase.
    slot = models.ForeignKey('DataSlot', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'data_payment'


class DataPublisher(models.Model):
    name = models.TextField()
    contact = models.BigIntegerField(blank=True, null=True)
    avatar = models.CharField(max_length=100)
    company_name = models.TextField()
    company_address = models.TextField()
    city = models.TextField()
    state = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('DataUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'data_publisher'


class DataRequestboard(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    advertiser = models.ForeignKey(DataAdvertiser, models.DO_NOTHING, db_column='Advertiser_id')  # Field name made lowercase.
    board = models.ForeignKey(DataBoard, models.DO_NOTHING, db_column='Board_id')  # Field name made lowercase.
    publisher = models.ForeignKey(DataPublisher, models.DO_NOTHING, db_column='Publisher_id')  # Field name made lowercase.
    slot = models.ForeignKey('DataSlot', models.DO_NOTHING)
    request_status = models.SmallIntegerField(blank=True, null=True)
    approve_status = models.SmallIntegerField(blank=True, null=True)
    shown = models.SmallIntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_requestboard'


class DataSlot(models.Model):
    from_field = models.TimeField(db_column='from_')  # Field renamed because it ended with '_'.
    to = models.TimeField()
    total = models.IntegerField()
    slot_price = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    board = models.ForeignKey(DataBoard, models.DO_NOTHING, db_column='Board_id')  # Field name made lowercase.
    publisher = models.ForeignKey(DataPublisher, models.DO_NOTHING, db_column='Publisher_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_slot'


class DataStates(models.Model):
    name = models.CharField(max_length=30)
    country_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'data_states'


class DataUpload(models.Model):
    type = models.TextField()
    location = models.TextField()
    upload_date = models.DateTimeField()
    current_state = models.IntegerField()
    seconds = models.BigIntegerField()
    upload_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    advertiser = models.ForeignKey(DataAdvertiser, models.DO_NOTHING, db_column='Advertiser_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_upload'


class DataUser(models.Model):
    username = models.CharField(unique=True, max_length=10)
    password = models.TextField()
    email = models.CharField(unique=True, max_length=30)
    token = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    role = models.TextField()

    class Meta:
        managed = False
        db_table = 'data_user'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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
