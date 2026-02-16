from rest_framework import serializers
from product.models import Category,Product,Review,ImageModel
from decimal import Decimal

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name','description','product_count']

    product_count=serializers.IntegerField(read_only=True)

# class ProductSerializer(serializers.Serializer):
#     id=serializers.IntegerField()
#     name=serializers.CharField()
#     Unit_price=serializers.DecimalField(max_digits=10,decimal_places=2,source='price')
    

#     # category=serializers.PrimaryKeyRelatedField(
#     #     queryset=Category.objects.all()
#     # category=serializers.StringRelatedField(
       
#     # )
#     # category=CategorySerializer()
#     category=serializers.HyperlinkedRelatedField(
#         queryset=Category.objects.all(),
#         view_name='category_specific_list'
#     )

class ProductImageSrialilzer(serializers.ModelSerializer):
    image=serializers.ImageField()
    class Meta:
        model=ImageModel
        fields=['id','image']

class ProductSerializer(serializers.ModelSerializer):
    images=ProductImageSrialilzer(many=True,read_only=True)
    class Meta:
        model=Product
        fields=['id','name','description','price','stock',
                'created_at','update_at','category','price_with_tax','images']


    price_with_tax=serializers.SerializerMethodField(method_name='calculate_tax')
    def calculate_tax(self,product):
        return round(product.price*Decimal(1.1),2)
    
    def validate_price(self,price):
        if price <0:
            raise serializers.ValidationError('Price could not be negative ')
        return price
    


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=['id','user','product','ratings','comment']
        read_only_fields=['ratings','comment']

    def create(self,validated_data):
        product_id=self.context['product_id']
        return Review.objects.create(product_id=product_id,**validated_data)

