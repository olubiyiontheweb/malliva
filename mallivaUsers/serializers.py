# middleware to handle user operations before saving in the database

from rest_framework import serializers
from .models import User, Permission, Role
from listings.models import Listing
from listings.serializers import ListingSerializer

# from customFields.serializers import AssociatedModelRelatedField


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class PermissionRelatedField(serializers.StringRelatedField):
    def to_representation(self, value):
        return PermissionSerializer(value).data

    def to_internal_value(self, data):
        return data


class RoleSerializer(serializers.ModelSerializer):
    permissions = PermissionRelatedField(many=True)

    class Meta:
        model = Role
        fields = "__all__"

    def create(self, validated_data):
        permissions = validated_data.pop("permissions", None)
        instance = self.Meta.model(**validated_data)
        instance.save()
        instance.permissions.add(*permissions)
        instance.save()
        return instance


class RoleRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return RoleSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)


class UserSerializer(serializers.ModelSerializer):
    # role = RoleRelatedField(many=False, queryset=Role.objects.all())
    # customfields = CustomFieldSerializer(many=True)

    class Meta:
        model = User

        # allow only selected inputs
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "profile_picture",
            "custom_fields",
            # "role",
            "terms_of_service_accepted",
        ]

        # Don't show passwords in API responses
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {"required": False},
        }

    def create(self, validated_data):

        # remove and return password from validated data
        password = validated_data.pop("password", None)

        user = self.Meta.model(**validated_data)

        if password is not None:
            user.set_password(password)

        if user.username is None:
            user.set_username

        user.save()
        return user

    def update(self, instance, validated_data):

        # remove and return password from validated data
        password = validated_data.pop("password", None)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.email = validated_data.get("email", instance.email)
        # instance.role = validated_data.get("role", instance.role)
        instance.profile_picture = validated_data.get(
            "profile_picture", instance.profile_picture
        )
        instance.terms_of_service_accepted = validated_data.get(
            "terms_of_service_accepted", instance.terms_of_service_accepted
        )

        if password is not None:
            instance.set_password(password)

        print(instance.get_fullname)

        instance.save()
        return instance
