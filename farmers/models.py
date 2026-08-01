from django.db import models

# Create your models here.
class Farmer(models.Model):
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE, related_name='farmer_profile')
    farm_name = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='farmers/profile_images/', null=True, blank=True)
    farm_description = models.TextField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.farm_name
