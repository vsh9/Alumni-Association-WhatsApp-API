# Generated by Django 5.1 on 2024-08-24 09:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('n_id', models.AutoField(primary_key=True, serialize=False)),
                ('n_type', models.CharField(max_length=25)),
                ('n_content', models.TextField()),
                ('priority', models.CharField(default='Normal', max_length=10)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Events.event')),
            ],
        ),
    ]