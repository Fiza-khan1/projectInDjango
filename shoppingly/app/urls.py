from django.urls import path
from app import views
urlpatterns = [
    path('', views.productView.as_view(),name='home'),
    path('product-detail/<int:pk>/', views.product_detail.as_view(), name='product_detail'),
    path('cart/<int:pk>', views.add_to_cart.as_view(), name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile.as_view(), name='mobile'),
    path('laptop/', views.laptop.as_view(), name='laptop'),
    path('electronics/',views.electronics.as_view(),name='electronics'),
    path('stationary/',views.stationary.as_view(),name='stationary'),

    path('login/', views.userlogin, name='login'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('remove/<int:pk>', views.remove,name='remove')

]
