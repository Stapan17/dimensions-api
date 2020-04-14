from . import views
from django.urls import path

urlpatterns = [
    path('dimension/', views.dimension),
]
