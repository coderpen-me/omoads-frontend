# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0012_auto_20171002_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_dimensions',
            field=models.CharField(choices=[('0', '50x10'), ('1', '40x10'), ('2', '30x10'), ('3', '20x10'), ('4', '6x3')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_type',
            field=models.CharField(choices=[('gantry', 'Gantry'), ('unipole', 'Unipole'), ('traffic_light', 'Traffic Light Signage')], default='gantry', max_length=100),
        ),
    ]
