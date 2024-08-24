# Generated by Django 5.1 on 2024-08-24 09:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Alumni', '0002_rename_address_alumni_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=200)),
                ('event_date_time', models.DateTimeField()),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('event_type', models.CharField(max_length=50)),
                ('registration_deadline', models.DateTimeField()),
                ('rsvp_deadline', models.DateField()),
                ('rsvp_status', models.BooleanField(default=False)),
                ('speaker_details', models.TextField(blank=True, null=True)),
                ('event_status', models.CharField(max_length=20)),
                ('feedback_available', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='EventAlumni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumni_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alumni.alumni')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Events.event')),
            ],
        ),
    ]