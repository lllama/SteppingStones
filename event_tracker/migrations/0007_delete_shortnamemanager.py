# Generated by Django 3.2.8 on 2021-10-20 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_tracker', '0006_alter_attacktactic_shortname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ShortNameManager',
        ),
    ]
