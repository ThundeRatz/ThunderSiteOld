# Generated by Django 2.0.1 on 2018-04-16 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("projects", "0002_project_thumbnail")]

    operations = [
        migrations.AddField(
            model_name="project",
            name="card_and_top",
            field=models.IntegerField(blank=True, default=0, null=True),
        )
    ]
