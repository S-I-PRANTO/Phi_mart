from django.urls import path,include

from product.views import ProductViewSet,CategoryViewset,ReviewViewSet,ProductImageViewSet
from rest_framework_nested import routers
from order.views import CartViewSet,CartItemViewSet,Orderviewset
router=routers.DefaultRouter()
router.register('products',ProductViewSet,basename='products')
router.register('category',CategoryViewset)
router.register('carts',CartViewSet,basename='carts')
router.register('orders',Orderviewset,basename='orders')

cart_router=routers.NestedDefaultRouter(router,'carts',lookup='cart')
cart_router.register('items',CartItemViewSet,basename='cart_item')

product_router=routers.NestedDefaultRouter(router,'products',lookup='product')
product_router.register('reviews',ReviewViewSet,basename='product-review')
product_router.register('images',ProductImageViewSet,basename='product_image')




urlpatterns =[

    path('',include(router.urls)),
    path('',include(product_router.urls)),
    path('',include(cart_router.urls)),
    path("auth/",include('djoser.urls')),
    path("auth/",include('djoser.urls.jwt')),
    
] 

# urlpatterns = [
#     path('/',include('product.Product_urls')),
#     path('/',include('product.Category_urls'))
# ]
