# Generated by Django 2.2.9 on 2020-02-14 19:36

from django.db import migrations
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0034_fix_ipaddress_status_dhcp'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aggregate',
            options={'ordering': ('prefix', 'pk')},
        ),
        migrations.AlterModelOptions(
            name='ipaddress',
            options={'ordering': ('address', 'pk'), 'verbose_name': 'IP address', 'verbose_name_plural': 'IP addresses'},
        ),
        migrations.AlterModelOptions(
            name='prefix',
            options={'ordering': (django.db.models.expressions.OrderBy(django.db.models.expressions.F('vrf'), nulls_first=True), 'prefix', 'pk'), 'verbose_name_plural': 'prefixes'},
        ),
        migrations.RemoveField(
            model_name='aggregate',
            name='family',
        ),
        migrations.RemoveField(
            model_name='ipaddress',
            name='family',
        ),
        migrations.RemoveField(
            model_name='prefix',
            name='family',
        ),
    ]
