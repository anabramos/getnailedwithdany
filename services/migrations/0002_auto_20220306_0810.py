# Generated by Django 3.2 on 2022-03-06 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Services',
            new_name='Service',
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['service_title']},
        ),
    ]
