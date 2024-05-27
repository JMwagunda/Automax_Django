from django.db import models
from django.contrib.auth.models import User
from localflavor.us.models import USStateField, USZipCodeField  # Import US state and zip code fields from localflavor

# Create your models here.
class Location(models.Model):
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True)
    city = USStateField(default="NY")  # Using USStateField for US state abbreviations
    zip_code = USZipCodeField(blank=True)  # Using USZipCodeField for US zip codes
    
    def __str__(self):
        return f'Location {self.id}'
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True)  # Allow photo to be optional by setting blank=True
    bio = models.CharField(max_length=140, blank=True)
    phone_number = models.CharField(max_length=10, blank=True)  # Correct field name to be lowercase for consistency
    location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'{self.user.username}\'s profile'
