# Generated by Django 3.1.5 on 2021-01-20 00:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recruit', '0003_auto_20210119_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EvaluationCriteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('max_score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=500)),
                ('answer', models.TextField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='application',
            name='applying_positions',
        ),
        migrations.DeleteModel(
            name='Position',
        ),
        migrations.AddField(
            model_name='evaluation',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruit.application'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='evaluator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='application',
            name='applying_parts',
            field=models.ManyToManyField(to='recruit.Part'),
        ),
        migrations.AddField(
            model_name='application',
            name='questions',
            field=models.ManyToManyField(to='recruit.Question'),
        ),
    ]
