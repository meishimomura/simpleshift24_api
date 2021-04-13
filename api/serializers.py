from rest_framework import serializers
from .models import Staff,Shift,Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs = {'password':{'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user_profile', 'img']
        extra_kwargs = {'user_profile': {'read_only': True}}


class StaffSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    class Meta:
        model = Staff
        fields = ['id', 'owner', 'staff_name', 'is_active', 'created_at', 'updated_at']
        extra_kwargs = {'owner': {'read_only': True}}


class ShiftSerializer(serializers.ModelSerializer):
    shift_date = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])
    shift_start = serializers.TimeField(format="%H:%M", input_formats=["%H:%M"])
    shift_end = serializers.TimeField(format="%H:%M", input_formats=["%H:%M"])
    staff_name = serializers.ReadOnlyField(source='staff.staff_name', read_only=True)
    staff_is_active = serializers.ReadOnlyField(source='staff.is_active', read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    class Meta:
        model = Shift
        fields = ['id', 'owner', 'shift_date', 'shift_start', 'shift_end', 'staff', 'staff_name', 'staff_is_active', 'created_at', 'updated_at']
        extra_kwargs = {'owner': {'read_only': True}}