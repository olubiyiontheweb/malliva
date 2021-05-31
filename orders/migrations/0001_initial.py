# Generated by Django 3.0.5 on 2021-05-28 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paymentGateways', '0002_auto_20210528_1612'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.UUIDField(default=uuid.UUID('bddab1b4-6839-4ec8-a165-c6fcddf5ccd6'), editable=False, primary_key=True, serialize=False)),
                ('PaymentGateway', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='paymentGateways.PaymentGateway')),
                ('seller', models.ForeignKey(default='deleted_user', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]