# Generated by Django 3.0.7 on 2020-08-12 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0007_remove_kidinstance_rules'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RuleInstance',
        ),
    ]
