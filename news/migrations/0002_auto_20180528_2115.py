# Generated by Django 2.0.1 on 2018-05-29 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='cover_image',
            field=models.ImageField(help_text='Imagem que vai no preview da noticia, no topo da pagina de detalhes e no final do texto da noticia, <strong>Cuidado</strong> com imagens muito grandes! Menos de 1MB é mais que suficiente.', upload_to='news_cover'),
        ),
    ]
