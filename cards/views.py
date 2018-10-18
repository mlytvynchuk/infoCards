from django.shortcuts import render
from .models import Card,Tag
# Create your views here.

def home(request):
    cards = Card.objects.all()
    return render(request,'cards/home.html',{'cards': cards})

def card_details(request,slug):
    card = Card.objects.get(slug__iexact=slug)
    tags = Tag.objects.all()
    return render(request,'cards/card-detail.html',context={'card':card})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request,'tags/tags_list.html',context={'tags':tags})

