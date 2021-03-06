# Generated by Django 4.0.4 on 2022-06-24 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_id', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='expired',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='expires_today',
            field=models.BooleanField(default=False),
        ),
    ]
