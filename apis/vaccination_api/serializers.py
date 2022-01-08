from rest_framework import serializers

from apps.vaccination.models import Parent, Child, Mother


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ('slug','name', 'gender')


class MotherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mother 
        fields = ("slug","name","last_delivery_date")

class ParentSearchSerializer(serializers.ModelSerializer):
    child = ChildSerializer(many=True, read_only=True)
    mother = MotherSerializer(many=True, read_only=True)
    class Meta:
        model = Parent
        fields = ("slug","name","phone","child","mother")
    
