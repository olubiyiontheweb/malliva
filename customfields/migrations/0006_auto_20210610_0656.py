# Generated by Django 3.0.5 on 2021-06-10 05:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customFields', '0005_auto_20210610_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customfield',
            name='field_id',
            field=models.UUIDField(default=uuid.UUID('0aba1cf5-14de-48fc-80a9-00331c59998d'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customfielditem',
            name='field_content_id',
            field=models.UUIDField(default=uuid.UUID('6d8eb3e8-06ed-4c32-8c64-6a03dcbabf87'), primary_key=True, serialize=False),
        ),
    ]
