# Generated by Django 2.0.1 on 2018-05-29 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20180528_2147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-is_active', '-debut_year']},
        ),
    ]
