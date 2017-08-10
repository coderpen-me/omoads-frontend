# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20170809_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agency',
            name='agency_id',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='banner_id',
        ),
        migrations.AddField(
            model_name='agency',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True, default=1, auto_created=True, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
