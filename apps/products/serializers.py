from .models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','sku','name','price','brand')
        read_only_fields = ('id','created_ad','is_active','counter')