# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170810_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailmarketingsignup',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
