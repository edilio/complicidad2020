from django.urls import path
from .views import home, buy, about, contact_us

urlpatterns = [
    path('comprar-complicidad-de-suspiros-y-gemidos', buy, name='buy'),
    path('acerca-de-la-autora', about, name='about'),
    path('contactanos', contact_us, name='contact-us'),
    path('', home, name='home'),
]
