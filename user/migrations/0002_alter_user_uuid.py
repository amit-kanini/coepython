# Generated by Django 4.1.3 on 2023-02-16 11:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('b5f8baee-86f8-4ad7-a4fe-24e6160a7e06'), primary_key=True, serialize=False),
        ),
    ]
