from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from apps.vaccination.models import Parent, Mother, Child, Vaccine, ChildVaccinated, MotherVaccinated
from .serializers import (ParentSearchSerializer, MotherSerializer, ChildSerializer, 
                MotherInfoSerializer, ChildInfoSerializer, VaccineSerializer,
                ChildVaccinatedSerializer, MotherVaccinatedSerializer,
                ParentCreateSerializer,MotherCreateSerializer,ChildCreateSerializer)


class IsMedicalStaff(permissions.BasePermission):
    """
    Permission to identify authorized medical staff.
    """

    def has_permission(self, request, view):
        message = 'Adding customers not allowed.'

        if request.user.profile.is_medical_staff:
            return True
        return False


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def ping(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "APIs are working"})


@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated, IsMedicalStaff))
def search_parent_by_aadhar(request):
    if request.method == 'POST':
        aadhar = request.data['aadhar']
        try:
            parent = Parent.objects.get(aadhar=aadhar)
            serializer = ParentSearchSerializer(parent, many=False)
            return Response(serializer.data)
        except Parent.DoesNotExist:
            return Response({"message": "Parent not found"})
    return Response("Enter aadhar number")
    

@api_view(['GET',])
@permission_classes((permissions.IsAuthenticated, IsMedicalStaff))
def get_mother_by_slug(request,slug):
    try:
        mother = Mother.objects.get(slug=slug)
        serializer = MotherInfoSerializer(mother)
        return Response(serializer.data)
    except Mother.DoesNotExist:
        return Response({"message": "Mother not found in our database"})


@api_view(['GET',])
@permission_classes((permissions.IsAuthenticated, IsMedicalStaff))
def get_child_by_slug(request,slug):
    try:
        child = Child.objects.get(slug=slug)
        serializer = ChildInfoSerializer(child)
        return Response(serializer.data)
    except Child.DoesNotExist:
        return Response({"message": "Child not found in our database"})

    
@api_view(['POST',])
@permission_classes((permissions.IsAuthenticated, IsMedicalStaff))
def add_parent(request):
    parent = ParentCreateSerializer(data=request.data)
    if parent.is_valid():
        parent.save()
        return Response({"message": "Parent's information added successfully", "data": parent.data})
    return Response(parent.errors)


@api_view(['POST',])
@permission_classes((permissions.IsAuthenticated, IsMedicalStaff))
def update_parent_info(request,slug):
    parent = get_object_or_404(Parent, slug=slug)
    parent_serialized = ParentCreateSerializer(instance=parent,data=request.data)
    if parent_serialized.is_valid():
        parent_serialized.save()
        return Response({"message": "Parent information updated successfully", "data": parent_serialized.data})
    return Response(parent_serialized.errors)


@api_view(['POST',])
@permission_classes((permissions.IsAuthenticated, IsMedicalStaff))
def add_mother(request):
    mother = MotherCreateSerializer(data=request.data)
    if mother.is_valid():
        mother.save()
        return Response({"message": "Mother's information added successfully", "data": mother.data})
    return Response(mother.errors)


@api_view(['POST',])
@permission_classes((permissions.IsAuthenticated, IsMedicalStaff))
def update_mother_info(request,slug):
    mother = get_object_or_404(Mother, slug=slug)
    mother_serialized = MotherCreateSerializer(instance=mother,data=request.data)
    if mother_serialized.is_valid():
        mother_serialized.save()
        return Response({"message": "Mother's information updated successfully", "data": mother_serialized.data})
    return Response(mother_serialized.errors)


@api_view(['POST',])
@permission_classes((permissions.IsAuthenticated, IsMedicalStaff))
def add_child(request):
    child = ChildCreateSerializer(data=request.data)
    if child.is_valid():
        child.save()
        return Response({"message": "Child's information added successfully", "data": child.data})
    return Response(child.errors)


