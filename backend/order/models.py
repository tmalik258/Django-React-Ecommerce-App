from django.db import models
from django.conf import settings
# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(
        "user.User", related_name="orders", on_delete=models.SET_NULL, null=True
    )
    payment_method = models.CharField(max_length=200, null=True, blank=True)
    tax_price = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    shipping_price = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    total_price = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    is_paid = models.BooleanField(default=False)
    paid_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    is_delivered = models.BooleanField(default=False)
    delivered_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.created_at


class OrderItem(models.Model):
    product = models.ForeignKey(
        "inventory.Product", related_name="order_items", on_delete=models.SET_NULL, null=True
    )
    user = models.ForeignKey(
        "user.User", related_name="order_items", on_delete=models.SET_NULL, null=True
    )
    qty = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'
        constraints = [
            models.CheckConstraint(check=models.Q(qty__gt=0), name="product_quantity_positive"),
            ]

    @property
    def get_total(self):
        """Calculate the total price of a single item"""
        return self.product.price * self.qty

    def __str__(self):
        return self.product.name


class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    shipping_price = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)

    class Meta:
        verbose_name = "Shipping Address"
        verbose_name_plural = "Shipping Addresses"

    def __str__(self):
        return self.address
