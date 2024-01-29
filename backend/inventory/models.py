from django.db import models


# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(
        "user.User", related_name="products", on_delete=models.SET_NULL, null=True
    )
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    brand = models.CharField(max_length=200, null=True, blank=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    num_reviews = models.IntegerField(default=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    count_in_stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(
        "Product", related_name="product_reviews", on_delete=models.SET_NULL, null=True
    )
    user = models.ForeignKey(
        "user.User", related_name="reviews", on_delete=models.SET_NULL, null=True
    )
    name = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    review = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.rating
