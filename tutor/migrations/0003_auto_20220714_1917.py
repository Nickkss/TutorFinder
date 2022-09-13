# Generated by Django 3.1.1 on 2022-07-14 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0002_auto_20220714_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mon', models.BooleanField(blank=True, default=False, verbose_name='Monday')),
                ('tue', models.BooleanField(blank=True, default=False, verbose_name='Tuesday')),
                ('wed', models.BooleanField(blank=True, default=False, verbose_name='Wednesday')),
                ('thu', models.BooleanField(blank=True, default=False, verbose_name='Thursday')),
                ('fri', models.BooleanField(blank=True, default=False, verbose_name='Friday')),
                ('sat', models.BooleanField(blank=True, default=False, verbose_name='Saturday')),
                ('sun', models.BooleanField(blank=True, default=False, verbose_name='Sunday')),
            ],
            options={
                'verbose_name': 'Days',
                'verbose_name_plural': 'Days',
            },
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='days_avail',
        ),
        migrations.AddField(
            model_name='tutor',
            name='days_avail',
            field=models.ManyToManyField(blank=True, related_name='tutor_days', to='tutor.Days'),
        ),
    ]