# Generated by Django 2.1.11 on 2020-01-08 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('civic_pulse', '0007_increase_length_add_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency',
            name='aliases',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
