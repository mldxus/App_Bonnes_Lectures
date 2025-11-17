from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from bonnes_lectures.forms import *
from bonnes_lectures.models import *

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
    
def review_create(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk) 
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False) 
            review.book = book
            review.save() 
            return redirect('book-detail', pk=book.pk)
    else:
        form = ReviewForm()
        
    return render(request, 'bonnes_lectures/review_form.html', {'form': form, 'book': book})

def review_update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('book-detail', pk=review.book.pk)
    else:
        form = ReviewForm(instance=review) 
        
    return render(request, 'bonnes_lectures/review_form.html', {'form': form, 'book': review.book})

def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    book_pk = review.book.pk

    if request.method == 'POST':
        review.delete()
        return redirect('book-detail', pk=book_pk)
        
    return render(request, 'bonnes_lectures/review_confirm_delete.html', {'review': review})