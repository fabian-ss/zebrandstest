from .models import User
from .serializers import UserSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return User.objects.filter(is_active = True)
        return User.objects.filter(id = pk,is_active = True).first()        

    def list(self,request):
        user_serializer = self.get_serializer(self.get_queryset(),many= True)
        if user_serializer and user_serializer.data != []:
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        return Response({'warning':'products not found'}, status=status.HTTP_400_BAD_REQUEST)
    
    def create(self,request):
        print("Create Request [USER]",request.data)
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()
            return Response({'message':'user created','data':user_serializer.data}, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, pk, *args, **kwargs):
        user = self.get_queryset().filter().first()
        if user:
            user.is_active = False
            user.save()
            return Response({'message':'removed user'}, status=status.HTTP_200_OK)
        return Response({'error':'user not found'}, status=status.HTTP_400_BAD_REQUEST)
    