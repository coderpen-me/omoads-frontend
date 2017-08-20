# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_banner_zone'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='banner_face_side',
            field=models.CharField(max_length=10, choices=[('Left', 'Left'), ('Right', 'Right')], default='Left'),
            preserve_default=False,
        ),
    ]
