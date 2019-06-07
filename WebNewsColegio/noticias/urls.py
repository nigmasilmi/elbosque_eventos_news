from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_noticias_view, name='home_noticias'),
    path('<int:noticia_id>/', views.detalle_noticia_view, name='detalle_noticia'),
]
