# Generated by Django 4.0.3 on 2022-03-15 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('JulaneHotel', '0004_rooms_dateofuse'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='custID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='JulaneHotel.customer'),
        ),
    ]
