# Generated by Django 2.1.7 on 2019-04-11 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190411_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='name'),
        ),
    ]
