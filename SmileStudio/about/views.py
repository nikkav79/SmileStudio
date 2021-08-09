from django.http import HttpResponse

def about(request):
    return HttpResponse('<h1>О нас<h1>')


