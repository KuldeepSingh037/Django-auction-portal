from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from portal.models import seller
from login.models import credentials
from .models import complete, bidder
from datetime import date

# Create your views here.

def home(request):

    dateToday=date.today()
    todays_properties = seller.objects.raw('SELECT * from seller WHERE date < %s', [dateToday])
    for item in todays_properties:
        max=0
        buyers= bidder.objects.filter(bid_id=item.id)
        for buyer in buyers:
            if buyer.amnt > max :
                max = buyer.amnt
                id=buyer.cid_id
            buyer.delete()

        user=complete(seller=item.cid_id, name=item.name, category=item.category, size=item.size, address=item.address, city=item.city, bidamnt=max, date=item.date, description=item.description, contact=item.contact, document=item.document, pic1=item.pic1, pic2=item.pic2, pic3=item.pic3, pic4=item.pic4)
        user.save()

        item.delete()

    completed=complete.objects.all()
    return render(request, 'home/home_page.html', {
        'sold_properties' : completed,
    })


# when search button of home page is clicked
def search(request):
    return render(request, 'login/login.html', {
        "error_message" : 'Login to continue !!!'
    })

def sold_info(request, id):
    completed_item=get_object_or_404(complete, id=id)
    buyer_person=get_object_or_404(credentials, id=completed_item.buyer)
    seller_person=get_object_or_404(credentials, id=completed_item.seller)

    return render(request, 'home/sold_info.html', {
        'completed_item' : completed_item,
        'buyer_person' : buyer_person,
        'seller_person' : seller_person,
    })

