# Generated by Django 4.2.7 on 2023-12-07 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_tracker', '0078_remove_context_bh_sync_done_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credential',
            name='hash_type',
            field=models.IntegerField(blank=True, choices=[(-1, 'Unlisted (-1)'), (111, 'LDAP_SSHA1 (111)'), (1000, 'NTLM (1000)'), (2100, 'Domain_Cached_Credentials_2 (2100)'), (3000, 'LM (3000)'), (5500, 'NetNTLMv1 (5500)'), (5600, 'NetNTLMv2 (5600)'), (13100, 'Kerberos_5_TGSREP_RC4 (13100)'), (19600, 'Kerberos_5_TGSREP_AES128 (19600)'), (19700, 'Kerberos_5_TGSREP_AES256 (19700)'), (18200, 'Kerberos_5_ASREP_RC4 (18200)')], help_text='The hashcat module number for the hash', null=True),
        ),
    ]
