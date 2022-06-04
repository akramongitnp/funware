from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from Product.models import Product

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        #username = request.POST.get('username') or
        username = request.POST['uname']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass']
        pass2 = request.POST['password']
        if pass1 == pass2:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = firstname
            myuser.last_name = lastname
            myuser.save()
            user = authenticate(username = username, password = pass1)
            login(request, user)
            return redirect('/')
        else:
            return redirect('/')

def signin(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['psw']

        user = authenticate(username = uname, password = password)
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'home.html', {'fname' : fname})
        else:
            return redirect('/')


    return render(request, 'home.html')

def index(request):
    products = Product.objects.all()
    context = {'prod': products}
    return render(request, 'index.html', context)

def profile(request):
    return render(request, 'profile.html')

def signout(request):
    logout(request)
    return redirect('/')

    


