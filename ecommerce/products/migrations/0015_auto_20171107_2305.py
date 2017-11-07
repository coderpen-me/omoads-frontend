# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20171016_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='banner_face_side',
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_dimensions',
            field=models.CharField(default='0', choices=[('0', '50x10'), ('1', '40x10'), ('2', '30x10'), ('3', '20x10'), ('4', '8x4')], max_length=100),
        ),
    ]
