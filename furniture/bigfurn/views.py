from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class BigFurnPage(ListView):
    model = Bigfurn
    template_name = 'bigfurn/bigfurnpage.html'
    context_object_name = 'bigfurn'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Furniture'
        return context