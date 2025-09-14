from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_receitas, name='listar_receitas'),
    path('receita/<int:pk>/', views.detalhe_receita, name='detalhe_receita'),
    path('receita/criar/', views.criar_receita, name='criar_receita'),
    path('receita/<int:pk>/editar/', views.editar_receita, name='editar_receita'),
    path('receita/<int:pk>/deletar/', views.deletar_receita, name='deletar_receita'),
    path('receita/importar/', views.importar_receita, name='importar_receita'),
]