# Generated by Django 2.2.2 on 2019-06-20 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0003_auto_20190620_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
