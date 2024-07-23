from django.contrib import admin
from .models import Customer, Product, OrderPlaced, Cart

class DynamicListDisplayAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        # Get all field names of the model
        return [field.name for field in self.model._meta.get_fields()]

# Register Customer model with dynamic list display
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'locality', 'city', 'zipcode']

# Register Product model with dynamic list display
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'title', 'selling_price', 'discounted_price', 'description', 'brand', 'category','product_img']


# Register OrderPlaced model with dynamic list display
@admin.register(OrderPlaced)
class OrderPlacedAdmin(DynamicListDisplayAdmin):
    pass

# Register Cart model with dynamic list display
@admin.register(Cart)
class CartAdmin(DynamicListDisplayAdmin):
    pass
