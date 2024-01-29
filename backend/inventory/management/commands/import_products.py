from django.core.management.base import BaseCommand

from inventory.models import Product

from products import products


class Command(BaseCommand):
    help = "Import pre-defined products data into the database"

    def handle(self, *args, **kwargs):
        for product in products:
            Product.objects.create(**product)
        
        self.stdout.write(self.style.SUCCESS('Products Imported Successfully.'))