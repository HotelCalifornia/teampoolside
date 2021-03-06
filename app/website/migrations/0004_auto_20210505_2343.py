# Generated by Django 3.1.6 on 2021-05-06 04:43

from django.db import migrations, models
import django.utils.timezone
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20210505_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date/time of the event'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='event_dates',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.DateTimeField(default=None, null=True), size=None, verbose_name='DEPRECATED DO NOT USE'),
        ),
    ]
