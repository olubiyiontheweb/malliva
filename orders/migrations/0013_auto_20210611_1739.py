# Generated by Django 3.0.5 on 2021-06-11 16:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20210611_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.UUIDField(default=uuid.UUID('72466fbf-8b3c-4356-a07b-f71d7aed4e2f'), editable=False, primary_key=True, serialize=False),
        ),
    ]
