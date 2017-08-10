# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20170810_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='banner_dimensions',
            field=models.CharField(default='50x10', max_length=100, choices=[('0', '50x10'), ('1', '40x10'), ('2', '30x10'), ('3', '20x10')]),
        ),
    ]
