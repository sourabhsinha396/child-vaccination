from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions



@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def ping(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "APIs are working"})