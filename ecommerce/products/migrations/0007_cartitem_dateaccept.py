# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20170904_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='dateAccept',
            field=models.BooleanField(default=True),
        ),
    ]
