from django.shortcuts import render
from django.views.generic import ListView
from about.models import ContactDetails, SocialNetworks


class ContactsListView(ListView):
    model = ContactDetails
    template_name = 'about/studio_contacts.html'
    queryset = ContactDetails.objects.get(pk=1)
    context_object_name = 'contacts'

    def get_context_data(self, **kwargs):
        context = super(ContactsListView, self).get_context_data(**kwargs)
        context['vk'] = SocialNetworks.objects.get(pk=1)
        context['instagram'] = SocialNetworks.objects.get(pk=2)
        context['whatsapp'] = SocialNetworks.objects.get(pk=3)
        context['telegram'] = SocialNetworks.objects.get(pk=4)
        context['facebook'] = SocialNetworks.objects.get(pk=5)
        return context


