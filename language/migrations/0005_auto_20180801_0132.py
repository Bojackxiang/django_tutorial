# Generated by Django 2.0.7 on 2018-08-01 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0004_auto_20180801_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='description',
            field=models.TextField(default='', max_length=200),
        ),
    ]
