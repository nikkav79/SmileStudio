from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views import View
from .models import ContactDetails, SocialNetworks


class Contacts(View):
    def get(self, request):
        contacts = ContactDetails.objects.all()
        soc_networks = SocialNetworks.objects.all()
        return render(request,
                      template_name='contacts/contacts_base.html',
                      context={'contacts': contacts, 'soc_networks': soc_networks}
                      )

