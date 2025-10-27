from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ItemList(models.Model):
    Category_name=models.CharField(max_length=15)

    def __str__(self):
        return self.Category_name

class Items(models.Model):
    Item_name=models.CharField(max_length=40)
    description=models.TextField(blank=False)
    Price=models.IntegerField()
    Category=models.ForeignKey(ItemList,related_name="Name",on_delete=models.CASCADE)
    Image=models.ImageField(upload_to='items/')
    
    def __str__(self):
        return self.Item_name
    
class AboutUs(models.Model):
    Description=models.TextField(blank=False)


class Feedback(models.Model):
    User_name=models.CharField(max_length=15)
    Description=models.TextField(blank=False)
    Rating=models.IntegerField()
    Image=models.ImageField(upload_to='items/',blank=True)

    def __str__(self):
        return self.User_name

class BookTable(models.Model):
    Name=models.CharField(max_length=15)
    Phone_number=models.IntegerField()
    Email=models.EmailField()
    Total_person=models.IntegerField()
    Booking_date=models.DateField()

    def __str__(self):
        return self.Name

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_items = models.ManyToManyField('Items', related_name="orders")
    name = models.CharField(max_length=100, blank=True)  # auto-filled from user
    email = models.EmailField(blank=True)                 # auto-filled from user
    phone = models.CharField(max_length=15)
    address = models.TextField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='items/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def save(self, *args, **kwargs):
        # Auto-fill name and email from logged-in user if not provided
        if self.user:
            if not self.name:
                self.name = self.user.get_full_name() or self.user.username
            if not self.email:
                self.email = self.user.email
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

