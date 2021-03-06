# Generated by Django 2.0.2 on 2018-04-09 09:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20180409_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 9, 24, 53, 746872)),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 9, 24, 53, 746844)),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 9, 24, 53, 746814)),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 9, 24, 53, 746887)),
        ),
        migrations.AlterField(
            model_name='advertiser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 9, 24, 53, 747632)),
        ),
        migrations.AlterField(
            model_name='advertiser',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 9, 24, 53, 747649)),
        ),
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 9, 24, 53, 748176)),
        ),
        migrations.AlterField(
            model_name='board',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 9, 24, 53, 748192)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 9, 24, 53, 749371)),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='avatar',
            field=models.FileField(null=True, upload_to='publisher/'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 9, 24, 53, 750028)),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 9, 24, 53, 750044)),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='user',
            field=models.ForeignKey(db_column='User_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='data.User'),
        ),
        migrations.AlterField(
            model_name='requestboard',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 9, 24, 53, 750485)),
        ),
        migrations.AlterField(
            model_name='requestboard',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 9, 24, 53, 750507)),
        ),
        migrations.AlterField(
            model_name='slot',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 9, 24, 53, 751176)),
        ),
        migrations.AlterField(
            model_name='slot',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 9, 24, 53, 751191)),
        ),
        migrations.AlterField(
            model_name='upload',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 9, 24, 53, 752102)),
        ),
        migrations.AlterField(
            model_name='upload',
            name='upload_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 9, 24, 53, 752088)),
        ),
        migrations.AlterField(
            model_name='upload',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 9, 24, 53, 752052)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 9, 24, 53, 752593)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 9, 24, 53, 752609)),
        ),
    ]
