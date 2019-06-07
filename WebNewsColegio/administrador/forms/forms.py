from django import forms
from django.db import models
from eventos.models import evento
from noticias.models import noticia


class EventoModelForm(forms.ModelForm):
    class Meta:
        imagen = models.ImageField()
        fecha_del_evento = models.DateTimeField(auto_now=False, auto_now_add=False)
        fecha_de_publicacion = models.DateTimeField(auto_now=False, auto_now_add=False)
        model = evento
        fields = [
            'imagen',
            'titulo',
            'resumen',
            'texto_descripcion',
            'fecha_del_evento',
            'fecha_de_publicacion',
            'tipo',
        ]

    def titulo_chequeado(self, *args, **kwargs):
        instance = self.instance
        titulo = self.cleaned_data.get('titulo')
        qs = evento.objects.filter(title__iexact=titulo)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("Este evento existe, intente con uno diferente")
        return titulo


class NoticiaModelForm(forms.ModelForm):
    class Meta:
        model = noticia
        imagen = models.ImageField()
        fecha_de_publicacion = models.DateTimeField(auto_now=False, auto_now_add=False)
        fields = [
            'imagen',
            'titulo',
            'resumen',
            'texto_descripcion',
            'fecha_de_publicacion',
            'tipo',
        ]

    def titulo_chequeado(self, *args, **kwargs):
        instance = self.instance
        titulo = self.cleaned_data.get('titulo')
        qs = evento.objects.filter(title__iexact=titulo)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("Esta noticia existe, intente con una diferente")
        return titulo
