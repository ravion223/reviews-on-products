from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.DecimalField(decimal_places = 2, max_digits = 10)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ["price"]
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = "reviews")
    
    author = models.CharField(max_length = 63)
    text = models.TextField()
    rating = models.IntegerField()

    def __str__(self) -> str:
        return f"review on {self.product}"
    
    class Meta:
        ordering = ["-rating"]
        verbose_name = "Review"
        verbose_name_plural = "Reviews"