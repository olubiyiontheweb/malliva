# Generated by Django 3.0.5 on 2021-06-12 13:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0015_auto_20210611_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_id',
            field=models.UUIDField(default=uuid.UUID('42be7311-1ac7-4879-8630-ca91aa7d25a6'), primary_key=True, serialize=False),
        ),
    ]
