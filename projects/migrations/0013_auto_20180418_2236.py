# Generated by Django 2.0.1 on 2018-04-19 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20180418_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='boards',
            field=models.ManyToManyField(blank=True, related_name='projects', to='projects.Board'),
        ),
    ]