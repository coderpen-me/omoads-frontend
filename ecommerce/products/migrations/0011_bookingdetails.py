# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20170813_0242'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('bookingDate', models.DateField()),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('numberDays', models.IntegerField()),
                ('banner', models.OneToOneField(to='products.Banner')),
            ],
        ),
    ]
