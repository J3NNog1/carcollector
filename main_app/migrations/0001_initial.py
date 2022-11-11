# Generated by Django 4.1.3 on 2022-11-11 00:28

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
                ('owner', models.CharField(max_length=250)),
                ('year', models.IntegerField()),
                ('make', models.CharField(max_length=100)),
                ('model', models.TextField(max_length=250)),
                ('color', models.CharField(max_length=250)),
                
            ],
        ),
    ]
