from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('id','email','name','password','confirm_password')
        extra_kwargs = {
            'password':{'write_only':True}
        }   

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError("Passwords doesnt match")
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)