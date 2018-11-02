# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20180913_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerimage',
            name='normal_image',
            field=models.ImageField(default='boardimages/<built-in function id>.jpg', upload_to=products.models.content_file_name),
        ),
    ]
