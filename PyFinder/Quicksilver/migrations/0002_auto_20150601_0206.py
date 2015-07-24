# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quicksilver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abilityset',
            name='id',
            field=models.CharField(primary_key=True, serialize=False, editable=False, max_length=17, unique=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='character',
            name='id',
            field=models.CharField(primary_key=True, serialize=False, editable=False, max_length=17, unique=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='class',
            name='id',
            field=models.CharField(primary_key=True, serialize=False, editable=False, max_length=17, unique=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classstats',
            name='id',
            field=models.CharField(primary_key=True, serialize=False, editable=False, max_length=17, unique=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='equipment',
            name='id',
            field=models.CharField(primary_key=True, serialize=False, editable=False, max_length=17, unique=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='feat',
            name='id',
            field=models.CharField(primary_key=True, serialize=False, editable=False, max_length=17, unique=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='knowledgeset',
            name='id',
            field=models.CharField(primary_key=True, serialize=False, editable=False, max_length=17, unique=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='race',
            name='id',
            field=models.CharField(primary_key=True, serialize=False, editable=False, max_length=17, unique=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='skillset',
            name='id',
            field=models.CharField(primary_key=True, serialize=False, editable=False, max_length=17, unique=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='speedstats',
            name='id',
            field=models.CharField(primary_key=True, serialize=False, editable=False, max_length=17, unique=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='spellsperday',
            name='id',
            field=models.CharField(primary_key=True, serialize=False, editable=False, max_length=17, unique=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visionstats',
            name='id',
            field=models.CharField(primary_key=True, serialize=False, editable=False, max_length=17, unique=True, db_index=True),
            preserve_default=True,
        ),
    ]
