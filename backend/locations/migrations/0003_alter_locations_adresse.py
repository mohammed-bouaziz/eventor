# Generated by Django 5.0.2 on 2024-02-20 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_locations_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='adresse',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
