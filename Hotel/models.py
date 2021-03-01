from django.db import models
from phone_field import PhoneField
from django.core.validators import RegexValidator
# Create your models here.

class HotelInfo(models.Model):
    User=models.CharField(max_length=100,null=True)
    Name = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{10}$', message="Phone number must be 10 digits and  entered in the format: '98XXXXXXXX'.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=13)  # validators should be a list
    number_of_room = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.Name
