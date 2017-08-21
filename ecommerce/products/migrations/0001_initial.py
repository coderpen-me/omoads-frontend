# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('agency_name', models.CharField(max_length=30)),
                ('agency_state', models.CharField(max_length=50)),
                ('agency_city', models.CharField(max_length=50)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('banner_facing', models.CharField(default=b'Facing IMS', max_length=200)),
                ('banner_type', models.CharField(default=b'gantry', max_length=100, choices=[(b'gantry', b'Gantry'), (b'unipole', b'Unipole')])),
                ('banner_lighted', models.CharField(default=b'n', max_length=100, choices=[(b'f', b'Front Lit'), (b'b', b'Back Lit'), (b'n', b'Not Lighted')])),
                ('banner_dimensions', models.CharField(default=b'0', max_length=100, choices=[(b'0', b'50x10'), (b'1', b'40x10'), (b'2', b'30x10'), (b'3', b'20x10')])),
                ('banner_cost', models.DecimalField(max_digits=12, decimal_places=3)),
                ('banner_lattitude', models.DecimalField(max_digits=12, decimal_places=9)),
                ('banner_longitude', models.DecimalField(max_digits=12, decimal_places=9)),
                ('banner_landmark', models.CharField(max_length=200)),
                ('banner_face_side', models.CharField(max_length=10, choices=[(b'Left', b'Left'), (b'Right', b'Right')])),
                ('banner_status', models.CharField(default=b'available', max_length=100, choices=[(b'available', b'Available'), (b'booked', b'Booked')])),
                ('banner_image', models.ImageField(default=b'omoads/Image/banner1.jpg', upload_to=None)),
                ('banner_bookingStatus', models.BooleanField(default=False)),
                ('agency', models.ForeignKey(to='products.Agency')),
            ],
        ),
        migrations.CreateModel(
            name='BookingDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bookingDate', models.DateField()),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('numberDays', models.IntegerField()),
                ('active', models.BooleanField(default=False)),
                ('banner', models.ForeignKey(to='products.Banner')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(null=True, blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('featured', models.BooleanField(default=None)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PricePeriod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('numberDays', models.IntegerField()),
                ('price', models.FloatField()),
                ('banner', models.ForeignKey(to='products.Banner')),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zone_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='banner',
            name='zone',
            field=models.ForeignKey(to='products.Zone'),
        ),
        migrations.AddField(
            model_name='agency',
            name='zones',
            field=models.ManyToManyField(to='products.Zone', null=True, blank=True),
        ),
    ]
