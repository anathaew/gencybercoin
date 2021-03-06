# Generated by Django 2.0.3 on 2018-04-07 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0038_code_school'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='is_superuser',
            new_name='is_admin',
        ),
        migrations.AlterField(
            model_name='achievement',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.School'),
        ),
        migrations.AlterField(
            model_name='code',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.School'),
        ),
        migrations.AlterField(
            model_name='marketitem',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.School'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.School'),
        ),
    ]
