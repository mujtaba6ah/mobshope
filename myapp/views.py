from django.shortcuts import render,redirect
from .models import Item
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms


# Create your views here.
def index(request):
    items = Item.objects.all()

    #search
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        items = items.filter(name__icontains=item_name)




    #pages
    paginator = Paginator(items,6)
    page = request.GET.get('page')
    items = paginator.get_page(page)

    return render(request,'myapp/index.html',{'items':items})

def detail(request,id):
    item = Item.objects.get(id=id)

    return render(request,'myapp/detail.html',{'item':item})

def category_items(request, id):
    category = Category.objects.get(id=id)
    items = Item.objects.filter(category=category)
    return render(request, 'myapp/category_items.html', {'category': category, 'items': items})

#login users 
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password  = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You Have Been Logged in"))
            return redirect('index')

        else:
            messages.success(request, ("There was an error. please try again "))
            return redirect('login')



    else:
        return render(request,'myapp/login.html',{'login':login})

def logout_user(request):
    logout(request)
    messages.success(request, ("YOU have been logged out."))
    return redirect('index')

#  register user:

def register_user(request):
        #form = UserCreationForm()
        #return render(request,'myapp/register.html',{'form':form})
        
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user to the database
            login(request, user)  # Log the user in after registration
            messages.success(request, "Registration successful!")
            return redirect('index')  # Redirect to home page or any other page
        else:
            messages.error(request, "Error during registration. Please try again.")
    else:
        form = SignUpForm()

    return render(request, 'myapp/register.html', {'form': form})
    