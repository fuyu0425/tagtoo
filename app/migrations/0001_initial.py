# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-30 03:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertiser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('product_key', models.CharField(max_length=255, null=True, unique=True)),
                ('price', models.IntegerField(null=True)),
                ('store_price', models.IntegerField(null=True)),
                ('Class', models.CharField(max_length=255, null=True)),
                ('update_time', models.DateTimeField(null=True)),
                ('advertiser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Advertiser')),
            ],
        ),
        migrations.CreateModel(
            name='Transcation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255, null=True)),
                ('value', models.IntegerField(null=True)),
                ('currency', models.CharField(max_length=255, null=True)),
                ('num_items', models.CharField(max_length=255, null=True)),
                ('content_ids', models.CharField(max_length=255, null=True)),
                ('purchase_time', models.DateTimeField(null=True)),
                ('click_time_last', models.DateTimeField(null=True)),
                ('click_time_7_days', models.DateTimeField(null=True)),
                ('click_time_30_days', models.DateTimeField(null=True)),
                ('ip', models.CharField(max_length=255, null=True)),
                ('user_agent', models.CharField(max_length=255, null=True)),
                ('advertiser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Advertiser')),
            ],
        ),
    ]
