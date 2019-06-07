# models noticias

from django.db import models


class noticia(models.Model):
    imagen = models.ImageField(upload_to='images/')
    titulo = models.CharField(max_length=120, null=True)
    resumen = models.TextField(null=True)
    texto_descripcion = models.TextField(null=True)
    fecha_de_publicacion = models.DateTimeField(auto_now=False, auto_now_add=False)
    tipo = models.CharField(max_length=10, default='noticias')
