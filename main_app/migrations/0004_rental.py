# Generated by Django 4.1.3 on 2022-11-14 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_maintenance_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver', models.CharField(max_length=250)),
                ('start_mileage', models.CharField(max_length=1000000)),
                ('end_mileage', models.CharField(max_length=1000000)),
                ('days_rented', models.CharField(max_length=10000)),
                ('paid_by', models.CharField(max_length=250)),
            ],
        ),
    ]