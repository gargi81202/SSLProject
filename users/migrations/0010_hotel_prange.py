# Generated by Django 4.0.3 on 2022-11-25 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_hotel_link_movie_link_restaurant_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='prange',
            field=models.TextField(default='2,500-5,000', max_length=20),
        ),
    ]
