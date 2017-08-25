# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20170824_0316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='banner_image',
        ),
    ]
