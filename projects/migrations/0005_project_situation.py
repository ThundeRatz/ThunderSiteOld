# Generated by Django 2.0.1 on 2018-01-22 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='situation',
            field=models.CharField(choices=[('A', 'active'), ('I', 'inactive')], default='A', max_length=1),
            preserve_default=False,
        ),
    ]
