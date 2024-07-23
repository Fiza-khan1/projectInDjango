from typing import Any
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views import View
from .models import Product
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User


class productView(View):
 def get(self,request):
   mobile=Product.objects.filter(category='M')
   laptop=Product.objects.filter(category='L')
   electronics=Product.objects.filter(category='E')
   stationary=Product.objects.filter(category='S')
   context={
     'Mobile':mobile,
     'laptop':laptop,
     'electronics':electronics,
     'stationary':stationary
   }
   return render(request, 'app/home.html',context)

# def product_detail(request,pk):
#  product=Product.objects.get(id=pk)
#  return render(request, 'app/productdetail.html',{'product':product})


class product_detail(DetailView):
  model=Product
  template_name='app/productdetail.html'

  
  

# def add_to_cart(request,pk):
#  product=Product.objects.get(id=pk)
#  totalPrice=product.selling_price+700
#  print(totalPrice)
#  return render(request, 'app/addtocart.html',{'product':product,'TP':totalPrice})

class add_to_cart(DetailView):
    model = Product
    template_name='app/addtocart.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        total_price = product.selling_price + 700
        context["TP"] = total_price
        return context

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')


class mobile(View):
    def get(self,request):
        mobile=Product.objects.filter(category='M')
        return render(request, 'app/mobile.html',{'product':mobile})
    
class laptop(View):
    def get(self,request):
        laptop=Product.objects.filter(category='L')
        return render(request, 'app/mobile.html',{'product':laptop})
    
class electronics(View):
    def get(self,request):
        electronics=Product.objects.filter(category='E')
        return render(request, 'app/mobile.html',{'product':electronics})
    
class stationary(View):
    def get(self,request):
        stationary=Product.objects.filter(category='S')
        return render(request, 'app/mobile.html',{'product':stationary})
    
   

def userlogin(request):
 if request.method=='POST':
        email=['email']
        password=request.POST['password']
        email=request.POST['email']
        username = User.objects.get(email=email.lower()).username
        print(username)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request,'Login Successfully')
            return redirect('home')
 return render(request, 'app/login.html')

def customerregistration(request):
    if request.method=='POST':
            fm=RegForm(request.POST)
            if fm.is_valid():
                fm.save()
                print("SAVED")
                messages.success(request,'Registration completed successfully')
                
                return redirect('login')
    else:
      messages.error(request, 'Please correct the errors below.')
      fm=RegForm()
    return render(request, 'app/customerregistration.html',{'form':fm})

def checkout(request):
 return render(request, 'app/checkout.html')

def remove(request,pk):
  product=Product.objects.get(id=pk)
  product.delete()
  return redirect('home')

