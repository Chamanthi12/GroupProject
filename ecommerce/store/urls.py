from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.store, name="store"),
	path('clothsStore/', views.clothsStore, name="clothsStore"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

    path('update_item/', views.updateItem, name="update_Item"),
    path('process_order/', views.processOrder, name="process_order"),

]
