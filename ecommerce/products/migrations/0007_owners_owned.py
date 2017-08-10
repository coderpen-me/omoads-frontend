# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_owners'),
    ]

    operations = [
        migrations.AddField(
            model_name='owners',
            name='owned',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
