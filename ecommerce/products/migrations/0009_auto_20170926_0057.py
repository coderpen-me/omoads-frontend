# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_payments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='order',
            field=models.OneToOneField(blank=True, to='products.Order', null=True),
        ),
    ]
