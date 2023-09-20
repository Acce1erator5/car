# Generated by Django 4.2.5 on 2023-09-20 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stamp', models.CharField(max_length=255)),
                ('release', models.IntegerField()),
                ('color', models.CharField(max_length=255)),
                ('mileage', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]