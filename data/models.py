from django.db import models
import datetime

class Advertisement(models.Model):
    start_date = models.DateTimeField(default=datetime.datetime.now())
    end_date = models.DateTimeField(default=datetime.datetime.now())
    is_active = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())
    advertiser = models.ForeignKey('Advertiser', models.DO_NOTHING, db_column='Advertiser_id')  # Field name made lowercase.
    board = models.ForeignKey('Board', models.DO_NOTHING, db_column='Board_id')  # Field name made lowercase.
    slot = models.ForeignKey('Slot', models.DO_NOTHING,db_column='Slot_id')
    upload = models.ForeignKey('Upload', models.DO_NOTHING, db_column='Upload_id')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'data_advertisement'


class Advertiser(models.Model):
    name = models.TextField()
    contact = models.BigIntegerField(blank=True, null=True)
    avatar = models.FileField(upload_to='advertiser/')
    company_name = models.TextField()
    company_address = models.TextField()
    city = models.TextField()
    state = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())
    user = models.IntegerField(blank=False , null=False)

    class Meta:
        managed = True
        db_table = 'data_advertiser'


class Board(models.Model):
    lat = models.DecimalField(max_digits=30, decimal_places=15)
    lng = models.DecimalField(max_digits=30, decimal_places=15)
    street = models.TextField()
    area = models.TextField()
    city = models.TextField()
    state = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())
    publisher = models.ForeignKey('Publisher', models.DO_NOTHING, db_column='Publisher_id')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'data_board'


class Cities(models.Model):
    name = models.CharField(max_length=30)
    state_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'data_cities'


class Log(models.Model):
    timestamp = models.DateTimeField(default=datetime.datetime.now())
    created_at = models.DateTimeField(default=datetime.datetime.now())
    advertisement = models.ForeignKey(Advertisement, models.DO_NOTHING, db_column='Advertisement_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_log'


class Payment(models.Model):
    price = models.FloatField()
    service_tax_ratio = models.FloatField()
    service_tax = models.FloatField()
    total_amount = models.FloatField()
    token = models.TextField()
    transaction_type = models.TextField()
    pay_log = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now())
    advertiser = models.ForeignKey(Advertiser, models.DO_NOTHING, db_column='Advertiser_id')  # Field name made lowercase.
    publisher = models.ForeignKey('Publisher', models.DO_NOTHING, db_column='Publisher_id')  # Field name made lowercase.
    slot = models.ForeignKey('Slot', models.DO_NOTHING,db_column='Slot_id')

    class Meta:
        managed = True
        db_table = 'data_payment'


class Publisher(models.Model):
    name = models.TextField()
    contact = models.BigIntegerField(blank=True, null=True)
    avatar = models.FileField(upload_to='publisher/' , null=True)
    company_name = models.TextField()
    company_address = models.TextField()
    city = models.TextField()
    state = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())
    user = models.IntegerField(blank=False , null=False)

    class Meta:
        managed = True
        db_table = 'data_publisher'


class Requestboard(models.Model):
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())
    advertiser = models.ForeignKey(Advertiser, models.DO_NOTHING, db_column='Advertiser_id')  # Field name made lowercase.
    board = models.ForeignKey(Board, models.DO_NOTHING, db_column='Board_id')  # Field name made lowercase.
    publisher = models.ForeignKey(Publisher, models.DO_NOTHING, db_column='Publisher_id')  # Field name made lowercase.
    slot = models.ForeignKey('Slot', models.DO_NOTHING,db_column='Slot_id')
    request_status = models.SmallIntegerField(blank=True, null=True)
    approve_status = models.SmallIntegerField(blank=True, null=True)
    shown = models.SmallIntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'data_requestboard'


class Slot(models.Model):
    from_field = models.TextField(db_column='from_')  # Field renamed because it ended with '_'.
    to = models.TextField()
    total = models.IntegerField()
    slot_price = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())
    board = models.ForeignKey(Board, models.DO_NOTHING, db_column='Board_id')  # Field name made lowercase.
    publisher = models.ForeignKey(Publisher, models.DO_NOTHING, db_column='Publisher_id')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'data_slot'


class States(models.Model):
    name = models.CharField(max_length=30)
    country_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'data_states'



class Upload(models.Model):
    type = models.TextField()
    location = models.FileField(upload_to='advertisement/')
    upload_date = models.DateTimeField(default=datetime.datetime.now())
    current_state = models.IntegerField()
    seconds = models.BigIntegerField()
    upload_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())
    advertiser = models.ForeignKey(Advertiser, models.DO_NOTHING, db_column='Advertiser_id')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'data_upload'



class User(models.Model):   
    username = models.CharField(unique=False, max_length=10)
    password = models.TextField()
    email = models.CharField(unique=False, max_length=30)
    token = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())
    role = models.TextField()

    class Meta:
        managed = True
        db_table = 'data_user'