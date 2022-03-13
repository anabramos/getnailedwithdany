# Generated by Django 3.2 on 2022-03-13 07:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0003_auto_20220311_2135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'ordering': ['timestamp']},
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='appointment_date',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='appointment_time',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='customer',
        ),
        migrations.AddField(
            model_name='appointment',
            name='timestamp',
            field=models.DateField(default=datetime.datetime(2022, 3, 13, 7, 32, 47, 584970), unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
