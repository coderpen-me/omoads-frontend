# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_agency_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='banner_dimensions',
            field=models.CharField(default='0', choices=[('0', '50x10'), ('1', '40x10'), ('2', '30x10'), ('3', '20x10')], max_length=100),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_facing',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_image',
            field=models.ImageField(default='omoads/Image/banner1.jpg', upload_to=None),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_lighted',
            field=models.CharField(default='n', choices=[('f', 'Front Lit'), ('b', 'Back Lit'), ('n', 'Not Lighted')], max_length=100),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_status',
            field=models.CharField(default='available', choices=[('available', 'Available'), ('booked', 'Booked')], max_length=100),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_type',
            field=models.CharField(default='gantry', choices=[('gantry', 'Gantry'), ('unipole', 'Unipole')], max_length=100),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='products/images/'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='category',
            field=models.CharField(default='size', choices=[('size', 'size'), ('color', 'color'), ('package', 'package')], max_length=120),
        ),
    ]
