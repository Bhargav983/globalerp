from django.db import models

class Product(models.Model):
    barcode = models.CharField(max_length=100)
    product_name = models.CharField(max_length=200)
    product_company = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField()
    stock_quantity = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    sales_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        # You manually list each field you want to include in the string
        return f"Product Name: {self.product_name}, Company: {self.product_company}, Category: {self.category}"
