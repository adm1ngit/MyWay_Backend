# Generated by Django 5.0.4 on 2024-05-09 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evakuator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carModel', models.CharField(max_length=50)),
                ('eventName', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
                ('eventDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('insuranceTerm', models.DateField()),
                ('startDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Mechanic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventName', models.CharField(max_length=250)),
                ('carModel', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=150)),
                ('eventDate', models.DateField()),
            ],
        ),
    ]
