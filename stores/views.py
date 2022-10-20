from ast import Store
from logging.config import valid_ident
from multiprocessing import context
from django.forms import Form
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from stores import models
from stores.forms import StoreItemForm
from stores.models import StoreItem 

def get_store_items(request: HttpRequest) -> HttpResponse:
    store_items: list[models.StoreItem] = list(models.StoreItem.objects.all())
    context = {
        "store_items": store_items,
    }
    return render(request, "store_item_list.html", context)

def create_store_item(request): # creating 
    form = StoreItemForm() # instance of a class 
    if request.method == "POST":
        #taking data
        form = StoreItemForm(request.POST) # retrive data 
        #checking validity
        if form.is_valid():
        #save
            form.save()
            return redirect("store-item-list")  # to save the value and go to item list page
    context = {"form": form}  
   
    return render (request, "create_store_item.html",context)

def update_store_item(request, item_id):
        store_item = StoreItem.objects.get(id=item_id) #fdetching id
        form = StoreItemForm(instance=store_item) #instance
        #when the user submit it will run
        if request.method == "POST":
            form = StoreItemForm(request.POST, instance=store_item)
            if form.is_valid():
                form.save()
                return redirect ("flight-list")
                
        POST = StoreItemForm(request.POST,instance=store_item)
        context = {"form": form, "store":item_id} 
        return render(request, "update_store_item.html", context)

def delete_store_item(request, item_id):
    store_item = StoreItem.objects.get(id=item_id)
    store_item.delete()
    return redirect ("store-item-list")
    
