from django.db import models

class Coffee(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='coffee_images/')  # Tentukan folder penyimpanan gambar

    def __str__(self):
        return self.name