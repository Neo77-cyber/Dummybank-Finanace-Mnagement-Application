# Generated by Django 4.2 on 2023-04-30 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novabank', '0014_portfolio_accoun_total_portfolio_pin_delete_balance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='accoun_total',
            new_name='account_total',
        ),
    ]
