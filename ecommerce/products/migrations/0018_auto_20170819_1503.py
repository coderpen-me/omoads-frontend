# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_zones'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='zones',
            name='agency',
        ),
        migrations.DeleteModel(
            name='Zones',
        ),
        migrations.AddField(
            model_name='agency',
            name='zone',
            field=models.ManyToManyField(to='products.Zone'),
        ),
    ]
