# Generated by Django 4.2 on 2023-04-30 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novabank', '0015_rename_accoun_total_portfolio_account_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='phone',
            new_name='phone_number',
        ),
    ]
