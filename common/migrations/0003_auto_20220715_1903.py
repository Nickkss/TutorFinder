# Generated by Django 3.1.1 on 2022-07-15 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20220715_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='title',
            field=models.CharField(default='Tutor Finder', max_length=500, verbose_name='Site Title'),
        ),
    ]