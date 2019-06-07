from django.shortcuts import render, get_object_or_404

from noticias import models


def index_noticias_view(request):
    noticias_todas = models.noticia.objects
    template_name = 'index_noticias.html'
    titulo = 'Noticias Colegio Los Pinos del Bosque'
    return render(request, template_name, {'title': titulo, 'noticias': noticias_todas})


def detalle_noticia_view(request, noticia_id):
    contenido_noticia = get_object_or_404(models.noticia, pk=noticia_id)
    template_name = 'noticias_detalle.html'
    return render(request, template_name, {'contenido': contenido_noticia})
