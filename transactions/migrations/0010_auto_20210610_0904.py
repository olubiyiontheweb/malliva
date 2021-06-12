# Generated by Django 3.0.5 on 2021-06-10 08:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0009_auto_20210610_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_id',
            field=models.UUIDField(default=uuid.UUID('f823dd7a-3ea4-46e4-bdd6-6f79b2867ea4'), primary_key=True, serialize=False),
        ),
    ]
