from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Cover

# 1. API : Renvoie du JSON
def api_cover(request, isbn):
    # On cherche l'image, ou on renvoie une erreur 404 si elle n'existe pas
    cover = get_object_or_404(Cover, isbn=isbn)
    
    data = {
        'isbn': cover.isbn,
        'format': cover.format,
        'image': cover.image_data, # L'image en base64
    }
    return JsonResponse(data)

# 2. GUI : Renvoie une page HTML
def gui_cover(request, isbn):
    cover = get_object_or_404(Cover, isbn=isbn)
    return render(request, 'covers/detail.html', {'cover': cover})