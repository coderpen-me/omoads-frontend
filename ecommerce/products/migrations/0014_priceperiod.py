# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20170814_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='PricePeriod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('numberDays', models.IntegerField()),
                ('price', models.FloatField()),
                ('banner', models.ForeignKey(to='products.Banner')),
            ],
        ),
    ]
