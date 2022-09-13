# Generated by Django 3.1.1 on 2022-07-15 13:49

from django.db import migrations, models
import language.models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0013_auto_20220715_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='id',
            field=models.CharField(default=language.models.get_random_id, editable=False, max_length=100, primary_key=True, serialize=False, unique=True, verbose_name='id'),
        ),
    ]
