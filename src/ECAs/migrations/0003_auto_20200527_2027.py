# Generated by Django 3.0.6 on 2020-05-27 19:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ECAs', '0002_activities_imagesactivities'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activities',
            old_name='post_date',
            new_name='act_date',
        ),
        migrations.RenameField(
            model_name='activities',
            old_name='post_update',
            new_name='act_update',
        ),
        migrations.AlterField(
            model_name='activities',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='activities',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='ECAs.TypeActivities'),
        ),
        migrations.AlterField(
            model_name='imagesactivities',
            name='activitie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='ECAs.Activities'),
        ),
    ]
