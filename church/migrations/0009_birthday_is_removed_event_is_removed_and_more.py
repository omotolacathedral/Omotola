# Generated by Django 5.0.2 on 2024-03-08 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0008_remove_birthday_is_removed_remove_event_is_removed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='birthday',
            name='is_removed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='is_removed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='office',
            name='is_removed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='is_removed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='testimony',
            name='is_removed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]