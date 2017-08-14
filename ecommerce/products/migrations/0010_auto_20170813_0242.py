# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20170811_1243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='agency_id',
            new_name='agency',
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_dimensions',
            field=models.CharField(max_length=100, default='0', choices=[('0', '50x10'), ('1', '40x10'), ('2', '30x10'), ('3', '20x10')]),
        ),
    ]
