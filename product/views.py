from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from product.serializers import ProductSerializer,CategorySerializer,ReviewSerializer,ProductImageSrialilzer
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin,ListModelMixin
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from product.models import Product,Category,Review,ImageModel
from django_filters.rest_framework import DjangoFilterBackend
from product.filter import ProductFilter
from rest_framework.filters import SearchFilter,OrderingFilter
from product.pagination import defaultPagination
from rest_framework.permissions import IsAdminUser,AllowAny
from api.permissions import IsAdminOrReadonly
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from drf_yasg.utils import swagger_auto_schema


class ProductViewSet(ModelViewSet):
    """ 
    API endpiont for managing products in the e-commerce store
        - Allows authenticated admin to create,update adn delete products
        - Allows users to browse and filter porduct 
        - Support searching by name, description and category
        - Support ordering by price and update_at 

    """
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class=ProductFilter
    search_fields= ['name','description','category__name']
    ordering_fields=['price']
    pagination_class=defaultPagination
    permission_classes=[IsAdminOrReadonly]

    @swagger_auto_schema(
        operation_summery="Retrive a list of product "
    )
    def list(self, request, *args, **kwargs):
        """ Retrive all the products """
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summery="Create a product by admin"
    )

    def create(self, request, *args, **kwargs):
        """ Only authenticated admin can create product """
        return super().create(request, *args, **kwargs)
class CategoryViewset(ModelViewSet):
    queryset=Category.objects.annotate(product_count=Count('products')).all()
    serializer_class=CategorySerializer





class ReviewViewSet(ModelViewSet):
    serializer_class=ReviewSerializer
    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs.get('product_pk'))
    def get_serializer_context(self):
        return {'product_id':self.kwargs.get('product_pk')}




class ProductImageViewSet(ModelViewSet):
    serializer_class=ProductImageSrialilzer
    permission_classes=[IsAdminOrReadonly]
    def get_queryset(self):
        return ImageModel.objects.filter(product_id=self.kwargs.get('product_pk'))
    
    def perform_create(self, serializer):
        serializer.save(product_id=self.kwargs.get('product_pk'))
# class ViewProduct(APIView):
#     def get(self,request):
#         product=Product.objects.select_related('category').all()
#         serializer=ProductSerializer(
#             product,many=True
#         )
#         return Response(serializer.data)
    
#     def post(self,request):
#         serailizer=ProductSerializer(data=request.data)
#         serailizer.is_valid(raise_exception=True)
#         serailizer.save()
#         return Response(serailizer.data,status=status.HTTP_201_CREATED)




    # def get_queryset(self):
    #     queryset=Product.objects.all()
    #     category_id=self.request.query_params.get('category_id')

    #     if category_id is not None:
    #         queryset=Product.objects.filter(category_id=category_id)
    #     return queryset
    # serializer_class=ProductSerializer

# class ProductList(ListCreateAPIView):
#     queryset=Product.objects.select_related('category').all()
#     serializer_class=ProductSerializer


# class ProductDetails(RetrieveUpdateDestroyAPIView):
#     queryset =Product.objects.all()
#     serializer_class=ProductSerializer
#     lookup_field='id'

# class ViewSpecificProduct(APIView):
#     def get(self,request,id):
#        product=get_object_or_404(Product,id=id) 
#        serializer=ProductSerializer(product)
#        return Response(serializer.data)
    
#     def put(self,request,id):
#         product=get_object_or_404(Product,id=id)
#         serializer=ProductSerializer(product,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def delete(self,request,id):
#         product=get_object_or_404(Product,id=id)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET','POST'])
# def view_product(request):
#     if request.method== 'GET':
#         product=Product.objects.select_related('category').all()
#         serializer=ProductSerializer(product,many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer=ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view()
# def view_category(request):
#     Categories=Category.objects.annotate(product_count=Count('products'))
#     serializer=CategorySerializer(Categories,many=True)
#     return Response(serializer.data)
 
# @api_view()
# def view_specific_category(request,pk):
#     category=get_object_or_404(Category,pk=pk)
#     serializer=CategorySerializer(category)
#     return Response(serializer.data)

     




# class ViewCategory(APIView):
#     def get(self,request):
#         Categories=Category.objects.annotate(product_count=Count('products'))
#         serializer=CategorySerializer(Categories,many=True)
#         return Response(serializer.data)    

#     def post(self,request):
#         serailizer=CategorySerializer(data=request.data)
#         serailizer.is_valid(raise_exception=True)
#         serailizer.save()
#         return Response(serailizer.data,status=status.HTTP_201_CREATED)
    


# class CategoryDetails(RetrieveUpdateDestroyAPIView):
#     queryset=Category.objects.annotate(product_count=Count('products')).all()
#     serializer_class=CategorySerializer
#     lookup_field='id'

# class ViewSpecificCategory(APIView):
#     def get(self,request,id):
#         category=get_object_or_404(Category.objects.annotate(product_count=Count('products')).all(),pk=id)
#         serializer=CategorySerializer(category)
#         return Response(serializer.data)
    
#     def put(self,request,id):
#         category=get_object_or_404(Category.objects.annotate(product_count=Count('products')).all(),pk=id)
#         serializer=CategorySerializer(category,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    

#     def delete(self,request,id):
#         category=get_object_or_404(Category.objects.annotate(product_count=Count('products')).all(),pk=id) 
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET','PUT','DELETE'])
# def view_Specific_products(request,id):
#     if request.method == 'GET':
#         product=get_object_or_404(Product,id=id)
#         serializer=ProductSerializer(product)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         product=get_object_or_404(Product,id=id)
#         serializer=ProductSerializer(product,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
    # if request.method =='DElETE':
        

