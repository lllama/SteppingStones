# Generated by Django 4.1.3 on 2022-11-22 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_tracker', '0047_event_tags_alter_event_detected_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attacksubtechnique',
            name='detection_advice',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='attacktechnique',
            name='detection_advice',
            field=models.TextField(null=True),
        ),
    ]
