from django.db import models

# Create your models here.


class Products(models.Model):

    def __str__(self):
        return self.product_name

    product_name = models.CharField('Product Name', max_length=200)
    product_category = models.CharField('Product Category', max_length=200)
    product_description = models.TextField("Product Description")
    product_price = models.FloatField('Product Price')
    product_image = models.CharField('Image', max_length=500)
