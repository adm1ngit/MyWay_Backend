# Generated by Django 5.0.4 on 2024-04-14 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jarima',
            old_name='name',
            new_name='name2',
        ),
        migrations.RenameField(
            model_name='jarimatoifasi',
            old_name='name',
            new_name='name1',
        ),
    ]