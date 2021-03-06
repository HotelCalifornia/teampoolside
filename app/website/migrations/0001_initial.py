# Generated by Django 3.1.6 on 2021-02-15 03:29

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish_date', models.DateTimeField(verbose_name='date on which to make the event public')),
                ('event_dates', django.contrib.postgres.fields.ArrayField(base_field=models.DateTimeField(null=True), default=datetime.datetime(1970, 1, 1, 6, 0, tzinfo=utc), size=None, verbose_name='dates/times of the event')),
                ('flyer', models.CharField(max_length=256, verbose_name='URL for the flyer image')),
            ],
        ),
    ]
