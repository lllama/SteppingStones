# Generated by Django 4.1.5 on 2023-02-02 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_tracker', '0053_alter_importedevent_mitre_tactic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='importedevent',
            name='additional_data',
            field=models.TextField(blank=True, null=True),
        ),
    ]
