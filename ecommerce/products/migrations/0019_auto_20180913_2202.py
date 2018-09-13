# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_favourite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourite',
            name='banner',
            field=models.ForeignKey(to='products.Banner'),
        ),
    ]
