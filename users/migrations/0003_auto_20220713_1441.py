# Generated by Django 3.1.1 on 2022-07-13 09:11

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220713_1139'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-last_login'], 'verbose_name': 'User', 'verbose_name_plural': 'All Users'},
        ),
        migrations.AddField(
            model_name='tutorprofile',
            name='days_avail',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'SUN'), (2, 'MON'), (3, 'TUE'), (4, 'WED'), (5, 'THU'), (6, 'FRI'), (7, 'SAT')], max_length=13, null=True, verbose_name='Days Available'),
        ),
    ]
