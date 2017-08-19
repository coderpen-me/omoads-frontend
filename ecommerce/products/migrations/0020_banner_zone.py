# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20170819_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='zone',
            field=models.ForeignKey(default=1, to='products.Zone'),
            preserve_default=False,
        ),
    ]
