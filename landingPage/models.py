from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    image = models.ImageField(upload_to="products/")
    price = models.DecimalField(max_digits=10,decimal_places=2)
    unit = models.CharField(max_length=50, default='unit')
        
    def __str__(self):
        return self.name
    
