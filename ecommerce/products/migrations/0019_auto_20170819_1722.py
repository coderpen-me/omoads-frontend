# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20170819_1503'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agency',
            old_name='zone',
            new_name='zones',
        ),
    ]
