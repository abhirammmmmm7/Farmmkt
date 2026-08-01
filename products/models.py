from django.db import models

# Create your models here.
class Product(models.Model):
    UNIT_CHOICES = (
        ('kg', 'Kilogram'),
        ('g', 'Gram'),
        ('liter', 'Liter'),
        ('piece', 'Piece'),
        ('dozen', 'Dozen'),
    )
    
    farmer = models.ForeignKey('farmers.Farmer', on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    image = models.ImageField(upload_to='products/images/', null=True, blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']