# Generated by Django 2.0.1 on 2018-01-22 23:23

from django.db import migrations, models
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20180122_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(upload_to=projects.models.project_image_path),
        ),
    ]
