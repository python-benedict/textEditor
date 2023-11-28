from django.shortcuts import render
from .models import Document
# Create your views here.

def index(request):
    documents = Document.objects.all()
    return render(request, 'text_editor/index.html', {'documents': documents})

