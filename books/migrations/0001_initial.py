# Generated by Django 5.1.1 on 2024-09-07 08:05

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('prince', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
