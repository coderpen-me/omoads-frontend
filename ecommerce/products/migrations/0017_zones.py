# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20170818_2352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zones',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('zone_name', models.CharField(max_length=30)),
                ('agency', models.ForeignKey(to='products.Agency')),
            ],
        ),
    ]
