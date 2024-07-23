from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxLengthValidator

STATE_CHOICES = (
    ("AN", "Andaman and Nicobar Islands"),
    ("AP", "Andhra Pradesh"),
    ("AR", "Arunachal Pradesh"),
    ("AS", "Assam"),
    ("BR", "Bihar"),
    ("CG", "Chhattisgarh"),
    ("CH", "Chandigarh"),
    ("DN", "Dadra and Nagar Haveli"),
    ("DD", "Daman and Diu"),
    ("DL", "Delhi"),
    ("GA", "Goa"),
    ("GJ", "Gujarat"),
    ("HR", "Haryana"),
    ("HP", "Himachal Pradesh"),
    ("JK", "Jammu and Kashmir"),
    ("JH", "Jharkhand"),
    ("KA", "Karnataka"),
    ("KL", "Kerala"),
    ("LA", "Ladakh"),
    ("LD", "Lakshadweep"),
    ("MP", "Madhya Pradesh"),
    ("MH", "Maharashtra"),
    ("MN", "Manipur"),
    ("ML", "Meghalaya"),
    ("MZ", "Mizoram"),
    ("NL", "Nagaland"),
    ("OD", "Odisha"),
    ("PB", "Punjab"),
    ("PY", "Pondicherry"),
    ("RJ", "Rajasthan"),
    ("SK", "Sikkim"),
    ("TN", "Tamil Nadu"),
    ("TS", "Telangana"),
    ("TR", "Tripura"),
    ("UP", "Uttar Pradesh"),
    ("UK", "Uttarakhand"),
    ("WB", "West Bengal"),
)

Category = (
    ("M", "Mobile"),
    ("L", "Laptop"),
    ("E", "Electronics"),
    ("S", "Stationary"),
)

Status_choice = (
    ('Accepted', 'Accepted'),
    ('On the way', 'On the way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
    ('Packed', 'Packed'),
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(choices=STATE_CHOICES, max_length=200)
    zipcode = models.IntegerField()

    def __str__(self):
        return f"Customer {self.name} ({self.id})"

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=200)
    category = models.CharField(choices=Category, max_length=100)
    product_img = models.ImageField(upload_to='product_image')

    def __str__(self):
        return f"Product {self.title} ({self.id})"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    def __str__(self):
        return f"Cart {self.id} - User {self.user.username}"

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=Status_choice, default='Pending')

    def __str__(self):
        return f"Order {self.id} - User {self.user.username}"
