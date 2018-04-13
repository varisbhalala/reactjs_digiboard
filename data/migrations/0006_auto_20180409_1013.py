# Generated by Django 2.0.2 on 2018-04-09 10:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20180409_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 13, 6, 223312)),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 13, 6, 223284)),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 13, 6, 223253)),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 13, 6, 223327)),
        ),
        migrations.AlterField(
            model_name='advertiser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 13, 6, 224074)),
        ),
        migrations.AlterField(
            model_name='advertiser',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 13, 6, 224091)),
        ),
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 13, 6, 224648)),
        ),
        migrations.AlterField(
            model_name='board',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 13, 6, 224665)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 13, 6, 225837)),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 13, 6, 226500)),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 13, 6, 226517)),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='user',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='requestboard',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 13, 6, 226906)),
        ),
        migrations.AlterField(
            model_name='requestboard',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 13, 6, 226929)),
        ),
        migrations.AlterField(
            model_name='slot',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 13, 6, 227599)),
        ),
        migrations.AlterField(
            model_name='slot',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 13, 6, 227615)),
        ),
        migrations.AlterField(
            model_name='upload',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 13, 6, 228530)),
        ),
        migrations.AlterField(
            model_name='upload',
            name='upload_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 13, 6, 228514)),
        ),
        migrations.AlterField(
            model_name='upload',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 13, 6, 228476)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 13, 6, 229015)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 13, 6, 229032)),
        ),
    ]