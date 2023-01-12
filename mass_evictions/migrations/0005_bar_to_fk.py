# Generated by Django 4.1.5 on 2023-01-12 16:49

from django.db import models, migrations
from django.db.models import Q


def remove_null_attorneys(apps, schema_editor):
    Attorneys = apps.get_model("mass_evictions", "Attorneys")
    Attorneys.objects.filter(Q(bar__isnull=True, name__isnull=True, address__isnull=True)).delete()


def reverse_func(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('mass_evictions', '0004_auto_20230107_0347'),
    ]

    operations = [
        migrations.RunPython(remove_null_attorneys, reverse_func),
        migrations.RemoveField(
            model_name='attorneys',
            name='id',
        ),
        migrations.AlterField(
            model_name='attorneys',
            name='bar',
            field=models.CharField(blank=True, primary_key=True, max_length=50, serialize=False, unique=True),
        ),
    ]
