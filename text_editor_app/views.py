from django.shortcuts import render
from .models import Document
# Create your views here.

def index(request):
    documents = Document.objects.all()
    return render(request, 'text_editor/index.html', {'documents': documents})

def edit_document(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    return render(request, 'text_editor/edit_document.html', {'document': document})