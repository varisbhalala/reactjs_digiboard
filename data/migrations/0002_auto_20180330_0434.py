# Generated by Django 2.0.2 on 2018-03-30 04:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 30, 4, 34, 22, 246675)),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 30, 4, 34, 22, 246646)),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 30, 4, 34, 22, 246618)),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 30, 4, 34, 22, 246689)),
        ),
        migrations.AlterField(
            model_name='advertiser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 30, 4, 34, 22, 247336)),
        ),
        migrations.AlterField(
            model_name='advertiser',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 30, 4, 34, 22, 247352)),
        ),
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 30, 4, 34, 22, 247947)),
        ),
        migrations.AlterField(
            model_name='board',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 30, 4, 34, 22, 247964)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 30, 4, 34, 22, 249143)),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 30, 4, 34, 22, 249735)),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 30, 4, 34, 22, 249753)),
        ),
        migrations.AlterField(
            model_name='requestboard',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 30, 4, 34, 22, 250252)),
        ),
        migrations.AlterField(
            model_name='requestboard',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 30, 4, 34, 22, 250273)),
        ),
        migrations.AlterField(
            model_name='slot',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 30, 4, 34, 22, 250938)),
        ),
        migrations.AlterField(
            model_name='slot',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 30, 4, 34, 22, 250954)),
        ),
        migrations.AlterField(
            model_name='upload',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 30, 4, 34, 22, 251855)),
        ),
        migrations.AlterField(
            model_name='upload',
            name='upload_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 30, 4, 34, 22, 251841)),
        ),
        migrations.AlterField(
            model_name='upload',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 30, 4, 34, 22, 251803)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 30, 4, 34, 22, 252430)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 30, 4, 34, 22, 252446)),
        ),
    ]