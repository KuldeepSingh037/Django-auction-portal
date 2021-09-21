from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import credentials
# from auction.models import seller
from django.urls import reverse

# Create your views here.

def logout(request):
    return render(request, 'login/login.html', {
        'error_message': 'logged out successfully'
    })


# for login form
def login(request):
    if request.method=='GET':
        return render(request, 'login/login.html')

    else:
        return render(request, 'login/login.html', {
        'error_message': 'An error occured.'
    })


# for signing up
def signup(request):
    if request.method=='GET' :
        return render(request, 'login/signup.html')
    elif request.method=='POST' :
        pwd1=request.POST['pwd1']
        pwd2=request.POST['pwd2']
        email=request.POST['email']
        if pwd1!=pwd2 :
            return render(request, 'login/signup.html', {
                'error_message': "Password didn't match."
            })
        elif credentials.objects.filter(email=email):
            return render(request, 'login/signup.html',{
                'error_message': 'Email already registered. Try different one.'
            })
        else:
            name=request.POST['name']
            userpic=request.FILES['userpic']
            mbno=request.POST['mb_no']
            adhaarno=request.POST['adhaar_no']
            city=request.POST['city']
            fadhaar=request.FILES['fadhaar']
            badhaar=request.FILES['badhaar']
            gender=request.POST['gender']

            userpic.name=adhaarno+userpic.name
            fadhaar.name=adhaarno+fadhaar.name
            badhaar.name=adhaarno+badhaar.name

            user=credentials(name=name,pwd=pwd1,userpic=userpic,email=email,mbno=mbno,adhaarno=adhaarno,city=city,fadhaar=fadhaar,badhaar=badhaar,gender=gender)
            user.save()
            return render(request, 'login/login.html', {
                'error_message' : 'Account created successfully. Login to continue.'
            })
    return render(request,"login/login.html",{
        'error_message' : 'An error ocurred !!!'
    })


def loggedin(request):

    if request.method=='POST':

        email=request.POST['email']
        pwd=request.POST['pwd']
        
        if credentials.objects.filter(email=email, pwd=pwd) :
            user=get_object_or_404(credentials, email=email)
            properties=seller.objects.all()
            all=credentials.objects.all()
            return render(request, 'auction/loggedin.html',{
                'user': user,
                'properties' : properties,
                'all' : all,
            })
        else:
            return render(request, 'login/login.html',{
                'error_message': 'Invalid Credentials !!!',
            })
    return render(request, 'login/login.html', {
        'error_message' : 'An error occured'
    })

