# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='installationPrice',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='cart',
            name='payment1',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='cart',
            name='payment2',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='cart',
            name='paymentAdvance',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='cart',
            name='tax',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='cart',
            name='totalSumPrice',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='order',
            name='installationPrice',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='order',
            name='payment1',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='order',
            name='payment2',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='order',
            name='paymentAdvance',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='order',
            name='tax',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='order',
            name='totalSumPrice',
            field=models.FloatField(default=0.0),
        ),
    ]
