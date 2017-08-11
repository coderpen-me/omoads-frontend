# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20170811_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='banner_dimensions',
            field=models.CharField(default=b'0', max_length=100, choices=[(b'0', b'50x10'), (b'1', b'40x10'), (b'2', b'30x10'), (b'3', b'20x10')]),
        ),
    ]
