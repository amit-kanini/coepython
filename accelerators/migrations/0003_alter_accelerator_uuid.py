# Generated by Django 4.1.3 on 2023-02-16 11:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accelerators', '0002_alter_accelerator_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accelerator',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('311a19a7-b762-4405-8390-7423e43150d2'), primary_key=True, serialize=False),
        ),
    ]
