from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView

from advertiser_management.models import Advertiser, Ad, AdForm


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


class CreateAdView(CreateView):
    model = Ad
    template_name = 'advertiser_management/create_ad.html'
    fields = ['advertiser', 'title', 'image', 'link']


def click(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)
    ad.inc_clicks()
    ad.save()
    return redirect(ad.link)
