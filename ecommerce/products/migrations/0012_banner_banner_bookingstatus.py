# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_bookingdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='banner_bookingStatus',
            field=models.BooleanField(default=False),
        ),
    ]
