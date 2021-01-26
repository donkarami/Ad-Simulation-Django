from django.urls import path
from advertiser_management import views

app_name = 'advertiser_management'
urlpatterns = [
    path('', views.ads, name='ads'),
    path('create-ad/', views.create_ad, name='create_ad'),
    path('click/<int:ad_id>/', views.click, name='click')
]
