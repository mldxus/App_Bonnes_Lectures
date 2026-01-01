from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from bonnes_lectures.forms import *
from bonnes_lectures.models import *
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

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

@login_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False) 
            book.user = request.user    
            book.save()                  
            return redirect('book-detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'bonnes_lectures/book_form.html', {'form': form})

@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    if book.user != request.user:
        raise PermissionDenied("Vous n'avez pas le droit de supprimer ce livre.")
        
    if request.method == 'POST':
        book.delete()
        return redirect('book-summary-list')
    return render(request, 'bonnes_lectures/book_confirm_delete.html', {'book': book})

@login_required
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.user != request.user:
        raise PermissionDenied("Vous n'avez pas le droit de modifier ce livre.")
        
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect('book-detail', pk=book.pk)
    else:
        form = BookForm(instance=book)

    return render(request, 'bonnes_lectures/book_form.html', {'form': form})
    
@login_required
def review_create(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book          
            review.user = request.user  
            review.save()
            return redirect('book-detail', pk=book.pk)
    else:
        form = ReviewForm()
    return render(request, 'bonnes_lectures/review_form.html', {'form': form, 'book': book})
    
@login_required
def review_update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    
    if review.user != request.user:
        raise PermissionDenied

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('book-detail', pk=review.book.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'bonnes_lectures/review_form.html', {'form': form, 'book': review.book})


@login_required
def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    book_pk = review.book.pk
    
    # Vérification
    if review.user != request.user:
        raise PermissionDenied

    if request.method == 'POST':
        review.delete()
        return redirect('book-detail', pk=book_pk)
    return render(request, 'bonnes_lectures/review_confirm_delete.html', {'review': review})


 # 1. Liste des auteurs
def author_list(request):
    authors = Author.objects.all().order_by('last_name')
    return render(request, 'bonnes_lectures/author_list.html', {'authors': authors})

# 2. Créer un auteur
@login_required
def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False) 
            author.user = request.user       
            author.save()                 
            return redirect('author-list')
    else:
        form = AuthorForm()
    return render(request, 'bonnes_lectures/author_form.html', {'form': form})

# 3. Modifier un auteur
@login_required
def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    
    if author.user != request.user:
        raise PermissionDenied
        
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author-list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'bonnes_lectures/author_form.html', {'form': form})

# 4. Supprimer un auteur
@login_required
def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)

    if author.user != request.user:
        raise PermissionDenied
        
    if request.method == 'POST':
        author.delete()
        return redirect('author-list')
    return render(request, 'bonnes_lectures/author_confirm_delete.html', {'author': author})