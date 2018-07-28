# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_agency_agency_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='phone_number',
            field=models.CharField(max_length=15, default='0000000000'),
        ),
    ]
