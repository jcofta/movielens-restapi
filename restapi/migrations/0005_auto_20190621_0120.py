# Generated by Django 2.2.2 on 2019-06-20 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0004_auto_20190621_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='imdb_id',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='tmdb_id',
            field=models.BigIntegerField(null=True),
        ),
    ]
