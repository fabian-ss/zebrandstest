from .models import Product
from .serializers import ProductSerializer
from ..users.models import User
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .utils import Util


class ProductViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ('create','update', 'destroy'):
            self.permission_classes = [IsAuthenticated,]
        return super(self.__class__, self).get_permissions()

    def get_queryset(self,pk=None):
        if pk is None:
            return Product.objects.filter(is_active = True)
        print("This is a pk",pk)
        return Product.objects.filter(id = pk,is_active = True).first()        

    def list(self,request):
        print("Request",)
        product_serializer = self.get_serializer(self.get_queryset(),many= True)
        if product_serializer and product_serializer.data != []:
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response({'warning':'products not found'}, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        product = self.get_queryset(pk)
        product_serializer = self.get_serializer(product)
        if self.request.user.is_authenticated == False:
            product.counter += 1
            product.save()
            return Response(product_serializer.data,status=status.HTTP_200_OK)
        return Response({'warning':'product not found'}, status=status.HTTP_400_BAD_REQUEST)        

    def create(self,request):
        product_serializer = self.serializer_class(data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response({'message':'Product created','data':product_serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'error':'Cant create the producto'}, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        user = User.objects.filter(is_active = True, is_admin=True)

        if instance.sku != request.data['sku'] or instance.name != request.data['name'] or instance.price != request.data['price'] or instance.brand != request.data['brand']:
            listEmailtosend= []
            for i in user:
                listEmailtosend.append(i.email)

            data = {
            'subject':'Updated product' ,
            'email_body': 
            "Data before the update \n" + 
            "\nsku:"  +str(instance.sku)+
            "\nname:" +str(instance.name)+
            "\nprice:"+str(instance.price)+
            "\nbror:"+str(instance.brand)+ 

            "\n\nData after the update \n\nsku:"+
            str(request.data['sku'])+
            "\nname:"+
            str(request.data['name'])+
            "\nprice:"+
            str(request.data['price'])+
            "\nbrand:"+
            str(request.data['brand']),
            'from_email': "acadynedev@gmail.com",
            'to_email':listEmailtosend
            }
            Util.send_email(data)        
            self.perform_update(serializer)
        return Response(serializer.data)
    
    
    def destroy(self, request, pk=None):
        instance = self.get_object()
        if instance:
            instance.is_active = False
            user = User.objects.filter(is_admin=True)
            listEmailtosend= []
            for i in user:
                listEmailtosend.append(i.email)            
            data = {
            'subject':'Deleted product' ,
            'email_body': f"Product name: {instance.name}, with the id: {instance.id} was deleted",
            'from_email': "acadynedev@gmail.com",
            'to_email':listEmailtosend
            }
            Util.send_email(data)                
            instance.save()
            return Response({'message':'removed product'}, status=status.HTTP_200_OK)
        return Response({'warning':'The id does not exist or cannot be deleted'}, status=status.HTTP_400_BAD_REQUEST)

    