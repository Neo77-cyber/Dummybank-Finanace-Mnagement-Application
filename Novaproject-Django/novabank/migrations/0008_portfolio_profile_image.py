# Generated by Django 4.1.7 on 2023-03-04 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novabank', '0007_transactions_transfer_pin'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
