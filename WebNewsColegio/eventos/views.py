from django.shortcuts import render, get_object_or_404
from eventos import models


def index_eventos_view(request):
    eventos_todos = models.evento.objects
    template_name = 'index_eventos.html'
    titulo = 'Eventos Colegio Los Pinos del Bosque'
    return render(request, template_name, {'title': titulo, 'eventos': eventos_todos})


def detalle_eventos_view(request, evento_id):
    contenido_evento = get_object_or_404(models.evento, pk=evento_id)
    template_name = 'evento_detalle.html'
    return render(request, template_name, {'contenido': contenido_evento})


