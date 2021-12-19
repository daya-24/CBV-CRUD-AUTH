# Generated by Django 4.0 on 2021-12-19 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=32)),
                ('model_name', models.CharField(max_length=32)),
                ('ram', models.IntegerField()),
                ('rom', models.IntegerField()),
                ('processor', models.CharField(max_length=32)),
                ('price', models.FloatField()),
                ('weight', models.FloatField()),
            ],
        ),
    ]
