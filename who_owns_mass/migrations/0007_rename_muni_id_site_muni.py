# Generated by Django 4.1.5 on 2024-10-31 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('who_owns_mass', '0006_owner_company_alter_owner_metacorp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='muni_id',
            new_name='muni',
        ),
    ]
