# Generated by Django 4.0.4 on 2022-06-24 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usd_price', models.FloatField()),
                ('rub_price', models.FloatField()),
                ('term', models.DateField()),
                ('date', models.DateField()),
                ('expires_today', models.BooleanField()),
                ('expired', models.BooleanField()),
            ],
        ),
    ]
