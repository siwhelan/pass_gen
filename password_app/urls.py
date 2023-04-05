from django.urls import path
from password_app.views import password_generator_view

urlpatterns = [
    path('', password_generator_view, name='password_generator'),
]
