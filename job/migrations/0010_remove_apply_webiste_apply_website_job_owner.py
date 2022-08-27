# Generated by Django 4.1 on 2022-08-26 11:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0009_remove_job_owner_job_slug_apply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='webiste',
        ),
        migrations.AddField(
            model_name='apply',
            name='website',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='job_owner', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]