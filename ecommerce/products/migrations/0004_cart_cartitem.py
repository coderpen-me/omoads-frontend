# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_remove_banner_banner_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('totalPrice', models.FloatField(default=0.0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('price', models.FloatField()),
                ('banner', models.ForeignKey(to='products.Banner')),
                ('cart', models.ForeignKey(to='products.Cart')),
            ],
        ),
    ]
