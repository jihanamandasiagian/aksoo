from django.shortcuts import render
from .models import Anime

# Fungsi view untuk menampilkan data anime
def anime_list(request):
    # Mengambil semua data anime dari database
    all_anime = Anime.objects.all()
    
    # Mengirim data anime ke template
    return render(request, 'anime_list.html', {'anime_list': all_anime})
