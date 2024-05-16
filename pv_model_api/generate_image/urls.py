from django.urls import path
from . import views

urlpatterns = [
    path('generate-image/', views.ImageGenerationView.as_view(), name='generate_image'),
]

