# Generated by Django 5.0.4 on 2024-04-15 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_rename_belgilar_yhqbelgilar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yhqqoida',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='yhqqoida',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media/belgilar/photos'),
        ),
    ]
