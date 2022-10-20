"""bakery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from stores.views import get_store_items, create_store_item
from stores.views import update_store_item, delete_store_item 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("items/", get_store_items, name="store-item-list"),
    path("stores/add/", create_store_item ,name="create-store-item"), 
    path("stores/edit/<int:item_id>/", update_store_item ,name="update-store-item"),
    path("stores/delete/<int:item_id>",delete_store_item, name="delete-store-item")

]
