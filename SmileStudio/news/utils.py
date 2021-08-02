from .models import *
from django.shortcuts import get_object_or_404
from django.shortcuts import render

class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        self.obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request,
                      template_name=self.template,
                      context={self.model.__name__.lower(): self.obj
                               })