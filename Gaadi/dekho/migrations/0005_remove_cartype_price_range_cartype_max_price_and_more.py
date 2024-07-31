# Generated by Django 5.0.7 on 2024-07-31 03:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dekho", "0004_remove_cartype_mileage_remove_cartype_power_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cartype",
            name="Price_Range",
        ),
        migrations.AddField(
            model_name="cartype",
            name="Max_Price",
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="cartype",
            name="Min_Price",
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
