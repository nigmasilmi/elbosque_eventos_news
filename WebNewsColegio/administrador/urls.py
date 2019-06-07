from django.urls import path

from . import views

urlpatterns = [

    path('', views.panel_administrativo_view, name='panel'),
    path('crear_e/', views.crear_evento, name='crear_evento'),
    path('lista_e/', views.listar_eventos, name='lista_de_eventos'),
    path('updat_e/<int:evento_id>', views.update_evento, name='update_evento'),
    path('updat_e/', views.hecho, name='update_hecho'),
    path('update_n/', views.hecho, name='update_hecho'),
    path('delet_e/<int:evento_id>', views.delete_evento, name='delete_evento'),
    path('crear_n', views.crear_noticia, name='crear_noticia'),
    path('lista_n/', views.listar_noticias, name='lista_de_noticias'),
    path('update_n/<int:noticia_id>', views.update_noticia, name='update_noticia'),
    path('delete_n/<int:noticia_id>', views.delete_noticia, name='delete_noticia'),
    path('confirma_delete/<int:noticia_id>', views.confirmar_delete_noticia, name='confirma_delete_noticia'),
    path('hecho/', views.hecho, name='hecho')
]
