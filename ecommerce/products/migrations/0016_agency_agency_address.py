# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20171107_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency',
            name='agency_address',
            field=models.CharField(max_length=200, default='NONE'),
        ),
    ]
