# Generated by Django 4.1.7 on 2023-03-03 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novabank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='first_name',
            field=models.CharField(max_length=500),
        ),
    ]