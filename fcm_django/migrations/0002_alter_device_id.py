# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcm_django', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fcmdevice',
            name='device_id',
            field=models.CharField(blank=True, db_index=True, help_text='Unique device identifier', max_length=150, null=True, verbose_name='Device ID'),
        ),
    ]
