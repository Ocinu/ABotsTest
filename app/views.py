from django.shortcuts import render
from .models import WikiPage


def index(request):
    records = WikiPage.objects.all()
    content = {
        'records': records,
        'title': 'Головна сторінка',
    }
    return render(request, 'index.html', content)


def add_new_record(request):
    return render(request, 'add_new.html')
