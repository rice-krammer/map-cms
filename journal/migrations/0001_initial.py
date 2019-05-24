# Generated by Django 2.2.1 on 2019-05-24 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry', models.CharField(max_length=1000, verbose_name='Entry')),
                ('pub_datetime', models.DateTimeField(verbose_name='Date/Time Published')),
                ('pub_loc_long', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Location Longitude')),
                ('pub_loc_lat', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Location Lattitue')),
            ],
        ),
    ]
