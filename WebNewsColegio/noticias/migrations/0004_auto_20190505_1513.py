# Generated by Django 2.2.1 on 2019-05-05 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0003_auto_20190505_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='fecha_de_publicacion',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
