# Generated by Django 3.0.5 on 2021-06-21 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import listings.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('description', models.CharField(default='', max_length=500)),
                ('visible', models.BooleanField(default=True, help_text='Is this listing visible to the public?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(default='1', on_delete=django.db.models.deletion.SET_DEFAULT, to='categories.Category')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posted_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ListingImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=listings.models.listing_directory_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listing_images', to='listings.Listing')),
            ],
        ),
    ]
