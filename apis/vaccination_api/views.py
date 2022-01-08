from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from apps.vaccination.models import Parent, Mother, Child
from .serializers import (ParentSearchSerializer, MotherSerializer, ChildSerializer, 
                MotherInfoSerializer, ChildInfoSerializer)


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
    

@csrf_exempt
@api_view(['GET',])
@permission_classes((permissions.IsAuthenticated, IsMedicalStaff))
def get_mother_by_slug(request,slug):
    try:
        mother = Mother.objects.get(slug=slug)
        serializer = MotherInfoSerializer(mother)
        return Response(serializer.data)
    except Mother.DoesNotExist:
        return Response({"message": "Mother not found in our database"})


@csrf_exempt
@api_view(['GET',])
@permission_classes((permissions.IsAuthenticated, IsMedicalStaff))
def get_child_by_slug(request,slug):
    try:
        child = Child.objects.get(slug=slug)
        serializer = ChildInfoSerializer(child)
        return Response(serializer.data)
    except Child.DoesNotExist:
        return Response({"message": "Child not found in our database"})