@api_view(['POST',])
@permission_classes((permissions.IsAuthenticated, IsMedicalStaff))
def update_child_info(request,slug):
    child = get_object_or_404(Child, slug=slug)
    child_serialized = ChildCreateSerializer(instance=child,data=request.data)
    if child_serialized.is_valid():
        child_serialized.save()
        return Response({"message": "Child's information updated successfully", "data": child_serialized.data})
    return Response(child_serialized.errors)


@api_view(['GET',])
@permission_classes((permissions.AllowAny,))
def vaccine_list(request):
    vaccines = Vaccine.objects.all()
    serializer = VaccineSerializer(vaccines, many=True)
    return Response(serializer.data)


@api_view(['GET',])
@permission_classes((permissions.IsAuthenticated, IsMedicalStaff))
def is_child_vaccinated(request,slug,vaccine):
    try:
        child = Child.objects.get(slug=slug)
        child_vaccinated = child.child_vaccinated.filter(vaccine=vaccine).first()
        vaccination_details = ChildVaccinatedSerializer(child_vaccinated)
        if child_vaccinated:
            return Response({"message": "True","vaccination_details":vaccination_details.data})
        else:
            return Response({"message": "False"})
    except Child.DoesNotExist:
        return Response({"message": "Child not found in our database"})


@api_view(['POST',])
@permission_classes((permissions.IsAuthenticated, IsMedicalStaff))
def save_child_vaccination_info(request):
    child_vaccinated = ChildVaccinatedSerializer(data=request.data)
    if child_vaccinated.is_valid():
        child_vaccinated.save()
        return Response(child_vaccinated.data)
    return Response(child_vaccinated.errors)


@api_view(['GET',])
@permission_classes((permissions.IsAuthenticated, IsMedicalStaff))
def is_mother_vaccinated(request,slug,vaccine):
    try:
        mother = get_object_or_404(Mother, slug=slug)
        mother_vaccinated = mother.mother_vaccinated.filter(vaccine=vaccine).first()
        vaccination_details = MotherVaccinatedSerializer(mother_vaccinated)
        if mother_vaccinated:
            return Response({"message": "True","vaccination_details":vaccination_details.data})
        else:
            return Response({"message": "False"})
    except Mother.DoesNotExist:
        return Response({"message": "Mother not found in our database"})


@api_view(['POST',])
@permission_classes((permissions.IsAuthenticated, IsMedicalStaff))
def save_mother_vaccination_info(request):
    mother_vaccinated = MotherVaccinatedSerializer(data=request.data)
    if mother_vaccinated.is_valid():
        mother_vaccinated.save()
        return Response(mother_vaccinated.data)
    return Response(mother_vaccinated.errors)


@api_view(['POST',])
@permission_classes((permissions.IsAuthenticated, IsMedicalStaff))
def update_child_vaccination_info(request,id):
    child = ChildVaccinated.objects.get(id=id)
    child_vaccinated = ChildVaccinatedSerializer(instance=child, data=request.data)
    if child_vaccinated.is_valid():
        child_vaccinated.save()
        return Response(child_vaccinated.data)
    return Response(child_vaccinated.errors)


@api_view(['POST',])
@permission_classes((permissions.IsAuthenticated, IsMedicalStaff))
def update_mother_vaccination_info(request,id):
    mother = get_object_or_404(MotherVaccinated,id=id)
    mother_vaccinated = MotherVaccinatedSerializer(instance=mother, data=request.data)
    if mother_vaccinated.is_valid():
        mother_vaccinated.save()
        return Response(mother_vaccinated.data)
    return Response(mother_vaccinated.errors)


@api_view(['DELETE',])
@permission_classes((permissions.IsAuthenticated, IsMedicalStaff))
def delete_child_vaccination_info(request,id):
    child = get_object_or_404(ChildVaccinated,id=id)
    child.delete()
    return Response({"message": "Deleted"})


@api_view(['DELETE',])
@permission_classes((permissions.IsAuthenticated, IsMedicalStaff))
def delete_mother_vaccination_info(request,id):
    mother = get_object_or_404(MotherVaccinated,id=id)
    mother.delete()
    return Response({"message": "Deleted"})