from django.shortcuts import render, get_object_or_404
from django.http  import Http404, HttpResponse, HttpResponseRedirect

from login.models import credentials
from .models import seller
from home.models import complete, bidder

import random

# Create your views here.


def auction(request, cid):
    if request.method=='POST':
        return render(request, 'portal/auctionform.html',{
            'cid' : cid,
        })

def detail(request, cid):

    if request.method=='POST' :
        # taking random int for unique name of same property pics
        x=random.randint(1,1000)
        x=str(x)

        name=request.POST['name']
        category=request.POST['category']
        size=request.POST['size']
        address=request.POST['address']

        description=request.POST['description']
        city=request.POST['city']
        minprice=request.POST['minprice']
        deadline=request.POST['deadline']
        contact=request.POST['contact']

        document=request.FILES['document']    
        pic1=request.FILES['pic1']
        pic2=request.FILES['pic2']
        pic3=request.FILES['pic3']
        pic4=request.FILES['pic4']

        document.name=x+document.name
        pic1.name=x+pic1.name
        pic2.name=x+pic2.name
        pic3.name=x+pic3.name
        pic4.name=x+pic4.name

        property=seller(name=name, category=category, size=size, address=address, city=city, minamnt=minprice, date=deadline,
                         description=description, document=document, pic1=pic1, pic2=pic2, pic3=pic3, pic4=pic4, contact=contact, cid_id=cid)
        property.save()
        #return render(request, 'portal/loggedin.html',{
            #'error_message' : 'Auction created successfuly !!!'
            #})
        user=get_object_or_404(credentials, id=cid)
        properties=seller.objects.all()
        all=credentials.objects.all()
        return render(request, 'portal/loggedin.html',{
            'user': user,
            'properties' : properties,
            'all' : all,
            'error_message' : 'auction created successfully.'
        })
    return render(request, 'login/login.html', {
        'error_message' : 'An error ocurred.'
    })


def particular(request, bid):

    cid=request.POST['cid']

    buyer=get_object_or_404(credentials, id=cid)
    item=get_object_or_404(seller, id=bid)
    owner=get_object_or_404(credentials, id=item.cid_id)

    return render(request, 'portal/detail.html',{
        'buyer' : buyer,
        'owner' : owner,
        'item' : item,
    })

def bid(request, bid):
    if request.method=='POST':

        amnt=request.POST['bidamnt']
        amnt=int(amnt)
        buy=request.POST['buyer']
        check_amnt=get_object_or_404(seller, id=bid)
        if check_amnt.minamnt > amnt :

            buyer=get_object_or_404(credentials, id=buy)
            item=get_object_or_404(seller, id=bid)
            owner=get_object_or_404(credentials, id=item.cid_id)
            
            return render(request, 'portal/detail.html',{
                'buyer' : buyer,
                'owner' : owner,
                'item' : item,
                "error_message" : "enter amount greater than minamnt"
            })

        user= bidder(amnt=amnt, bid_id=bid, cid_id=buy)
        user.save()

        owner=get_object_or_404(credentials, id=buy)
        properties=seller.objects.all()

        return render(request, 'portal/loggedin.html',{
            'user' : owner,
            'properties' : properties,
            'error_message' : "Amount Bidded Successfully"
        })

    return HttpResponse("An error ocurred ")











