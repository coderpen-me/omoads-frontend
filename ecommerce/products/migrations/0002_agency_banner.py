# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('agency_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('agency_name', models.CharField(max_length=30)),
                ('agency_state', models.CharField(max_length=50)),
                ('agency_city', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('banner_id', models.CharField(unique=True, max_length=200)),
                ('banner_facing', models.CharField(default=b'0', max_length=200)),
                ('banner_type', models.CharField(default=b'gantry', max_length=100, choices=[(b'gantry', b'Gantry'), (b'unipole', b'Unipole')])),
                ('banner_lighted', models.CharField(default=b'n', max_length=100, choices=[(b'f', b'Front Lit'), (b'b', b'Back Lit'), (b'n', b'Not Lighted')])),
                ('banner_dimensions', models.CharField(default=b'0', max_length=100, choices=[(b'0', b'50x10'), (b'1', b'40x10'), (b'2', b'30x10'), (b'3', b'20x10')])),
                ('banner_cost', models.DecimalField(max_digits=12, decimal_places=3)),
                ('banner_lattitude', models.DecimalField(max_digits=12, decimal_places=9)),
                ('banner_longitude', models.DecimalField(max_digits=12, decimal_places=9)),
                ('banner_landmark', models.CharField(max_length=200)),
                ('banner_status', models.CharField(default=b'available', max_length=100, choices=[(b'available', b'Available'), (b'booked', b'Booked')])),
                ('banner_image', models.ImageField(default=b'omoads/Image/banner1.jpg', upload_to=None)),
                ('agency_id', models.ForeignKey(to='products.Agency')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
