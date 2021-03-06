# Generated by Django 3.0.7 on 2020-06-23 15:11

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('consilium_api', '0014_auto_20200622_0453'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flight',
            options={'ordering': (django.db.models.expressions.OrderBy(django.db.models.expressions.F('trip__start_date')), django.db.models.expressions.OrderBy(django.db.models.expressions.F('destination_airport'))), 'verbose_name': 'flight', 'verbose_name_plural': 'flights'},
        ),
        migrations.AddField(
            model_name='accommodation',
            name='traveler',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='consilium_api.Traveler'),
            preserve_default=False,
        ),
    ]
