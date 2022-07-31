from django.urls import path
from .views import redirector

urlpatterns = [
    path('', redirector, name='redirector'),
]
