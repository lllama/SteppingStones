# Generated by Django 3.2.8 on 2021-10-20 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event_tracker', '0007_delete_shortnamemanager'),
    ]

    operations = [
        migrations.AddField(
            model_name='attacksubtechnique',
            name='parent_technique',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='event_tracker.attacktechnique'),
            preserve_default=False,
        ),
    ]
