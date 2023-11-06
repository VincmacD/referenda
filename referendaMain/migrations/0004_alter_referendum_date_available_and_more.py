# Generated by Django 4.2.6 on 2023-11-04 20:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referendaMain', '0003_alter_referendum_date_expired_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referendum',
            name='date_available',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='referendum',
            name='date_published',
            field=models.DateField(default=datetime.datetime(2023, 11, 4, 20, 59, 22, 367690, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vote',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 4, 20, 59, 22, 368692, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='voter',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 4, 20, 59, 22, 366535, tzinfo=datetime.timezone.utc)),
        ),
    ]
