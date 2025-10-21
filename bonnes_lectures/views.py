from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from bonnes_lectures.forms import BookForm
from bonnes_lectures.models import Book

def about(request):
    return render(request, 'bonnes_lectures/about.html')

def welcome(request):
    return render(request, 'bonnes_lectures/welcome.html')

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bonnes_lectures/book_detail.html', {'book': book})

def book_summary_list(request):
    books = Book.objects.all()
    return render(request, 'bonnes_lectures/book_summary_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            # Redirige vers la page de détail du livre nouvellement créé
            return redirect('book-detail', pk=book.pk)
    else:
        form = BookForm()

    return render(request, 'bonnes_lectures/book_form.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book-summary-list')
    return render(request, 'bonnes_lectures/book_confirm_delete.html', {'book': book})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect('book-detail', pk=book.pk)
    else:
        form = BookForm(instance=book)

    return render(request, 'bonnes_lectures/book_form.html', {'form': form})
    