# Generated by Django 4.0.6 on 2022-07-11 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner_app', '0007_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.DateField(),
        ),
    ]
