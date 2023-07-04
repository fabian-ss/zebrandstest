from django.db import models
import uuid

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    is_active = models.BooleanField(default=True)
    brand = models.TextField(max_length=300)
    counter = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'