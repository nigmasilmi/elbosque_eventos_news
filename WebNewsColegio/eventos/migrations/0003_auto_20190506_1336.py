# Generated by Django 2.2.1 on 2019-05-06 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_evento_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fecha_de_publicacion',
            field=models.DateTimeField(),
        ),
    ]
