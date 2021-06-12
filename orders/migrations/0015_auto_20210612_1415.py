# Generated by Django 3.0.5 on 2021-06-12 13:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20210611_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.UUIDField(default=uuid.UUID('dfbe5036-d265-40ba-8d34-ca2401ec761a'), editable=False, primary_key=True, serialize=False),
        ),
    ]
