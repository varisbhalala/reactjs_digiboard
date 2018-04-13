# Generated by Django 2.0.2 on 2018-04-09 10:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_auto_20180409_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 43, 21, 590269)),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 43, 21, 590241)),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 43, 21, 590212)),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 43, 21, 590283)),
        ),
        migrations.AlterField(
            model_name='advertiser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 43, 21, 591078)),
        ),
        migrations.AlterField(
            model_name='advertiser',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 43, 21, 591095)),
        ),
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 43, 21, 591629)),
        ),
        migrations.AlterField(
            model_name='board',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 43, 21, 591645)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 43, 21, 592802)),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 43, 21, 593455)),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 43, 21, 593471)),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='user',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='requestboard',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 43, 21, 593856)),
        ),
        migrations.AlterField(
            model_name='requestboard',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 43, 21, 593879)),
        ),
        migrations.AlterField(
            model_name='slot',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 43, 21, 594542)),
        ),
        migrations.AlterField(
            model_name='slot',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 43, 21, 594558)),
        ),
        migrations.AlterField(
            model_name='upload',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 43, 21, 595488)),
        ),
        migrations.AlterField(
            model_name='upload',
            name='upload_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 43, 21, 595471)),
        ),
        migrations.AlterField(
            model_name='upload',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 43, 21, 595435)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 43, 21, 595976)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 10, 43, 21, 595992)),
        ),
    ]