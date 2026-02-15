from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator,MaxValueValidator
from product.validators import validate_file_size
class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.name
    


class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products' )
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)


    class Meta:
        ordering=['-id',]
    
    def __str__(self):
        return self.name
    
class ImageModel(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images')
    image=models.ImageField(upload_to='product/images/',validators=[validate_file_size])

class Review(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    # name=models.CharField(m(ax_length=255)
    ratings=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    comment=models.TextField()
    Created_at=models.DateTimeField(auto_now_add=True)
    Update_at=models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"Review by {self.user.first_name} on {self.product.name} "


