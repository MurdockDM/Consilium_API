# Generated by Django 3.0.7 on 2020-06-17 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consilium_api', '0006_auto_20200616_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='traveler',
            name='possible_friend',
            field=models.ManyToManyField(through='consilium_api.Friend', to='consilium_api.Traveler'),
        ),
    ]
