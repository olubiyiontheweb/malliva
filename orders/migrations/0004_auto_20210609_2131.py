# Generated by Django 3.0.5 on 2021-06-09 20:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210609_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.UUIDField(default=uuid.UUID('04de8b1d-dde2-4d4c-9739-03e3082058d9'), editable=False, primary_key=True, serialize=False),
        ),
    ]
