from django.shortcuts import render, get_object_or_404

from administrador.forms.forms import NoticiaModelForm, EventoModelForm
from eventos.models import evento
from noticias.models import noticia
from administrador.models import *


def landing_page_view(request):
    eventos_todos = evento.objects
    noticias_todas = noticia.objects
    titulo = 'Eventos y Noticias del Colegio Los Pinos del Bosque'
    template_name = 'index.html'
    return render(request, template_name, {
        'title': titulo,
        'eventos_ppal': eventos_todos,
        'noticias_ppal': noticias_todas},
                  )


def panel_administrativo_view(request):
    template_name = 'panel_administrativo.html'
    titulo = "Panel administrativo de Noticias y Eventos"
    return render(request, template_name, {'title': titulo})


def crear_evento(request):
    template_name = 'crear_evento.html'
    form = EventoModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
       # form = EventoModelForm()
    template_name = 'crear_evento.html'
    context = {'form': form}
    return render(request, template_name, context)


def listar_eventos(request):
    template_name = 'lista_eventos.html'
    eventos_todos = evento.objects
    titulo = 'Eventos Colegio Los Pinos del Bosque'
    return render(request, template_name, {'title': titulo, 'eventos': eventos_todos})


def update_evento(request, evento_id):
    template_name = 'update_evento.html'
    evento_a_editar = evento.objects.get(pk=evento_id)
    form = EventoModelForm(instance=evento_a_editar)
    return render(request, template_name, {'form': form})


def delete_evento(request, evento_id):
    template_name = 'delete_evento.html'
    contenido_evento = get_object_or_404(evento, pk=evento_id)
    return render(request, template_name, {'contenido': contenido_evento})


def crear_noticia(request):
    template_name = 'crear_noticia.html'
    form = NoticiaModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = NoticiaModelForm()
        template_name = 'crear_noticia.html'
    context = {'form': form}
    return render(request, template_name, context)


def listar_noticias(request):
    template_name = 'lista_noticias.html'
    noticias_todas = noticia.objects
    titulo = 'Noticias Colegio Los Pinos del Bosque'
    return render(request, template_name, {'title': titulo, 'noticias': noticias_todas})


def update_noticia(request, noticia_id):
    template_name = 'update_noticia.html'
    noticia_a_editar = noticia.objects.get(pk=noticia_id)
    form = NoticiaModelForm(instance=noticia_a_editar)
    return render(request, template_name, {'form': form})


def delete_noticia(request, noticia_id):
    template_name = 'delete_noticia.html'
    contenido_noticia = get_object_or_404(noticia, pk=noticia_id)
    return render(request, template_name, {'contenido': contenido_noticia})


def confirmar_delete_noticia(request, noticia_id):
    template_name = 'confirma_elimina_noticia.html'
    contenido_noticia = get_object_or_404(noticia, pk=noticia_id)
    id_eliminar = noticia_id
    return render(request, template_name, {'id': id_eliminar, 'contenido': contenido_noticia})


def hecho(request):
    template_name = "hecho.html"
    return render(request, template_name)
