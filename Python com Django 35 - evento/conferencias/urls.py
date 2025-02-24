from django.urls import path
from .views import (
    lista_eventos, criar_evento, editar_evento, excluir_evento,
    lista_palestrantes, criar_palestrante, editar_palestrante, excluir_palestrante,
    lista_participantes, criar_participante, editar_participante, excluir_participante,
    lista_ingressos, criar_ingresso, editar_ingresso, excluir_ingresso,
    lista_programacao, criar_programacao, editar_programacao, excluir_programacao
)

urlpatterns = [
    path('eventos/', lista_eventos, name='lista_eventos'),
    path('eventos/novo/', criar_evento, name='criar_evento'),
    path('eventos/editar/<int:id>/', editar_evento, name='editar_evento'),
    path('eventos/excluir/<int:id>/', excluir_evento, name='excluir_evento'),

    path('palestrantes/', lista_palestrantes, name='lista_palestrantes'),
    path('palestrantes/novo/', criar_palestrante, name='criar_palestrante'),
    path('palestrantes/editar/<int:id>/', editar_palestrante, name='editar_palestrante'),
    path('palestrantes/excluir/<int:id>/', excluir_palestrante, name='excluir_palestrante'),

    path('participantes/', lista_participantes, name='lista_participantes'),
    path('participantes/novo/', criar_participante, name='criar_participante'),
    path('participantes/editar/<int:id>/', editar_participante, name='editar_participante'),
    path('participantes/excluir/<int:id>/', excluir_participante, name='excluir_participante'),

    path('ingressos/', lista_ingressos, name='lista_ingressos'),
    path('ingressos/novo/', criar_ingresso, name='criar_ingresso'),
    path('ingressos/editar/<int:id>/', editar_ingresso, name='editar_ingresso'),
    path('ingressos/excluir/<int:id>/', excluir_ingresso, name='excluir_ingresso'),

    path('programacao/', lista_programacao, name='lista_programacao'),
    path('programacao/novo/', criar_programacao, name='criar_programacao'),
    path('programacao/editar/<int:id>/', editar_programacao, name='editar_programacao'),
    path('programacao/excluir/<int:id>/', excluir_programacao, name='excluir_programacao'),
]
