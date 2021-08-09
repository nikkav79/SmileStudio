from django import forms
from .models import WriteToUs
from django.core.exceptions import ValidationError
from phone_field import PhoneField



class WriteToUsForm(forms.Form):
    """Данные пользователей для обратной связи"""
    name = forms.CharField(max_length=100)
    # phone = PhoneField(blank=True)
    email = forms.EmailField(max_length=254)
    lesson_type = forms.CharField(max_length=100)

    name.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    lesson_type.widget.attrs.update({'class': 'form-control'})

    def clean_name(self):
        new_name = self.cleaned_data['name'].lower()

        if new_name == 'степан':
            raise ValidationError('This name is invalid')
        return new_name

    def save(self):
        new_write = WriteToUs.objects.create(name=self.cleaned_data['name'], email=self.cleaned_data['email'],
                                             lesson_type=self.cleaned_data['lesson_type'])
        return new_write
# class WriteToUsForm(forms.ModelForm):
#
#     class Meta:
#         model = WriteToUs
#         fields = ('name', 'phone', 'email', 'lesson_type')
