from django.urls import path,include
from product import views

urlpatterns = [
    path('',views.ViewCategory.as_view(),name='category_list'),
    path('<int:id>/',views.CategoryDetails.as_view(),name='category_specific_list')
]
