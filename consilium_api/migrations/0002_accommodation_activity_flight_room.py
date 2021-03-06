# Generated by Django 3.0.7 on 2020-06-13 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consilium_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'room',
                'verbose_name_plural': 'rooms',
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_airport', models.CharField(max_length=20)),
                ('destination_airport', models.CharField(max_length=20)),
                ('arrival_time', models.DateTimeField()),
                ('traveler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flights', to='consilium_api.Traveler')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='consilium_api.Trip')),
            ],
            options={
                'verbose_name': 'flight',
                'verbose_name_plural': 'flights',
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=900)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('traveler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consilium_api.Traveler')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consilium_api.Trip')),
            ],
            options={
                'verbose_name': 'activity',
                'verbose_name_plural': 'activities',
            },
        ),
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('check_in_date', models.DateField()),
                ('checkout_date', models.DateField()),
                ('capacity', models.IntegerField(blank=True, null=True)),
                ('booked', models.BooleanField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='consilium_api.Room')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consilium_api.Trip')),
            ],
        ),
    ]
