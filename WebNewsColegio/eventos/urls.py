from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_eventos_view, name='home_eventos'),
    path('<int:evento_id>', views.detalle_eventos_view, name='evento_detalle'),

]
