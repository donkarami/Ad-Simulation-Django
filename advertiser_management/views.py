from django.http import HttpResponse
from django.shortcuts import render
from advertiser_management.models import Advertiser


# Create your views here.


def ads(request):
    advertisers = Advertiser.objects.order_by('name')
    for advertiser in advertisers:
        for ad in advertiser.ad_set.all():
            ad.inc_views()
    context = {
        'advertisers': advertisers
    }
    return render(request, 'advertiser_management/ads.html', context)


def create_ad(request):
    return HttpResponse("this is create_ad view")


def click(request, ad_id):
    return HttpResponse("this is click %s view" % ad_id)
