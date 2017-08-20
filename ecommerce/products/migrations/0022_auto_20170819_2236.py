# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_banner_banner_face_side'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='zones',
            field=models.ManyToManyField(to='products.Zone', null=True),
        ),
    ]
