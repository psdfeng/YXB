from django.shortcuts import render
from django.views import generic

from .models import Drug


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'DrugID/index.html'
    context_object_name = 'drug_list'

    def get_queryset(self):
        """
        :return: all drugs
        """
        return Drug.objects.all()
