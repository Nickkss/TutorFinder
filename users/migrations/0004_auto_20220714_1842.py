# Generated by Django 3.1.1 on 2022-07-14 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220713_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tutorprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Tutor',
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.SmallIntegerField(choices=[(1, 'Admin'), (2, 'Student')], default=2, help_text='Choose User Role', verbose_name='Role'),
        ),
        migrations.DeleteModel(
            name='StudentProfile',
        ),
        migrations.DeleteModel(
            name='TutorProfile',
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]