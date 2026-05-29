from django.shortcuts import render
from .models import Book

def index(request):
    books = Book.objects.all()
    context = {
        'books': books,
        'total_books': books.count(),
    }
    return render(request, 'index.html', context)