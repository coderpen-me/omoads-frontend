# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_auto_20181030_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerimage',
            name='image',
            field=models.ImageField(upload_to=products.models.content_file_name, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bannerimage',
            name='normal_image',
            field=models.ImageField(upload_to=products.models.content_file_name, blank=True, null=True),
        ),
    ]
