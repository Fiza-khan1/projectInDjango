from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from .forms import RegForm,CustomerForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views import View
from .models import Product
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from .forms import loginForm,passChange
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,PasswordChangeView

class change_password(PasswordChangeView):
    template_name = "app/changepassword.html"
    form_class = passChange
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        messages.success(self.request,'Password Cahnge Successfully')
        return super().form_valid(form)
    def form_invalid(self, form):    
        return super().form_invalid(form)
 
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

class profile(FormView):
    template_name = "app/profile.html"
    form_class = CustomerForm
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        customer=form.save(commit=False)
        customer.user = self.request.user
        customer.save()
        return super().form_valid(form)
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
def address(request):
 
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')




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
class userlogin(LoginView):  
    template_name = "app/login.html"
    def form_valid(self, form):
        messages.success(self.request, 'Login Successfully!!!!!!')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid credentials, please try again.')
        return super().form_invalid(form)

# def userlogin(request):
#  if request.method=='POST':
#         password=request.POST.get('password')
#         email=request.POST.get('email')
#         try:
#               username = User.objects.get(email=email).username
#               print(username)
#               user = authenticate(username=username, password=password)
#               print(user)
#         except User.DoesNotExist:
#             messages.error(request, 'Invalid email or password.')
#             return render(request, 'app/login.html')
#         if user is not None:
#             login(request,user)
#             messages.success(request,'Login Successfully')
#             return redirect('home')
#  return render(request, 'app/login.html')

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

def userLogout(request):
  logout(request)
  messages.success(request, 'You have been logged out successfully.')
  return redirect('login')
  
