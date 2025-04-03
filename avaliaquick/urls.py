from django.urls import path
from avaliaquick.views import index, avaliacao

urlpatterns = [
    path('', index),
    path('avaliacao/', avaliacao)
]