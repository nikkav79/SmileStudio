from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import View
from .forms import *
from .models import *

def mainpage(request):
    return render(request, 'mainpage/mainpage_base.html')


class Write(View):
    def get(self, request):
        form = WriteToUsForm
        return render(request, 'mainpage/mainpage_write_to_us.html', context={'form': form})

    def post(self, request):
        bound_form = WriteToUsForm(request.POST)
        if bound_form.is_valid():
            record = bound_form.save()
            return HttpResponseRedirect('/about/')
        return render(request, 'mainpage/mainpage_write_to_us.html', context={'form': bound_form})