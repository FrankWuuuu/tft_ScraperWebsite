# Generated by Django 4.1.4 on 2023-01-03 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_carryandcomps_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carryandcomps',
            name='body',
        ),
        migrations.AddField(
            model_name='carryandcomps',
            name='name',
            field=models.CharField(default='yes', max_length=200),
            preserve_default=False,
        ),
    ]
