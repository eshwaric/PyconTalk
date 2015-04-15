# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('question', models.CharField(max_length=200)),
                ('up_vote', models.IntegerField(default=0)),
                ('down_vote', models.IntegerField(default=0)),
            ],
        ),
    ]
