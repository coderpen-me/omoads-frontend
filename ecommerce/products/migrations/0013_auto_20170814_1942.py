# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_banner_banner_bookingstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingdetails',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='banner',
            field=models.ForeignKey(to='products.Banner'),
        ),
    ]
