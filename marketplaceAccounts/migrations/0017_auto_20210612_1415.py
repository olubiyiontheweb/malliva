# Generated by Django 3.0.5 on 2021-06-12 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplaceAccounts', '0016_auto_20210611_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketplaceaccount',
            name='marketplace_id',
            field=models.UUIDField(default='806b2e1001ae4716a3c7a49ac27c3e60', primary_key=True, serialize=False),
        ),
    ]
