# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerImage',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('image', models.ImageField(default='boardimages/<built-in function id>.jpg', upload_to=products.models.content_file_name)),
            ],
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_dimensions',
            field=models.CharField(choices=[('0', '50x10'), ('1', '40x10'), ('2', '30x10'), ('3', '20x10')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_face_side',
            field=models.CharField(choices=[('Left', 'Left'), ('Right', 'Right')], max_length=10),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_facing',
            field=models.CharField(default='Facing IMS', max_length=200),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_image',
            field=models.ImageField(default='omoads/Image/banner1.jpg', upload_to=None),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_lighted',
            field=models.CharField(choices=[('f', 'Front Lit'), ('b', 'Back Lit'), ('n', 'Not Lighted')], default='n', max_length=100),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_status',
            field=models.CharField(choices=[('available', 'Available'), ('booked', 'Booked')], default='available', max_length=100),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_type',
            field=models.CharField(choices=[('gantry', 'Gantry'), ('unipole', 'Unipole')], default='gantry', max_length=100),
        ),
        migrations.AddField(
            model_name='bannerimage',
            name='banner',
            field=models.OneToOneField(to='products.Banner'),
        ),
    ]
