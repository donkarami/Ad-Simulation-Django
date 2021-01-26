from django.urls import path
from advertiser_management import views
from advertiser_management.views import CreateAdView

app_name = 'advertiser_management'
urlpatterns = [
    path('', views.ads, name='ads'),
    path('create_ad/', CreateAdView.as_view(), name='create_ad'),
    path('click/<int:ad_id>/', views.click, name='click'),
]
