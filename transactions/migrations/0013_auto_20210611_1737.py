# Generated by Django 3.0.5 on 2021-06-11 16:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0012_auto_20210611_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_id',
            field=models.UUIDField(default=uuid.UUID('04723345-a20f-431c-a425-e4a3a6e0163e'), primary_key=True, serialize=False),
        ),
    ]
