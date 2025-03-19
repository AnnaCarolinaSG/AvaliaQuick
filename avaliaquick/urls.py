from django.urls import path
from avaliaquick.views import index

urlpatterns = [
    path('', index),
]