# Generated by Django 3.1.1 on 2022-07-14 13:36

from django.db import migrations, models
import tutor.models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='id',
            field=models.CharField(default=tutor.models.get_random_id, editable=False, max_length=100, primary_key=True, serialize=False, unique=True, verbose_name='id'),
        ),
    ]
