# Generated by Django 4.0.1 on 2022-10-06 13:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doctorApp', '0006_alter_appointment_schedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='Doctor',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='Schedule',
        ),
        migrations.AddField(
            model_name='appointment',
            name='Time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]