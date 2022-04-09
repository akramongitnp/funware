from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

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

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()

        return redirect(request, '/signin')


    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['psw']

        user = authenticate(username = uname, password = password)
        if user is not None:
            login(request, user)
            fname = user.first_name
            print(fname)
            return render(request, 'home.html', {'fname' : fname})
        else:
            return redirect('/signup')


    return render(request, 'signin.html')

def signout(request):
    logout(request)
    return redirect('/signin')
    


