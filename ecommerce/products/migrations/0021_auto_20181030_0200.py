# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_bannerimage_normal_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerimage',
            name='image',
            field=models.ImageField(null=True, upload_to=products.models.content_file_name),
        ),
    ]
