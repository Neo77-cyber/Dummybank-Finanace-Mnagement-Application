# Generated by Django 4.1.7 on 2023-03-03 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novabank', '0006_remove_balance_account_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='transfer_pin',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
