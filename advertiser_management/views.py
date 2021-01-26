from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("this is index view")


def create_ad(request):
    return HttpResponse("this is create_ad view")


def click(request, ad_id):
    return HttpResponse("this is click %s view" % ad_id)
