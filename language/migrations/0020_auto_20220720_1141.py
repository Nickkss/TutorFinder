# Generated by Django 3.1.1 on 2022-07-20 06:11

from django.db import migrations, models
import language.models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0019_auto_20220717_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='id',
            field=models.CharField(default=language.models.get_random_id, editable=False, max_length=100, primary_key=True, serialize=False, unique=True, verbose_name='id'),
        ),
    ]
