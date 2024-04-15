# Generated by Django 5.0.4 on 2024-04-15 11:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True)),
                ('price_main', models.CharField(max_length=50)),
                ('price_sale30', models.CharField(max_length=50)),
                ('price_sale50', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Belgilar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='JarimaToifasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BelgiQoidalari',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('BelgilarBolimi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.belgilar')),
            ],
        ),
        migrations.CreateModel(
            name='Jarima',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name2', models.TextField()),
                ('band', models.ManyToManyField(to='backend.band')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.jarimatoifasi')),
            ],
        ),
        migrations.CreateModel(
            name='Qoida',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('img', models.ImageField(upload_to='media/belgilar/photos')),
                ('BelgiQoidalari', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.belgiqoidalari')),
            ],
        ),
    ]
