# Generated by Django 2.0.5 on 2018-05-15 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IPAddress',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('ip_address', models.GenericIPAddressField()),
                ('description', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'swappable': 'DJANGO_IPAM_IPADDRESS_MODEL',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subnet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'swappable': 'DJANGO_IPAM_SUBNET_MODEL',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='ipaddress',
            name='subnet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.DJANGO_IPAM_SUBNET_MODEL),
        ),
    ]