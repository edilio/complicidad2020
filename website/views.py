from django.shortcuts import render
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from . import models


def home(request):
    return render(request, 'website/home.html')


def buy(request):
    return render(request, 'website/comprar.html')


def about(request):
    return render(request, 'website/sobre-la-autora.html')


def contact_us(request):
    return render(request, 'website/contactanos.html')


class PoemDetailView(DetailView):

    model = models.Poem
    queryset = models.Poem.objects.filter(draft=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class PoemListView(ListView):

    model = models.Poem
    paginate_by = 20  # if pagination is desired
    queryset = models.Poem.objects.filter(draft=False).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
