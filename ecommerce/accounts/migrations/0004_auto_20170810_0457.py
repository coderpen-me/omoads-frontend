# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20170809_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailmarketingsignup',
            name='email',
            field=models.EmailField(max_length=75),
            preserve_default=True,
        ),
    ]
