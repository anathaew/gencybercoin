# Generated by Django 2.1.2 on 2019-06-22 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0079_auto_20190310_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='group_number',
            field=models.IntegerField(default=0),
        ),
    ]