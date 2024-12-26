from django.db import models

class Anime(models.Model):
    judul = models.CharField(max_length=255, verbose_name="Judul Anime")
    jadwal_tayang = models.CharField(max_length=255, verbose_name="Jadwal Tayang")
    studio = models.CharField(max_length=255, verbose_name="Studio Produksi")
    genre = models.CharField(max_length=255, verbose_name="Genre")
    durasi_per_eps = models.CharField(max_length=50, verbose_name="Durasi per Episode")
    sumber = models.CharField(max_length=255, verbose_name="Sumber (Source)")
    rating = models.FloatField(verbose_name="Rating")
    link_anime = models.URLField(max_length=500, verbose_name="Link Anime")

    def __str__(self):
        return self.judul
