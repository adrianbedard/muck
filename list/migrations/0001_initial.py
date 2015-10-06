# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrintObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.CharField(max_length=50)),
                ('createDate', models.DateTimeField(verbose_name=b'date published')),
                ('ownerName', models.CharField(max_length=200)),
                ('priority', models.IntegerField(default=10)),
                ('dropOffLocation', models.CharField(max_length=200)),
                ('uniqueID', models.IntegerField(default=0)),
            ],
        ),
    ]
