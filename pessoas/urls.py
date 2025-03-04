from django.urls import path
from . import views

urlpatterns = [
    path('criar_pessoa/', views.criar_pessoa, name='criar_pessoa'),
    path('deletar_pessoa/<int:id>', views.deletar_pessoa, name='deletar_pessoa'),
    path('atualizar_pessoa/<int:id>', views.atualizar_pessoa, name='atualizar_pessoa'),
]
