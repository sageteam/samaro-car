# Generated by Django 2.1.7 on 2019-04-21 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0008_auto_20190421_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='state',
            field=models.PositiveSmallIntegerField(choices=[(1, 'safe'), (2, 'abort')], default=1, verbose_name='state'),
        ),
    ]
