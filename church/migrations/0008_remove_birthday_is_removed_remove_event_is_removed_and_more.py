# Generated by Django 5.0.2 on 2024-03-08 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0007_alter_birthday_is_removed_alter_event_is_removed_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='birthday',
            name='is_removed',
        ),
        migrations.RemoveField(
            model_name='event',
            name='is_removed',
        ),
        migrations.RemoveField(
            model_name='office',
            name='is_removed',
        ),
        migrations.RemoveField(
            model_name='team',
            name='is_removed',
        ),
        migrations.RemoveField(
            model_name='testimony',
            name='is_removed',
        ),
    ]
