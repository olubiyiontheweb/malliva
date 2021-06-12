# Generated by Django 3.0.5 on 2021-06-10 08:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customFields', '0008_auto_20210610_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customfield',
            name='field_id',
            field=models.UUIDField(default=uuid.UUID('4cddf8f9-0ab3-4fd0-954e-0d9052c4a0a1'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customfielditem',
            name='field_content_id',
            field=models.UUIDField(default=uuid.UUID('a0a0bd28-3a64-4fab-a5f4-ec1e007d2a2c'), primary_key=True, serialize=False),
        ),
    ]
