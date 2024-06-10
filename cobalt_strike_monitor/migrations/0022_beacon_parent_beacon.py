# Generated by Django 4.0.5 on 2022-07-11 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cobalt_strike_monitor', '0021_download'),
    ]

    operations = [
        migrations.AddField(
            model_name='beacon',
            name='parent_beacon',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cobalt_strike_monitor.beacon'),
        ),
    ]
