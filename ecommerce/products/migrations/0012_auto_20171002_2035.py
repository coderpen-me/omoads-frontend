# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20171002_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='banner_type',
            field=models.CharField(default=b'gantry', max_length=100, choices=[(b'gantry', b'Gantry'), (b'unipole', b'Unipole'), (b'traffic_light', b'Traffic Light Signage')]),
        ),
    ]
