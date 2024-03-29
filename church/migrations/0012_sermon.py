# Generated by Django 5.0.2 on 2024-03-15 19:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0011_inquiry'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sermon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(blank=True, max_length=250, null=True)),
                ('sermoner_picture', models.TextField()),
                ('sermoner', models.CharField(max_length=250)),
                ('topic', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('is_removed', models.BooleanField(blank=True, default=False, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
