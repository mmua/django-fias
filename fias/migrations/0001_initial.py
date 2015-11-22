# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddrObj',
            fields=[
                ('ifnsfl', models.PositiveIntegerField(null=True, blank=True)),
                ('terrifnsfl', models.PositiveIntegerField(null=True, blank=True)),
                ('ifnsul', models.PositiveIntegerField(null=True, blank=True)),
                ('terrifnsul', models.PositiveIntegerField(null=True, blank=True)),
                ('okato', models.BigIntegerField(null=True, blank=True)),
                ('oktmo', models.BigIntegerField(null=True, blank=True)),
                ('postalcode', models.PositiveIntegerField(null=True, blank=True)),
                ('updatedate', models.DateField()),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('normdoc', models.UUIDField(null=True, blank=True)),
                ('aoguid', models.UUIDField(serialize=False, primary_key=True)),
                ('parentguid', models.UUIDField(db_index=True, null=True, blank=True)),
                ('aoid', models.UUIDField(unique=True, db_index=True)),
                ('previd', models.UUIDField(null=True, blank=True)),
                ('nextid', models.UUIDField(null=True, blank=True)),
                ('formalname', models.CharField(max_length=120, db_index=True)),
                ('offname', models.CharField(max_length=120, null=True, blank=True)),
                ('shortname', models.CharField(max_length=10, db_index=True)),
                ('aolevel', models.PositiveSmallIntegerField(db_index=True)),
                ('regioncode', models.CharField(max_length=2)),
                ('autocode', models.CharField(max_length=1)),
                ('areacode', models.CharField(max_length=3)),
                ('citycode', models.CharField(max_length=3)),
                ('ctarcode', models.CharField(max_length=3)),
                ('placecode', models.CharField(max_length=3)),
                ('streetcode', models.CharField(max_length=4)),
                ('extrcode', models.CharField(max_length=4)),
                ('sextcode', models.CharField(max_length=3)),
                ('code', models.CharField(max_length=17, null=True, blank=True)),
                ('plaincode', models.CharField(max_length=15, null=True, blank=True)),
                ('actstatus', models.BooleanField(default=False)),
                ('centstatus', models.PositiveSmallIntegerField()),
                ('operstatus', models.PositiveSmallIntegerField()),
                ('currstatus', models.PositiveSmallIntegerField()),
                ('livestatus', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['aolevel', 'formalname'],
            },
        ),
        migrations.CreateModel(
            name='AddrObjIndex',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aoguid', models.UUIDField()),
                ('aolevel', models.PositiveSmallIntegerField()),
                ('scname', models.TextField()),
                ('fullname', models.TextField()),
                ('item_weight', models.PositiveSmallIntegerField(default=64)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('ifnsfl', models.PositiveIntegerField(null=True, blank=True)),
                ('terrifnsfl', models.PositiveIntegerField(null=True, blank=True)),
                ('ifnsul', models.PositiveIntegerField(null=True, blank=True)),
                ('terrifnsul', models.PositiveIntegerField(null=True, blank=True)),
                ('okato', models.BigIntegerField(null=True, blank=True)),
                ('oktmo', models.BigIntegerField(null=True, blank=True)),
                ('postalcode', models.PositiveIntegerField(null=True, blank=True)),
                ('updatedate', models.DateField()),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('normdoc', models.UUIDField(null=True, blank=True)),
                ('housenum', models.CharField(max_length=20, null=True, blank=True)),
                ('eststatus', models.PositiveSmallIntegerField(default=0)),
                ('buildnum', models.CharField(max_length=10, null=True, blank=True)),
                ('strucnum', models.CharField(max_length=10, null=True, blank=True)),
                ('strstatus', models.PositiveSmallIntegerField()),
                ('houseguid', models.UUIDField(serialize=False, primary_key=True)),
                ('houseid', models.UUIDField()),
                ('statstatus', models.PositiveSmallIntegerField()),
                ('counter', models.IntegerField()),
                ('aoguid', models.ForeignKey(to='fias.AddrObj')),
            ],
        ),
        migrations.CreateModel(
            name='HouseInt',
            fields=[
                ('ifnsfl', models.PositiveIntegerField(null=True, blank=True)),
                ('terrifnsfl', models.PositiveIntegerField(null=True, blank=True)),
                ('ifnsul', models.PositiveIntegerField(null=True, blank=True)),
                ('terrifnsul', models.PositiveIntegerField(null=True, blank=True)),
                ('okato', models.BigIntegerField(null=True, blank=True)),
                ('oktmo', models.BigIntegerField(null=True, blank=True)),
                ('postalcode', models.PositiveIntegerField(null=True, blank=True)),
                ('updatedate', models.DateField()),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('normdoc', models.UUIDField(null=True, blank=True)),
                ('houseintid', models.UUIDField()),
                ('intguid', models.UUIDField(serialize=False, primary_key=True)),
                ('intstart', models.PositiveIntegerField()),
                ('intend', models.PositiveIntegerField()),
                ('intstatus', models.PositiveIntegerField()),
                ('counter', models.PositiveIntegerField()),
                ('aoguid', models.ForeignKey(to='fias.AddrObj')),
            ],
        ),
        migrations.CreateModel(
            name='LandMark',
            fields=[
                ('ifnsfl', models.PositiveIntegerField(null=True, blank=True)),
                ('terrifnsfl', models.PositiveIntegerField(null=True, blank=True)),
                ('ifnsul', models.PositiveIntegerField(null=True, blank=True)),
                ('terrifnsul', models.PositiveIntegerField(null=True, blank=True)),
                ('okato', models.BigIntegerField(null=True, blank=True)),
                ('oktmo', models.BigIntegerField(null=True, blank=True)),
                ('postalcode', models.PositiveIntegerField(null=True, blank=True)),
                ('updatedate', models.DateField()),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('normdoc', models.UUIDField(null=True, blank=True)),
                ('landid', models.UUIDField()),
                ('landguid', models.UUIDField(serialize=False, primary_key=True)),
                ('location', models.TextField()),
                ('aoguid', models.ForeignKey(to='fias.AddrObj')),
            ],
        ),
        migrations.CreateModel(
            name='NormDoc',
            fields=[
                ('normdocid', models.UUIDField(serialize=False, primary_key=True)),
                ('docname', models.TextField(blank=True)),
                ('docdate', models.DateField(null=True, blank=True)),
                ('docnum', models.CharField(max_length=20, null=True, blank=True)),
                ('doctype', models.PositiveIntegerField()),
                ('docimgid', models.PositiveIntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocrBase',
            fields=[
                ('level', models.PositiveSmallIntegerField(verbose_name='level')),
                ('scname', models.CharField(default=' ', max_length=10)),
                ('socrname', models.CharField(default=' ', max_length=50)),
                ('kod_t_st', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('item_weight', models.PositiveSmallIntegerField(default=64)),
            ],
            options={
                'ordering': ['level', 'scname'],
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('table', models.CharField(max_length=15, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('ver', models.IntegerField(serialize=False, primary_key=True)),
                ('date', models.DateField(db_index=True, null=True, blank=True)),
                ('dumpdate', models.DateField(db_index=True)),
                ('complete_xml_url', models.CharField(max_length=255)),
                ('delta_xml_url', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='status',
            name='ver',
            field=models.ForeignKey(to='fias.Version'),
        ),
        migrations.AlterIndexTogether(
            name='socrbase',
            index_together=set([('level', 'scname')]),
        ),
        migrations.AlterIndexTogether(
            name='addrobj',
            index_together=set([('aolevel', 'shortname'), ('shortname', 'formalname')]),
        ),
    ]