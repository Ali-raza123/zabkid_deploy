from rest_framework import serializers
from .models import *


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"


class ChildrensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Childrens
        fields = "__all__"


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = "__all__"


class Online_RideSerializer(serializers.ModelSerializer):
    driver = DriverSerializer()
    children = ChildrensSerializer()
    parent = ParentSerializer()

    class Meta:
        model = Online_Ride
        fields = ['driver_id', 'children_id', 'driver', 'children', 'parent_id', 'parent', 'status']


class AddAssign_DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assign_driver
        fields = "__all__"


class Assign_DriverSerializer(serializers.ModelSerializer):
    driver = DriverSerializer()
    children = ChildrensSerializer()
    parent = ParentSerializer()

    class Meta:
        model = Assign_driver
        fields = ['id', 'driver_id', 'children_id', 'driver', 'children', 'parent_id', 'parent']


class Ride_historySerializer(serializers.ModelSerializer):
    children = ChildrensSerializer()

    class Meta:
        model = Ride_history
        fields = "__all__"


class Add_Ride_historySerializer(serializers.ModelSerializer):
    class Meta:
        model = Add_Ride_history
        fields = "__all__"


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = "__all__"


class ShiftsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shifts
        fields = "__all__"


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"
