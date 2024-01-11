from django.shortcuts import render, HttpResponse, redirect
from .models import signin
from .models import signup
from .models import contact_us
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.
def home(request):
    return render(request, 'index.html')


def signin(request):
    if request.method =='POST':
        print('hi')
        email=request.POST['email']
        password=request.POST['password']
        user = auth.authenticate(username=email, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials!")
            return redirect('/signin')


    else:
        return render(request, 'signin.html')

def signup(request):
    if request.method =='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        repassword=request.POST['repassword']
        # user = auth.authenticate(name=name, password=repassword)
        # print(user)
        if password==repassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exist:)')
                print('email already exist')
                return redirect('/signup/')
            else:
                user = User.objects.create_user(username=email, password=password, email=email, first_name=name)
                user.save()
                return redirect('/signin')
                
        else:
            messages.info(request, "Passowrd didn't match:(")
            return redirect('/signup/')

    else:

        return render(request, 'signup.html')
    
   
def about(request):
    return HttpResponse("This is about page")
def services(request):
    return HttpResponse("This is services page")

def portfolio(request):
    return HttpResponse("This is contact page")



        
def contactus(request):
    if request.method == 'POST':
        name = request.POST['Name']
        email = request.POST['email']
        message = request.POST['message']

        b = contact_us(name=name, email=email, message=message)
        b.save()
        forms = contact_us.objects.all()
        context={'forms':forms}
        return redirect('/contactus/')
    

    else:
        return render(request, 'contactus.html')
