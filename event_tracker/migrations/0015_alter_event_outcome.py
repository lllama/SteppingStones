# Generated by Django 3.2.8 on 2021-11-09 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_tracker', '0014_event_outcome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='outcome',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
