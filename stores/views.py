from ast import Store
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from stores import models
from stores.forms import StoreItem, StoreItemForm
from stores.models import StoreItem 


def get_store_items(request: HttpRequest) -> HttpResponse:
    store_items: list[models.StoreItem] = list(models.StoreItem.objects.all())
    context = {
        "store_items": store_items,
    }
    return render(request, "store_item_list.html", context)

def create_store_item(request): # creating 
    form = StoreItem.object() # instance of a class 
    context = {"form": form}  
    POST = StoreItemForm.object(request.POST)
    return render (request, "create_page.html",context)