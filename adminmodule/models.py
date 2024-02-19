from django.db import models

# Create your models here.

class Toko(models.Model):
    nama_toko = models.CharField(max_length=255)
    pemilik = models.CharField(max_length=255)
    tahun_berdiri = models.CharField(max_length=255)
    
    JENIS_TOKO = (
        ('MENJUAL JASA', 'MENJUAL JASA'),
        ('MENJUAL PRODUK', 'MENJUAL PRODUK'),
    )
    jenis_toko = models.CharField(max_length=255 , choices=JENIS_TOKO)
    
    def __str__(self):
        return self.nama_toko