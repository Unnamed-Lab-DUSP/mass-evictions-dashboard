# Generated by Django 4.1.5 on 2023-08-05 17:13

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mass_evictions', '0009_parcel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attorneys',
            name='geometry',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='filings',
            name='geometry',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]