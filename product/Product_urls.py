from django.urls import path,include
from product import views

urlpatterns = [
    path('',views.ProductList.as_view(),name='product'),
    path('<int:id>/',views.ProductDetails.as_view(),name='product_list'),
 
]

