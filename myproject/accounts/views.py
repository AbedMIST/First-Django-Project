from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        email = request.POST['email']

        if pass1==pass2:

            if User.objects.filter(username=username).exists():
                print("Username already exists")
                messages.error(request, "That username is already taken. Please choose another.")
                return redirect('register')
            if User.objects.filter(email=email).exists():
                print("Email already exists")
                messages.error(request, "An account with this email already exists.")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=pass1, first_name=first_name, last_name=last_name)
                user.save()
                print("User created successfully..")
                # messages.info(request, "User created successfully")

                return redirect('/')
        else:
            print('Two given passwords not matched')
            messages.error(request, "The two passwords do not match. Please try again.")
            return redirect('register')
    
    else:
        return render(request, 'register.html')
    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        print(user)

        if user is not None:
            auth.login(request, user)
            print("Logged in successfully..")
            # messages.info(request, "Logged in successfully")

            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('login')
    
    else:
        return render(request, 'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/')
