from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='shoe/')

    def __str__(self):
        return self.title