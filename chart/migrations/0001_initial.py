# Generated by Django 3.0.7 on 2020-07-03 20:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, help_text='Enter kid name', max_length=20)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, help_text='Enter reward', max_length=50)),
                ('points_needed', models.IntegerField(default=0, max_length=2)),
                ('description', models.TextField(help_text='Enter description of reward', max_length=250)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, help_text='Enter rule', max_length=50)),
                ('weight', models.IntegerField(default=0, max_length=2)),
                ('description', models.TextField(help_text='Enter description of rule', max_length=250)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='KidInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this kid', primary_key=True, serialize=False)),
                ('points', models.IntegerField(default=0, max_length=3)),
                ('kid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chart.Kid')),
            ],
            options={
                'ordering': ['-points'],
            },
        ),
        migrations.AddField(
            model_name='kid',
            name='rules',
            field=models.ManyToManyField(help_text='Select a rule to give to this kid', to='chart.Rule'),
        ),
    ]
