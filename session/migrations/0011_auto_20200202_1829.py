# Generated by Django 2.2.6 on 2020-02-02 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('session', '0010_auto_20200202_1814'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activitypost',
            options={'ordering': ['-publish_date', '-updated']},
        ),
        migrations.AddField(
            model_name='activitypost',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='activitypost',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
