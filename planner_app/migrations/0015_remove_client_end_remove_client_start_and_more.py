# Generated by Django 4.0.6 on 2022-07-18 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner_app', '0014_rename_name_client_title_client_end_client_start'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='end',
        ),
        migrations.RemoveField(
            model_name='client',
            name='start',
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
