# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-23 19:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0009_auto_20170723_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Banner')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Customer')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='order_info',
            name='pole_id',
        ),
        migrations.RemoveField(
            model_name='order_info',
            name='price',
        ),
        migrations.AddField(
            model_name='order_info',
            name='banner_id',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='search.Banner'),
        ),
        migrations.AddField(
            model_name='order_info',
            name='end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='order_info',
            name='omoid',
            field=models.CharField(default='0', max_length=10000000, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='order_info',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Customer'),
        ),
        migrations.AlterField(
            model_name='order_info',
            name='order_id',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='search.Order'),
        ),
    ]
