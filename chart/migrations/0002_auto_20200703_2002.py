# Generated by Django 3.0.7 on 2020-07-03 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kidinstance',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reward',
            name='points_needed',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rule',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]