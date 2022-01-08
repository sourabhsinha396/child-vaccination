from rest_framework import serializers

from apps.vaccination.models import Parent


class ParentSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ("slug","name","phone")

    
