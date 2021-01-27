from django.db import models

# Create your models here.
from django.forms import ModelForm, forms
from django.urls import reverse


class BaseAdvertising(models.Model):
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Advertiser(BaseAdvertising):
    name = models.CharField(max_length=200)

    def inc_clicks(self):
        self.clicks += 1
        self.save()
        return

    def inc_views(self):
        self.views += 1
        self.save()
        return

    def __str__(self):
        return self.name


class Ad(BaseAdvertising):
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ads/')
    link = models.URLField()

    def inc_clicks(self):
        self.clicks += 1
        self.save()
        self.advertiser.inc_clicks()
        return

    def inc_views(self):
        self.views += 1
        self.save()
        self.advertiser.inc_views()
        return

    def get_absolute_url(self):
        return reverse('advertiser_management:ads')


class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ('advertiser', 'title', 'image', 'link')
