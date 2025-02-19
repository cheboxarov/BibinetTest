# Generated by Django 5.0.7 on 2024-07-13 05:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('producer_country_name', models.CharField(max_length=100)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_visible', models.BooleanField(default=True)),
                ('mark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parts.mark')),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('json_data', models.JSONField(default=dict)),
                ('is_visible', models.BooleanField(default=True)),
                ('mark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parts.mark')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parts.model')),
            ],
        ),
    ]
