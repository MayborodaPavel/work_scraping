# Generated by Django 3.0.11 on 2020-12-23 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0002_auto_20201223_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='language',
            name='slug',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
