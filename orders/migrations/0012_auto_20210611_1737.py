# Generated by Django 3.0.5 on 2021-06-11 16:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20210611_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.UUIDField(default=uuid.UUID('1a305691-1984-432d-810b-574b8c30e851'), editable=False, primary_key=True, serialize=False),
        ),
    ]
