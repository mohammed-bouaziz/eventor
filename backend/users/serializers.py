from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'first_name', 'last_name', 'email', 'profile_img', 'is_superadmin', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            profile_img=validated_data.get('profile_img'),
            is_superadmin=validated_data.get('is_superadmin', False),
            username=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user