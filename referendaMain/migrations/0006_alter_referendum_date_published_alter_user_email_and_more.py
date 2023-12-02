# Generated by Django 4.2.6 on 2023-11-26 22:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referendaMain', '0005_alter_referendum_date_published_alter_vote_timestamp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referendum',
            name='date_published',
            field=models.DateField(default=datetime.datetime(2023, 11, 26, 22, 42, 57, 671273, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='vote',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 26, 22, 42, 57, 672311, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='voter',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 26, 22, 42, 57, 670094, tzinfo=datetime.timezone.utc)),
        ),
    ]