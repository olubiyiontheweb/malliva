# Generated by Django 3.2 on 2021-06-22 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paymentGateways', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('PaymentGateway', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='paymentGateways.paymentgateway')),
                ('seller', models.ForeignKey(default='deleted_user', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]