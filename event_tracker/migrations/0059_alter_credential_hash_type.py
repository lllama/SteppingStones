# Generated by Django 4.1.7 on 2023-03-20 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_tracker', '0058_alter_credential_hash_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credential',
            name='hash_type',
            field=models.IntegerField(blank=True, choices=[(1000, 'NTLM (1000)'), (2100, 'Domain_Cached_Credentials_2 (2100)'), (3000, 'LM (3000)'), (5500, 'NetNTLMv1 (5500)'), (5600, 'NetNTLMv2 (5600)'), (13100, 'Kerberos_5_TGSREP_RC4 (13100)'), (19600, 'Kerberos_5_TGSREP_AES128 (19600)'), (19700, 'Kerberos_5_TGSREP_AES256 (19700)'), (18200, 'Kerberos_5_ASREP_RC4 (18200)')], help_text='The hashcat module number for the hash', null=True),
        ),
    ]
