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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('agency_name', models.CharField(max_length=30)),
                ('agency_state', models.CharField(max_length=50)),
                ('agency_city', models.CharField(max_length=50)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('banner_facing', models.CharField(default='Facing IMS', max_length=200)),
                ('banner_type', models.CharField(default='gantry', choices=[('gantry', 'Gantry'), ('unipole', 'Unipole')], max_length=100)),
                ('banner_lighted', models.CharField(default='n', choices=[('f', 'Front Lit'), ('b', 'Back Lit'), ('n', 'Not Lighted')], max_length=100)),
                ('banner_dimensions', models.CharField(default='0', choices=[('0', '50x10'), ('1', '40x10'), ('2', '30x10'), ('3', '20x10')], max_length=100)),
                ('banner_cost', models.DecimalField(decimal_places=3, max_digits=12)),
                ('banner_lattitude', models.DecimalField(decimal_places=9, max_digits=12)),
                ('banner_longitude', models.DecimalField(decimal_places=9, max_digits=12)),
                ('banner_landmark', models.CharField(max_length=200)),
                ('banner_face_side', models.CharField(choices=[('Left', 'Left'), ('Right', 'Right')], max_length=10)),
                ('banner_status', models.CharField(default='available', choices=[('available', 'Available'), ('booked', 'Booked')], max_length=100)),
                ('banner_image', models.ImageField(default='omoads/Image/banner1.jpg', upload_to=None)),
                ('banner_bookingStatus', models.BooleanField(default=False)),
                ('agency', models.ForeignKey(to='products.Agency')),
            ],
        ),
        migrations.CreateModel(
            name='BookingDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('numberDays', models.IntegerField()),
                ('price', models.FloatField()),
                ('banner', models.ForeignKey(to='products.Banner')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(null=True, blank=True)),
                ('price', models.DecimalField(decimal_places=2, default=29.99, max_digits=100)),
                ('sale_price', models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('update_defaults', models.BooleanField(default=False)),
                ('category', models.ManyToManyField(to='products.Category', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='products/images/')),
                ('featured', models.BooleanField(default=False)),
                ('thumbnail', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('category', models.CharField(default='size', choices=[('size', 'size'), ('color', 'color'), ('package', 'package')], max_length=120)),
                ('title', models.CharField(max_length=120)),
                ('price', models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('image', models.ForeignKey(to='products.ProductImage', blank=True, null=True)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
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
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set([('title', 'slug')]),
        ),
    ]
