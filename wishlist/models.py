from django.db import models

# Create your models here.
class Wishlist(models.Model):
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE, related_name='wishlist_items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('customer', 'product')

    def __str__(self):
        return f"{self.customer.user.username}'s Wishlist"