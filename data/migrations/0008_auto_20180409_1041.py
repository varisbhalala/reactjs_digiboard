# Generated by Django 2.0.2 on 2018-04-09 10:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_auto_20180409_1038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publisher',
            old_name='User_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 41, 5, 892319)),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 41, 5, 892291)),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 41, 5, 892262)),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 41, 5, 892333)),
        ),
        migrations.AlterField(
            model_name='advertiser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 41, 5, 893072)),
        ),
        migrations.AlterField(
            model_name='advertiser',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 41, 5, 893088)),
        ),
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 41, 5, 893677)),
        ),
        migrations.AlterField(
            model_name='board',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 41, 5, 893694)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 41, 5, 894906)),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 41, 5, 895573)),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 41, 5, 895589)),
        ),
        migrations.AlterField(
            model_name='requestboard',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 41, 5, 895979)),
        ),
        migrations.AlterField(
            model_name='requestboard',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 41, 5, 896001)),
        ),
        migrations.AlterField(
            model_name='slot',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 41, 5, 896671)),
        ),
        migrations.AlterField(
            model_name='slot',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 41, 5, 896686)),
        ),
        migrations.AlterField(
            model_name='upload',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 41, 5, 897598)),
        ),
        migrations.AlterField(
            model_name='upload',
            name='upload_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 41, 5, 897582)),
        ),
        migrations.AlterField(
            model_name='upload',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 41, 5, 897545)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 41, 5, 898091)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 41, 5, 898107)),
        ),
    ]