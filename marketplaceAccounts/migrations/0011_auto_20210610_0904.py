# Generated by Django 3.0.5 on 2021-06-10 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplaceAccounts', '0010_auto_20210610_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketplaceaccount',
            name='marketplace_id',
            field=models.UUIDField(default='a2fd533c9c6b4e68b0f7f42cf8c5291c', primary_key=True, serialize=False),
        ),
    ]
