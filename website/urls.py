from django.urls import path
from .views import home, buy, about, contact_us, PoemDetailView, PoemListView

urlpatterns = [
    path('comprar-complicidad-de-suspiros-y-gemidos', buy, name='buy'),
    path('acerca-de-la-autora', about, name='about'),
    path('contactanos', contact_us, name='contact-us'),
    path('poemas', PoemListView.as_view(), name='poem-list'),
    path('poema/<int:pk>', PoemDetailView.as_view(), name='poem-detail'),
    path('', home, name='home'),
]
