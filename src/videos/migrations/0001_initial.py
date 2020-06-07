# Generated by Django 3.0.6 on 2020-06-06 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.CharField(max_length=100)),
                ('coefficient', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('hours_per_year', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('hours_per_week', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('average_expression', models.CharField(max_length=100, null=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='videos.Branch', verbose_name='الشعبة')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('link', models.CharField(max_length=128)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='videos.Module', verbose_name='المادة')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='Level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='videos.Level', verbose_name='المستوى'),
        ),
    ]
