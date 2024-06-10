# Generated by Django 4.2.1 on 2023-05-23 12:27

from django.db import migrations

from event_tracker.models import HashCatMode
from event_tracker.signals import convert_tgs_to_hashcat_format


def convert_AES256_TGS_to_hashcat(apps, schema_editor):
    Credential = apps.get_model("event_tracker", "Credential")
    for credential in Credential.objects.filter(hash_type=HashCatMode.Kerberos_5_TGSREP_AES256).exclude(hash__isnull=True):
        credential.hash = convert_tgs_to_hashcat_format(credential.hash)
        credential.save()

class Migration(migrations.Migration):

    dependencies = [
        ('event_tracker', '0067_alter_credential_hash_alter_credential_purpose'),
    ]

    operations = [
        migrations.RunPython(convert_AES256_TGS_to_hashcat),
    ]
