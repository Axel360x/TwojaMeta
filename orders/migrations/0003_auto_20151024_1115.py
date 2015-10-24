# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20151024_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='procuct_description',
        ),
        migrations.AddField(
            model_name='product',
            name='product_description',
            field=models.CharField(default='ererger', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=100),
        ),
    ]
