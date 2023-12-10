from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    
    def __str__(self):
        return self.name
        
    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL) # Foreign key to the category model
    sku = models.CharField(max_length=254, null=True, blank=True) # SKU is a unique identifier for each product
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2) # Decimal field to store the price
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True) # Decimal field to store the rating
    image_url = models.URLField(max_length=1024, null=True, blank=True) # URL field to store the image URL
    image = models.ImageField(null=True, blank=True) # Image field to store the image itself
    
    def __str__(self):
        return self.name