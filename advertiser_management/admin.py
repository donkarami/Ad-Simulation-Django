from django.contrib import admin

# Register your models here.
from advertiser_management.models import Advertiser, Ad

admin.site.register(Advertiser)
admin.site.register(Ad)
