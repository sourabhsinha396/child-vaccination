from rest_framework import serializers

from apps.vaccination.models import Parent, Child, Mother, Vaccine, ChildVaccinated, MotherVaccinated


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
    


class MotherInfoSerializer(serializers.ModelSerializer):
    child = ChildSerializer(source="parent.child",many=True, read_only=True)
    class Meta:
        model = Mother 
        fields = ("slug","name","last_delivery_date","parent","child")


class ChildInfoSerializer(serializers.ModelSerializer):
    mother = MotherSerializer(read_only=True)
    class Meta:
        model = Child
        fields = ("slug","name","blood_group","gender","parent","mother","date_of_birth","place_of_delivery","remarks")


class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Vaccine
        fields = ("id","name","slug","designated_age","for_child","for_mother","extra_info")


class ChildVaccinatedSerializer(serializers.ModelSerializer):
    class Meta:
        model =  ChildVaccinated
        fields = ("id","child","vaccine","date","vaccinator","extra_info")


class MotherVaccinatedSerializer(serializers.ModelSerializer):
    class Meta:
        model =  MotherVaccinated
        fields = ("id","mother","vaccine","date","vaccinator","extra_info")
