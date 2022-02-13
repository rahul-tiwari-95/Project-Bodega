import imp
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from backend.models import MetaUser
from backend.serializers import MetaUserSerializer



@csrf_exempt
def metauser_list(request):
    if request.method == 'GET':
        metauser = MetaUser.objects.all()
        serializer = MetaUserSerializer(metauser.data, many=True)
        return JsonResponse(serializer.data, safe=False)
    



#

