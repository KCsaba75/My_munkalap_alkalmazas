from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

@login_required(login_url='login_page')
def home(request):
    return render(request,'home.html')
#----- Bejelentkezés---------
def login_page(request):
    if  request.method=='POST' :     
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('home')
        return render(request,'login.html', {'erorr_message': 'Hibás felhasználó név vagy jelszó!'})    
                     
    return render(request,'login.html')

#----- Regisztráció----------
def register_page(request):
    if  request.method=='POST' :
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']
          
        if password != password2:
              
                return render(request, 'reg.html',{'erorr_message': 'A jelszavak nem egyeznek!'})
        
        if User.objects.filter(username=username).exists():
           return render(request, 'reg.html',{'erorr_message': 'Van már ilyen felhasználó!'}) 
        else:
            user=User.objects.create_user(username=username, password=password)
            user.save()
            return render (request, "login.html", { 'erorr_message':' sikeresen regisztrálva!'} )



    return render(request,'reg.html')


def logout_page(request):
    logout(request)
    return redirect('home')