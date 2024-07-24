from django.urls import path
from app import views
from django.contrib.auth import views as auth_views
from .forms import passwordSetting
urlpatterns = [
    path('', views.productView.as_view(),name='home'),
    path('product-detail/<int:pk>/', views.product_detail.as_view(), name='product_detail'),
    path('cart/<int:pk>/', views.add_to_cart.as_view(), name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password.as_view(), name='changepassword'),
    path('mobile/', views.mobile.as_view(), name='mobile'),
    path('laptop/', views.laptop.as_view(), name='laptop'),
    path('electronics/',views.electronics.as_view(),name='electronics'),
    path('stationary/',views.stationary.as_view(),name='stationary'),
    path('userLogout/',views.userLogout,name='userLogout'),
    path('login/', views.userlogin.as_view(), name='login'),
    path('accounts/profile/',views.profile.as_view(), name='Accprofile'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('remove/<int:pk>', views.remove,name='remove'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html'),name='passwordreset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='password_reset_done'),
    path('password_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=passwordSetting),name='password_reset_confirm'),
    path('password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/password_complete.html'),name='password_reset_complete'),


   

]
