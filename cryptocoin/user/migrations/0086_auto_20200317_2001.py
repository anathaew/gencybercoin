# Generated by Django 2.1.2 on 2020-03-18 00:01

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0085_auto_20200317_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketitem',
            name='image_file',
            field=models.ImageField(default='../static/img/no-image.jpg', upload_to=user.models.image_upload_market),
        ),
    ]
