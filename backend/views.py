
from dataclasses import fields
from locale import currency
from tempfile import TemporaryFile
from rest_framework import status, generics, mixins, request, viewsets

from rest_framework.decorators import api_view
from rest_framework.views import exception_handler
from django.http import HttpRequest, HttpResponse, JsonResponse

from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response
import datetime
from django.utils import timezone
from .forms import UserAddressFormSet
import requests
from rest_framework.request import Request
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.conf import settings
import stripe
import json




from backend.models import *
from backend.serializers import *






#HTML files for Bodega Landing Page
def home_page(request):
    metausers = message_hashkey_generator()
    return render(request, 'backend/index.html', {'metausers': metausers})

def landing_page(request):
    metausers = MetaUser.objects.all()
    time = timezone.now()
    kanye = requests.get('https://api.kanye.rest')
    kanye = kanye.text
    return render(request, 'backend/landingpage.html', {'metausers': metausers, 'time':time, 'kanye': kanye})

def filter_spam(request):
    return render(request, 'backend/filter-non-hackers.html')

def about_us(request):
    return render(request, 'backend/aboutbodega.html')

def contact_us(request):
    return render(request, 'backend/contact_us.html')




#MetaUser Generic Views  

class MetaUserList(generics.ListCreateAPIView):
    queryset = MetaUser.objects.all()
    serializer_class = MetaUserSerializer

#@csrf_exempt
class MetaUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetaUser.objects.all()
    serializer_class = MetaUserSerializer

#MetaUser Auth Generic Views
class MetaUserAuth(generics.ListCreateAPIView):
    queryset = MetaUser.objects.all()
    serializer_class = MetaUserAuthSerializer

# @csrf_exempt
# def MetaUserAuthHashkey(request):
#     #GET,PUT,DELETE request for metauser{id}
    
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = MetaUserLoginSerializer(data=data)
#         if serializer.is_valid():
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors)

@api_view(['POST'])    
def metauserauth(request, pk):
    instance = MetaUser.objects.get(meta_username=pk)
    instanceID = str(instance.id)
    metausercredentials = "ID: " + instanceID + " " + " meta_username: " + instance.meta_username
    serializer = MetaUserAuthSerializer(instance)
    #print(request.data['passcode'])
    if instance.passcode == request.data['passcode'] and instance.public_hashkey == request.data['public_hashkey']:
        print("Authentication successful")
        return Response(serializer.data,status=200)
    else:
        print("Authentication failed")
        return Response(data='Authentication Failed',status=404)

#For searching metauser by their metausername 
@api_view(['POST'])
def searchMetaUserByName(request):
    try :
        instance = MetaUser.objects.get(meta_username=request.data['meta_username'])
        serializer = MetaUserSerializer(instance)
        return Response(serializer.data, status=200)


    except MetaUser.DoesNotExist:
        return Response(status=404, data= request.data['meta_username']+ ' MetaUser not found.')



@csrf_exempt
def metauser_detail(request, pk):
    #GET,PUT,DELETE request for metauser{id}
    try:
        metauser = MetaUser.objects.get(pk=pk)
    except MetaUser.DoesNotExist:
        return JsonResponse(status=404)

    
    if request.method == 'GET':
        serializer = MetaUserSerializer(metauser)
        return JsonResponse(serializer.data)

    
    elif request.method == 'PUT':
        serializer = MetaUserSerializer(metauser, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        metauser.delete()
        return HttpResponse(status=204)




#Level Views
@csrf_exempt
def level_list(request):
    #GET, POST request for Level
    if request.method == 'GET':
        level = Level.objects.all()
        serializer = LevelSerializer(level, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LevelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JSONParser(serializer.errors, status=400)



@csrf_exempt
def level_detail(request, pk):
    #GET, PUT, DELETE request for level{id}
    try:
        level = Level.objects.get(pk=pk)
    except Level.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        serializer = LevelSerializer(level)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        serializer = LevelSerializer(level, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        level.delete()
        return HttpResponse(status=204)




#BLA Views
@csrf_exempt
def blascore_list(request):
    #GET, POST request for BLAScore
    if request.method == 'GET':
        base_line_analysis = BLAScore.objects.all()
        serializer = BLASerializer(base_line_analysis, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BLASerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JSONParser(serializer.errors, status=400)



@csrf_exempt
def blascore_detail(request, pk):
    #GET, PUT, DELETE request for  blascore{id}
    try:
        base_line_analysis = BLAScore.objects.get(pk=pk)
    except BLAScore.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        serializer = BLASerializer(base_line_analysis)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BLASerializer(base_line_analysis, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        base_line_analysis.delete()
        return HttpResponse(status=204)




#Sentino Item Proximity Model
@csrf_exempt
def sentino_item_proximity_list(request):
    #GET, POST request for sentino_item_proximity model
    if request.method == 'GET':
        sentino_item_proximity = SentinoItemProximity.objects.all()
        serializer = SentinoItemProximitySerializer(sentino_item_proximity, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SentinoItemProximitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JSONParser(serializer.errors, status=400)


@csrf_exempt
def sentino_item_proximity_detail(request, pk):
    #GET, PUT, DELETE request for  sentino_item_proximity{id}
    try:
        sentino_item_proximity = SentinoItemProximity.objects.get(pk=pk)
    except SentinoItemProximity.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        serializer = SentinoItemProximitySerializer(sentino_item_proximity)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SentinoItemProximitySerializer(sentino_item_proximity, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        sentino_item_proximity.delete()
        return HttpResponse(status=204)





#Sentino Item Projection Model
@csrf_exempt
def sentino_item_projection_list(request):
    #GET, POST request for sentino_item_projection model
    if request.method == 'GET':
        sentino_item_projection = SentinoItemProjection.objects.all()
        serializer = SentinoItemProjectionSerializer(sentino_item_projection, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SentinoItemProjectionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JSONParser(serializer.errors, status=400)


@csrf_exempt
def sentino_item_projection_detail(request, pk):
    #GET, PUT, DELETE request for  sentino_item_projection{id}
    try:
        sentino_item_projection = SentinoItemProjection.objects.get(pk=pk)
    except SentinoItemProjection.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        serializer = SentinoItemProjectionSerializer(sentino_item_projection)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SentinoItemProjectionSerializer(sentino_item_projection, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        sentino_item_projection.delete()
        return HttpResponse(status=204)





#Sentino Item Classification Model
@csrf_exempt
def sentino_item_classification_list(request):
    #GET, POST request for sentino_item_classification model
    if request.method == 'GET':
        sentino_item_classification = SentinoItemClassification.objects.all()
        serializer = SentinoItemClassificationSerializer(sentino_item_classification, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SentinoItemClassificationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JSONParser(serializer.errors, status=400)


@csrf_exempt
def sentino_item_classification_detail(request, pk):
    #GET, PUT, DELETE request for  sentino_item_classification{id}
    try:
        sentino_item_classification = SentinoItemClassification.objects.get(pk=pk)
    except SentinoItemClassification.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        serializer = SentinoItemClassificationSerializer(sentino_item_classification)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SentinoItemClassificationSerializer(sentino_item_classification, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        sentino_item_classification.delete()
        return HttpResponse(status=204)





#Sentino  Inventory Model
@csrf_exempt
def sentino_inventory_list(request):
    #GET, POST request for sentino_inventory model
    if request.method == 'GET':
        sentino_inventory = SentinoInventory.objects.all()
        serializer = SentinoInventorySerializer(sentino_inventory, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SentinoInventorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JSONParser(serializer.errors, status=400)

@csrf_exempt
def sentino_inventory_detail(request, pk):
    #GET, PUT, DELETE request for  sentino_inventory{id}
    try:
        sentino_inventory = SentinoInventory.objects.get(pk=pk)
    except SentinoInventory.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        serializer = SentinoInventorySerializer(sentino_inventory)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SentinoInventorySerializer(sentino_inventory, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        sentino_inventory.delete()
        return HttpResponse(status=204)




#Sentino Description Model
@csrf_exempt
def sentino_description_list(request):
    #GET, POST request for sentino_description model
    if request.method == 'GET':
        sentino_description = SentinoSelfDescription.objects.all()
        serializer = SentinoDescriptionSerializer(sentino_description, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SentinoDescriptionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JSONParser(serializer.errors, status=400)


@csrf_exempt
def sentino_description_detail(request, pk):
    #GET, PUT, DELETE request for  sentino_description{id}
    try:
        sentino_description = SentinoSelfDescription.objects.get(pk=pk)
    except SentinoSelfDescription.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        serializer = SentinoDescriptionSerializer(sentino_description)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SentinoDescriptionSerializer(sentino_description, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        sentino_description.delete()
        return HttpResponse(status=204)


#Sentino Profile Model
@csrf_exempt
def sentino_profile_list(request):
    #GET, POST request for sentino_profile model
    if request.method == 'GET':
        sentino_profile = SentinoProfile.objects.all()
        serializer = SentinoProfileSerializer(sentino_profile, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SentinoProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JSONParser(serializer.errors, status=400)


@csrf_exempt
def sentino_profile_detail(request, pk):
    #GET, PUT, DELETE request for  sentino_profile{id}
    try:
        sentino_profile = SentinoProfile.objects.get(pk=pk)
    except SentinoProfile.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        serializer = SentinoProfileSerializer(sentino_profile)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SentinoProfileSerializer(sentino_profile, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        sentino_profile.delete()
        return HttpResponse(status=204)



#Bodega Vision Model
@csrf_exempt
def bodega_vision_list(request):
    #GET, POST request for bodega_vision model
    if request.method == 'GET':
        bodega_vision = BodegaVision.objects.all()
        serializer = BodegaVisionSerializer(bodega_vision, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BodegaVisionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JSONParser(serializer.errors, status=400)


@csrf_exempt
def bodega_vision_detail(request, pk):
    #GET, PUT, DELETE request for  bodega_vision{id}
    try:
        bodega_vision = BodegaVision.objects.get(pk=pk)
    except BodegaVision.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        serializer = BodegaVisionSerializer(bodega_vision)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BodegaVisionSerializer(bodega_vision, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        bodega_vision.delete()
        return HttpResponse(status=204)




#Bodega Face Model
@csrf_exempt
def bodega_face_list(request):
    #GET, POST request for bodega_face model
    if request.method == 'GET':
        bodega_face = BodegaFace.objects.all()
        serializer = BodegaFaceSerializer(bodega_face, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BodegaFaceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JSONParser(serializer.errors, status=400)


@csrf_exempt
def bodega_face_detail(request, pk):
    #GET, PUT, DELETE request for  bodega_face{id}
    try:
        bodega_face = BodegaFace.objects.get(pk=pk)
    except BodegaFace.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        serializer = BodegaFaceSerializer(bodega_face)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BodegaFaceSerializer(bodega_face, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        bodega_face.delete()
        return HttpResponse(status=204)





#Bodega Personalizer Model
@csrf_exempt
def bodega_personalizer_list(request):
    #GET, POST request for bodega_personalizer model
    if request.method == 'GET':
        bodega_personalizer = BodegaPersonalizer.objects.all()
        serializer = BodegaPersonalizerSerializer(bodega_personalizer, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BodegaPersonalizerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JSONParser(serializer.errors, status=400)

@csrf_exempt
def bodega_personalizer_detail(request, pk):
    #GET, PUT, DELETE request for  bodega_personalizer{id}
    try:
        bodega_personalizer = BodegaPersonalizer.objects.get(pk=pk)
    except BodegaPersonalizer.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        serializer = BodegaPersonalizerSerializer(bodega_personalizer)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BodegaPersonalizerSerializer(bodega_personalizer, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        bodega_personalizer.delete()
        return HttpResponse(status=204)





#Bodega Cognitive Item Model
@csrf_exempt
def bodega_item_list(request):
    #GET, POST request for bodega_item model
    if request.method == 'GET':
        bodega_item = BodegaCognitiveItem.objects.all()
        serializer = BodegaCognitiveItemSerializer(bodega_item, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BodegaCognitiveItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JSONParser(serializer.errors, status=400)

@csrf_exempt
def bodega_item_detail(request, pk):
    #GET, PUT, DELETE request for  bodega_item{id}
    try:
        bodega_item = BodegaCognitiveItem.objects.get(pk=pk)
    except BodegaCognitiveItem.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        serializer = BodegaCognitiveItemSerializer(bodega_item)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BodegaCognitiveItemSerializer(bodega_item, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        bodega_item.delete()
        return HttpResponse(status=204)



#Bodega Cognitive Inventory Model
@csrf_exempt
def bodega_inventory_list(request):
    #GET, POST request for bodega_inventory model
    if request.method == 'GET':
        bodega_inventory = BodegaCognitiveInventory.objects.all()
        serializer = BodegaCognitiveInventorySerializer(bodega_inventory, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BodegaCognitiveInventorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JSONParser(serializer.errors, status=400)


@csrf_exempt
def bodega_inventory_detail(request, pk):
    #GET, PUT, DELETE request for  bodega_inventory{id}
    try:
        bodega_inventory = BodegaCognitiveInventory.objects.get(pk=pk)
    except BodegaCognitiveInventory.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        serializer = BodegaCognitiveInventorySerializer(bodega_inventory)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BodegaCognitiveInventorySerializer(bodega_inventory, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        bodega_inventory.delete()
        return HttpResponse(status=204)





#Bodega Cognitive Person Model
@csrf_exempt
def bodega_person_list(request):
    #GET, POST request for bodega_person model
    if request.method == 'GET':
        bodega_person = BodegaCognitivePerson.objects.all()
        serializer = BodegaCognitivePersonSerializer(bodega_person, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BodegaCognitivePersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JSONParser(serializer.errors, status=400)

@csrf_exempt
def bodega_person_detail(request, pk):
    #GET, PUT, DELETE request for  bodega_person{id}
    try:
        bodega_person = BodegaCognitivePerson.objects.get(pk=pk)
    except BodegaCognitivePerson.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        serializer = BodegaCognitivePersonSerializer(bodega_person)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BodegaCognitivePersonSerializer(bodega_person, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        bodega_person.delete()
        return HttpResponse(status=204)





#Bodega Department Model
@csrf_exempt
def bodega_dept_list(request):
    #GET, POST request for bodega_dept model
    if request.method == 'GET':
        bodega_dept = BodegaDept.objects.all()
        serializer = BodegaDeptSerializer(bodega_dept, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BodegaDeptSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JSONParser(serializer.errors, status=400)

@csrf_exempt
def bodega_dept_detail(request, pk):
    #GET, PUT, DELETE request for  bodega_dept{id}
    try:
        bodega_dept = BodegaDept.objects.get(pk=pk)
    except BodegaDept.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        serializer = BodegaDeptSerializer(bodega_dept)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BodegaDeptSerializer(bodega_dept, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        bodega_dept.delete()
        return HttpResponse(status=204)





#USER ADDRESS MODEL

#Fetching data via UserID - Parent ID - RESTRICTED USE
@csrf_exempt
def address_list(request):
    #GET, POST request for metauser_address/
    if request.method == 'GET':
        user_address = UserAddress.objects.all()
        serializer = UserAddressSerializer(user_address, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = UserAddressSerializer(data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def address_detail(request, pk):
    #GET, PUT, DELETE requests for metauser_address/

    try:
        user_address = UserAddress.objects.get(metauserID=pk)
    
    except UserAddress.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        return JsonResponse(UserAddressSerializer(user_address).data)

    elif request.method == 'PUT':
        serializer = UserAddressSerializer(user_address, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user_address.delete()
        return HttpResponse(status=204)








#For Searching ChatRoom by names
@api_view(['POST'])
def searchChatRoomByName(request):
    try:
        instance = ChatRoom.objects.filter(name=request.data['name'])
        serializer = ChatRoomSerializer(instance, many=True)
        return Response(serializer.data, status=200)
    
    except ChatRoom.DoesNotExist:
        return Response(data="No ChatRoom Found.", status=404)


#Filtering Messages by ChatRoom IDs
@api_view(['POST'])
def messagesByChatRoomID(request):
    try:
        instance = Message.objects.filter(chat_room_ID=request.data['chatRoomID'])
        serializer = MessageSerializer(instance, many=True)
        return Response(serializer.data, status=200)
    except Message.DoesNotExist:
        return Response(data="No Message Found.", status=404)

#For Searching Product by productName
@api_view(['POST'])
def searchProductByName(request):
    try:
        instance = Product.objects.filter(productName=request.data['productName'])
        serializer = ProductSerializer(instance, many=True)
        return Response(serializer.data, status=200)

    except Product.DoesNotExist:
        return Response(status=404)
#For searching Boost tags by tags
@api_view(['POST'])
def searchBoostTags(request):
    try:
        instance = BoostTags.objects.filter(tags=request.data['tags'])
        serializer = BoostTagsSerializer(instance, many=True)
        return Response(serializer.data, status=200)
    except BoostTags.DoesNotExist:
        return Response(status=404)



#For searching BoostTags name


@api_view(['POST'])    
def killswitch(request):
    instance = MetaUser.objects.get(meta_username=request.data['meta_username'])
    serializer = KillSwitchSerializer(instance)
    #print(request.data['passcode'])
    if instance.passcode == request.data['passcode'] and instance.public_hashkey == request.data['public_hashkey'] and instance.private_hashkey == request.data['private_hashkey']:
        print("Authentication successful")
        instance.delete()
        return Response(data='KILL SWITCH Successful',status=200)
    else:
        print("Authentication failed")
        return Response(data='KILL SWITCH Failed',status=404)


@api_view(['GET'])
def cartbymetauser(request, pk):
    instance = ShoppingCartItem.objects.filter(metauserID=pk)
    serializer = CartItemSerializer(instance, many=True)
    return Response(serializer.data, status=200)


#Fetch Shop data by metauserID
@api_view(['POST'])
def FetchShopByMetaUserID(request):
    instance = Shop.objects.filter(metauserID=request.data.get('metauserID'))
    serializer = ShopMetaUserSerializer(instance, many=True)
    return Response(serializer.data, status=200)


#Fetch Order Items by metauserID - User's past orders 
@api_view(['POST'])
def FetchOrderItemsByMetaUserID(request):
    instance = OrderItem.objects.filter(metauserID=request.data.get('metauserID'))
    serializer = OrderItemSerializer(instance, many=True)
    return Response(serializer.data, status=200)




#Fetch Collaboration / Yerrr items by metauserID - User's all past collaborations
@api_view(['POST'])
def FetchCollaborationByMetaUserID(request):
    instance = Collaboration.objects.filter(metauserID=request.data['metauserID'])
    serializer = CollaborationSerializer(instance, many=True)
    return Response(serializer.data, status=200)

#Fetch all ChatRooms by MetaUser ID
@api_view(['POST'])
def FetchParticipantByMetaUserID(request):
    instance = Participant.objects.filter(metauserID=request.data.get)
    serializer = ParticipantSerializer(instance, many=True)
    return Response(serializer.data, status=200)

#Authenticate New Participant by Room Hashkey
@api_view(['POST'])
def AuthenticateParticipantByRoomHashkey(request, pk):
    instance = ChatRoom.objects.filter(pk=pk)
    serializer = ChatRoomSerializer(instance, many=True)
    
    if instance.room_hashkey == request.data.get('room_hashkey'):
        print("Authentication Successful")
        return Response(serializer.data, status=200)
    else:
        print("Authentication Failed")
        return Response(serializer.data, status=200)



#Show all products by filtering via metauserID
@api_view(['POST'])
def productsByMetaUser(request):
    try: 
        instance = Product.objects.filter(metauserID=request.data['metauserID'])
        serializer = ProductSerializer(instance, many=True)
        return Response(serializer.data, status=200)
    except Product.DoesNotExist:
        return Response(data="No Products", status=200)

#================================================================================================================================
#STRIPE Connect Integration Code
#Sample views testing the Stripe integration [TEST MODE]
#Comment these views when you go to production mode with SWIFT as the Frontend.

#     elif request.method == 'POST':
#         serializer = ProductOwnershipLedgerSerializer(data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def message_list(request):

    if request.method == 'GET':
        message = Message.objects.all()
        serializer = MessageSerializer(message, many=True)
        return JsonResponse(serializer.data, safe=False)



# @csrf_exempt
# def product_ownershipLedger_detail(request, pk):



#================================================================================================================================

#MetaUser Tags Generic Views
class MetaUserTagsList(generics.ListCreateAPIView):
    queryset = MetaUserTags.objects.all()
    serializer_class = MetaUserTagsSerializer

class MetaUserTagsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetaUserTags.objects.all()
    serializer_class = MetaUserTagsSerializer


#Level Generics Views 
#@csrf_exempt
class LevelList(generics.ListCreateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

#@csrf_exempt
class LevelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

#BLA Generics Views  
#@csrf_exempt
class BLAScoreList(generics.ListCreateAPIView):
    queryset = BLAScore.objects.all()
    serializer_class = BLASerializer

#@csrf_exempt
class BLAScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BLAScore.objects.all()
    serializer_class = BLASerializer

#Sentino Item Proximity Generics Views
#@csrf_exempt
class SentinoItemProximityList(generics.ListCreateAPIView):
    queryset = SentinoItemProximity.objects.all()
    serializer_class = SentinoItemProximitySerializer

#@csrf_exempt
class SentinoItemProximityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SentinoItemProximity.objects.all()
    serializer_class = SentinoItemProximitySerializer

#Sentino Item Projection Generic Views
#@csrf_exempt
class SentinoItemProjectionList(generics.ListCreateAPIView):
    queryset = SentinoItemProjection.objects.all()
    serializer_class = SentinoItemProjectionSerializer

#@csrf_exempt
class SentinoItemProjectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SentinoItemProjection.objects.all()
    serializer_class = SentinoItemProjectionSerializer

#Sentino Item Classification Generic Views    
#@csrf_exempt
class SentinoItemClassificationList(generics.ListCreateAPIView):
    queryset = SentinoItemClassification.objects.all()
    serializer_class = SentinoItemClassificationSerializer

#@csrf_exempt
class SentinoItemClassificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SentinoItemClassification.objects.all()
    serializer_class = SentinoItemClassificationSerializer

#@csrf_exempt
class BLAScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BLAScore.objects.all()
    serializer_class = BLASerializer

#Sentino Inventory Model Generic Views 
#@csrf_exempt
class SentinoInventoryList(generics.ListCreateAPIView):
    queryset = SentinoInventory.objects.all()
    serializer_class = SentinoInventorySerializer
    
#@csrf_exempt
class SentinoInventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SentinoInventory.objects.all()
    serializer_class = SentinoInventorySerializer


#Sentino Description Generic Views
#@csrf_exempt
class SentinoDescriptionList(generics.ListCreateAPIView):
    queryset = SentinoSelfDescription.objects.all()
    serializer_class = SentinoDescriptionSerializer

#@csrf_exempt
class SentinoDescriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SentinoSelfDescription.objects.all()
    serializer_class = SentinoDescriptionSerializer

#Sentino Profile Generic Views
#@csrf_exempt
class SentinoProfileList(generics.ListCreateAPIView):
    queryset = SentinoProfile.objects.all()
    serializer_class = SentinoProfileSerializer

#@csrf_exempt
class SentinoProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SentinoProfile.objects.all()
    serializer_class = SentinoProfileSerializer

#Bodega Vision Generic Views
#@csrf_exempt
class BodegaVisionList(generics.ListCreateAPIView):
    queryset = BodegaVision.objects.all()
    serializer_class = BodegaVisionSerializer

#@csrf_exempt
class BodegaVisionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BodegaVision.objects.all()
    serializer_class = BodegaVisionSerializer


#Bodega Face Generic Views
#@csrf_exempt
class BodegaFaceList(generics.ListCreateAPIView):
    queryset = BodegaFace.objects.all()
    serializer_class = BodegaFaceSerializer

#@csrf_exempt
class BodegaFaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BodegaFace.objects.all()
    serializer_class = BodegaFaceSerializer


#Bodega Personalizer Generic Views
#@csrf_exempt
class BodegaPersonalizerList(generics.ListCreateAPIView):
    queryset = BodegaPersonalizer.objects.all()
    serializer_class = BodegaPersonalizerSerializer

#@csrf_exempt
class BodegaPersonalizerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BodegaPersonalizer.objects.all()
    serializer_class = BodegaPersonalizerSerializer


#Bodega Cognitive Item Generic Views 
#@csrf_exempt
class BodegaCognitiveItemList(generics.ListCreateAPIView):
    queryset = BodegaCognitiveItem.objects.all()
    serializer_class = BodegaCongnitiveItemSerializer

#@csrf_exempt
class BodegaCognitiveItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BodegaCognitiveItem.objects.all()
    serializer_class = BodegaCongnitiveItemSerializer
    

#Bodega Cognitive Inventory Generic Views
#@csrf_exempt
class BodegaCognitiveInventoryList(generics.ListCreateAPIView):
    queryset = BodegaCognitiveInventory.objects.all()
    serializer_class = BodegaCognitiveInventorySerializer

#@csrf_exempt
class BodegaCognitiveInventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BodegaCognitiveInventory.objects.all()
    serializer_class = BodegaCognitiveInventorySerializer

#Sentino Profile Generic Views
#@csrf_exempt
class SentinoProfileList(generics.ListCreateAPIView):
    queryset = SentinoProfile.objects.all()
    serializer_class = SentinoProfileSerializer

#@csrf_exempt
class SentinoProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SentinoProfile.objects.all()
    serializer_class = SentinoProfileSerializer

#Bodega Vision Generic Views
#@csrf_exempt
class BodegaVisionList(generics.ListCreateAPIView):
    queryset = BodegaVision.objects.all()
    serializer_class = BodegaVisionSerializer

#@csrf_exempt
class BodegaVisionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BodegaVision.objects.all()
    serializer_class = BodegaVisionSerializer


#Bodega Face Generic Views
#@csrf_exempt
class BodegaFaceList(generics.ListCreateAPIView):
    queryset = BodegaFace.objects.all()
    serializer_class = BodegaFaceSerializer

#@csrf_exempt
class BodegaFaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BodegaFace.objects.all()
    serializer_class = BodegaFaceSerializer


#Bodega Personalizer Generic Views
#@csrf_exempt
class BodegaPersonalizerList(generics.ListCreateAPIView):
    queryset = BodegaPersonalizer.objects.all()
    serializer_class = BodegaPersonalizerSerializer

#@csrf_exempt
class BodegaPersonalizerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BodegaPersonalizer.objects.all()
    serializer_class = BodegaPersonalizerSerializer


#Bodega Cognitive Item Generic Views 
#@csrf_exempt
class BodegaCognitiveItemList(generics.ListCreateAPIView):
    queryset = BodegaCognitiveItem.objects.all()
    serializer_class = BodegaCongnitiveItemSerializer

#@csrf_exempt
class BodegaCognitiveItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BodegaCognitiveItem.objects.all()
    serializer_class = BodegaCongnitiveItemSerializer
    

#Bodega Cognitive Inventory Generic Views
#@csrf_exempt
class BodegaCognitiveInventoryList(generics.ListCreateAPIView):
    queryset = BodegaCognitiveInventory.objects.all()
    serializer_class = BodegaCognitiveInventorySerializer

#@csrf_exempt
class BodegaCognitiveInventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BodegaCognitiveInventory.objects.all()
    serializer_class = BodegaCognitiveInventorySerializer

#Bodega Cognitive Person Generic Views
#@csrf_exempt
class BodegaCognitivePersonList(generics.ListCreateAPIView):
    queryset = BodegaCognitivePerson.objects.all()
    serializer_class = BodegaCognitivePersonSerializer

#@csrf_exempt
class BodegaCognitivePersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BodegaCognitivePerson.objects.all()
    serializer_class = BodegaCognitivePersonSerializer

#Bodega Cognitive Person Generic Views
#@csrf_exempt
class BodegaCognitivePersonList(generics.ListCreateAPIView):
    queryset = BodegaCognitivePerson.objects.all()
    serializer_class = BodegaCognitivePersonSerializer

#@csrf_exempt
class BodegaCognitivePersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BodegaCognitivePerson.objects.all()
    serializer_class = BodegaCognitivePersonSerializer


#Bodega Dept Generic Views
#@csrf_exempt
class BodegaDeptList(generics.ListCreateAPIView):
    queryset = BodegaDept.objects.all()
    serializer_class = BodegaDeptSerializer

#@csrf_exempt
class BodegaDeptDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BodegaDept.objects.all()
    serializer_class = BodegaDeptSerializer


#User Address Generic Views
#@csrf_exempt
class UserAddressList(generics.ListCreateAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer

#@csrf_exempt
class UserAddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer


#User Payment Generic Views
#@csrf_exempt
class UserPaymentList(generics.ListCreateAPIView):
    queryset = UserPayment.objects.all()
    serializer_class = UserPaymentSerializer

#@csrf_exempt
class UserPaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserPayment.objects.all()
    serializer_class = UserPaymentSerializer

#User Type Generic Views
#@csrf_exempt
class UserTypeList(generics.ListCreateAPIView):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer

#User Type Generic Views
#@csrf_exempt
class UserTypeList(generics.ListCreateAPIView):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer

#@csrf_exempt
class UserTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer


#Chat Room Generic Views
#@csrf_exempt
class ChatRoomList(generics.ListCreateAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

#@csrf_exempt
class ChatRoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

#Particpant Generic Views
#@csrf_exempt
class ParticipantList(generics.ListCreateAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

#Particpant Generic Views
#@csrf_exempt
class ParticipantList(generics.ListCreateAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

#@csrf_exempt
class ParticpiantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

#Message Generic Views 
#@csrf_exempt
class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

#@csrf_exempt
class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

#Message Generic Views 
#@csrf_exempt
class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

#@csrf_exempt
class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer



#Product Category Generic Views
#@csrf_exempt
class ProductCategoryList(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

#@csrf_exempt
class ProductCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer 

#Product Theme Generic Views
#@csrf_exempt
class BoostTagsList(generics.ListCreateAPIView):
    queryset = BoostTags.objects.all()
    serializer_class = BoostTagsSerializer

#Product Theme Generic Views
#@csrf_exempt
class BoostTagsList(generics.ListCreateAPIView):
    queryset = BoostTags.objects.all()
    serializer_class = BoostTagsSerializer

#@csrf_exempt
class BoostTagsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoostTags.objects.all()
    serializer_class = BoostTagsSerializer


#Discount Generic Views
#@csrf_exempt
class DiscountList(generics.ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

#@csrf_exempt
class DiscountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


#Social Generic Views 
#@csrf_exempt
class SocialList(generics.ListCreateAPIView):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer

#@csrf_exempt
class SocialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer

#Shop Generic Views
#@csrf_exempt
class ShopList(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

#Shop Generic Views
#@csrf_exempt
class ShopList(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

#@csrf_exempt
class ShopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


#Product MetaData Generic Views
#@csrf_exempt
class ProductMetaDataList(generics.ListCreateAPIView):
    queryset = ProductMetaData.objects.all()
    serializer_class = ProductMetaDataSerializer

#@csrf_exempt
class ProductMetaDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductMetaData.objects.all()
    serializer_class = ProductMetaDataSerializer


#Product Generic Views 
#@csrf_exempt
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#@csrf_exempt
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#MunchiesPage Generics Views
class MunchiesPageList(generics.ListCreateAPIView):
    from .models import MunchiesPage
    queryset = MunchiesPage.objects.all()
    from .serializers import MunchiesPageSerializer
    serializer_class = MunchiesPageSerializer

class MunchiesPageDetail(generics.RetrieveUpdateDestroyAPIView):
    from .models import MunchiesPage
    queryset = MunchiesPage.objects.all()
    from .serializers import MunchiesPageSerializer
    serializer_class = MunchiesPageSerializer

#Shopping Session Generic Views 
#@csrf_exempt
class ShoppingSessionList(generics.ListCreateAPIView):
    queryset = ShoppingSession.objects.all()
    serializer_class = ShoppingSessionSerializer

class MunchiesVideoList(generics.ListCreateAPIView):
    from .models import MunchiesVideo
    queryset = MunchiesVideo.objects.all()
    from .serializers import MunchiesVideoSerializer
    serializer_class = MunchiesVideoSerializer

class MunchiesVideoDetail(generics.RetrieveUpdateDestroyAPIView):
    from .models import MunchiesVideo
    queryset = MunchiesVideo.objects.all()
    from .serializers import MunchiesVideoSerializer
    serializer_class = MunchiesVideoSerializer


#Munchies Videos Generics Views
    

#Collaboration Generic Views
#@csrf_exempt
class CollaborationList(generics.ListCreateAPIView):
    queryset = Collaboration.objects.all()
    serializer_class = CollaborationSerializer

#@csrf_exempt
class CollaborationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collaboration.objects.all()
    serializer_class = CollaborationSerializer


#Shopping Session Generic Views 
#@csrf_exempt
class ShoppingSessionList(generics.ListCreateAPIView):
    queryset = ShoppingSession.objects.all()
    serializer_class = ShoppingSessionSerializer

#@csrf_exempt
class ShoppingSessionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingSession.objects.all()
    serializer_class = ShoppingSessionSerializer


#Cart Item Generic Views 
#@csrf_exempt
class CartItemList(generics.ListCreateAPIView):
    queryset = ShoppingCartItem.objects.all()
    serializer_class = CartItemSerializer

#@csrf_exempt
class CartItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingCartItem.objects.all()
    serializer_class = CartItemSerializer


#Order Detail Generic Views
#@csrf_exempt
class OrderDetailList(generics.ListCreateAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailsSerializer

#@csrf_exempt
class OrderDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailsSerializer


#Order Item Generic View
#@csrf_exempt
class OrderItemList(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

#@csrf_exempt
class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderSuccessList(generics.ListCreateAPIView):
    queryset = OrderSuccess.objects.all()
    serializer_class = OrderSuccessSerializer

class OrderSuccessDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderSuccess.objects.all()
    serializer_class = OrderSuccessSerializer

class OrderFailureList(generics.ListCreateAPIView):
    queryset = OrderFailure.objects.all()
    serializer_class = OrderFailureSerializer

class OrderFailureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderFailure.objects.all()
    serializer_class = OrderFailureSerializer


#SysOps Agnet Generic Views
#@csrf_exempt
class SysOpsAgentList(generics.ListCreateAPIView):
    queryset = SysOpsAgent.objects.all()
    serializer_class = SysOpsAgentSerializer

#@csrf_exempt
class SysOpsAgentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SysOpsAgent.objects.all()
    serializer_class = SysOpsAgentSerializer

#Stripe Integration Viewset

#SysOps Agent Repo Generic View
#@csrf_exempt
class SysOpsAgentRepoList(generics.ListCreateAPIView):
    queryset = SysOpsAgentRepo.objects.all()
    serializer_class = SysOpsAgentRepoSerializer

#@csrf_exempt
class SysOpsAgentRepoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SysOpsAgentRepo.objects.all()
    serializer_class = SysOpsAgentRepoSerializer


#SysOps Agent Project Generic Views
#@csrf_exempt
class SysOpsAgentProjectList(generics.ListCreateAPIView):
    queryset = SysOpsProject.objects.all()
    serializer_class = SysOpsProjectSerializer

#@csrf_exempt
class SysOpsAgentProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SysOpsProject.objects.all()
    serializer_class = SysOpsProjectSerializer



#SysOps Demand Node Generic Views 
#@csrf_exempt
class SysOpsDemandNodeList(generics.ListCreateAPIView):
    queryset = SysOpsDemandNode.objects.all()
    serializer_class = SysOpsDemandNodeSerializer

#@csrf_exempt
class SysOpsDemandNodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SysOpsDemandNode.objects.all()
    serializers_class = SysOpsDemandNodeSerializer


#SysOps Supply Node Generic Views
#@csrf_exempt
class SysOpsSupplyNodeList(generics.ListCreateAPIView):
    queryset = SysOpsSupplyNode.objects.all()
    serializers_class = SysOpsSupplyNodeSerializer

#@csrf_exempt
class SysOpsSupplyNodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SysOpsSupplyNode.objects.all()
    serializer_class = SysOpsSupplyNodeSerializer



#Stripe Integration Viewset

stripe.api_key='sk_test_51L08MiHqfk1hk8aABrqHYR0aGbxNY3YkKdSmX8VRRSKEVUTmYnvfxert4KnNnAh1R2qSbyRpKiohlYpG8Nfk89vB00W13HuLdg'

#Create a New Stripe Account Endpoint - For Digital Services
@api_view(['POST'])
def createStripeAccount(request):
    newStripeAccount = stripe.Account.create(type="express", 
                                            country=request.data['country'], 
                                            email=request.data['email'],
                                            )
    

    return Response(newStripeAccount, status=200)

    

#Proceed with Stripe Account Authentication -- Outsourced to Stripe via in-app browser
#Generates an URL which facilitates on-boaridng via Stripe
@api_view(['POST'])
def authenticateStripeAccount(request):
    stripeAuthLink = stripe.AccountLink.create(
                                            account=request.data['stripeAccountID'],
                                            refresh_url="https://example.com/reauth",
                                            return_url="https://example.com/return",
                                            type="account_onboarding")

    return Response(stripeAuthLink.url, status=200)



#Retreive a StripeAccount and store that data in our Database
@api_view(['POST'])
def retreiveStripeAccount(request):
    stripeAccount = stripe.Account.retrieve(request.data['stripeAccountID'])


    if stripeAccount.capabilities.get("card_payments") and stripeAccount.capabilities.get("transfers") == 'active':

        #Check if the StripeAccount already exisst or not?
        try:
            existingStripeAccount = stripeAccountInfo.objects.get(stripeAccountID=request.data['stripeAccountID'])
            stripeAccountAuth = "Existing Austhorized Bodega Account ID: "+ existingStripeAccount.stripeAccountID + " | Payout Status: Active"
            return Response(data=stripeAccountAuth, status=200)
        except:
            stripeAccountInfo.objects.create(
            metauserID = MetaUser.objects.get(pk=request.data['metauserID']),
            stripeAccountID = stripeAccount.id, 
            accountPaymentStatus = True,
            accountTransfersStatus = True, 
        )
            stripeAccountAuth = "New Authorized Bodega Account ID: "+ stripeAccount.id + " | Payout Status: Active"
            return Response(data=stripeAccountAuth, status=200)

        

    else:
        return Response(data='Project-Bodega Creator Status: INELIGIBLE FOR PAYOUTS', status=200)


#Generic Views for stripeAccountInfo model instance.
class StripeAccountInfoList(generics.ListCreateAPIView):
    queryset = stripeAccountInfo.objects.all()
    serializer_class = stripeAccountInfoSerializer

class StripeAccountInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = stripeAccountInfo.objects.all()
    serializer_class = stripeAccountInfoSerializer




#Transfer funds to Bodega Merchants via stripeAccountID
@api_view(['POST'])
def payoutStripeAccount(request):
    transferFunds = stripe.Transfer.create(
        amount=request.data['payoutAmount'], 
        currency=request.data['currency'], 
        destination=request.data['stripeAccountID'],
        transfer_group = request.data['orderID'],
    )


    stripeAccountTransfer.objects.create(
                                        stripeAccountInfoID =  stripeAccountInfo.objects.get(pk = request.data['stripeAccountInfoID']),
                                        transactionID = transferFunds.id, 
                                        payoutAmount = transferFunds.amount,
                                        payoutOrderInfo = transferFunds.transfer_group,

    )

    return Response(data="Successfull. TransactionID: "+ transferFunds.id, status=200 )


#Generic views for Stripe Account Transfer Model  Instance
class StripeAccountTransferList(generics.ListCreateAPIView):
    queryset = stripeAccountTransfer.objects.all()
    serializer_class = stripeAccountTransferSerializer


class StripeAccountTransferDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = stripeAccountTransfer.objects.all()
    serializer_class = stripeAccountTransferSerializer



#Stripe API Endpoint for listing all transfers

@api_view(['GET'])
def allStripeTransfers(request):
    alltransfers = stripe.Transfer.list()
    return Response(data=alltransfers, status=200)



#Reversing Transfer Funds to Connected Accounts.
@api_view(['POST'])
def reverseFunds(request):
    refundAmount = stripe.Transfer.create_reversal(
                                                request.data['transactionID'], 
                                                amount=request.data['refundAmount']
    )
    try:
        refundObject=stripeAccountTransfer.objects.get(transactionID=request.data['transactionID'])
        refundObject.payoutAmount=request.data['refundAmount']
        serializer = stripeAccountTransferSerializer(refundObject)
        return Response(serializer.data, status=200)
    except stripeAccountTransfer.DoesNotExist:
        return Response(data="Transaction ID Invalid", status=404)


#Retreive our Stripe Balance and maintain Stripe Balance ledgers
@api_view(['GET'])
def retrieveStripeBalance(request):
    balance = stripe.Balance.retrieve()
    #accountBalance = stripeAccountBalance.objects.create(
        #store in Database later. For now, return JSON instead
    
    return Response(data=balance, status=200)




#Stripe Code for Creating a new Charge to user's Payment methods.

@api_view(['POST'])
def createCharge(request):
    stripeCharge = stripe.PaymentIntent.create(
                                        amount=request.data['amount'], 
                                        currency=request.data['currency'], 
                                        #source='tok_visa,
                                        payment_method_types=["card"],
                                        description=request.data['description'],
                                        customer=request.data['customerID'],
                                        payment_method= request.data['paymentMethodID']
    )
    captureCharge = stripe.PaymentIntent.confirm(stripeCharge.id)

    try:
        chargeObject=stripeCharges.objects.create(      bodegaCustomerID = customerPayment.objects.get(pk=request.data['bodegaCustomerID']), 
                                                        amount=request.data['amount'], 
                                                        currency=request.data['currency'],
                                                        description=request.data['description'],
                                                        stripeChargeID = stripeCharge.id, 
                                                        paymentStatus=True, 
                                                        capturedStatus=True, 
                                                        stripeCustomerID = request.data['customerID'],
                                                        stripePaymentMethodID = request.data['paymentMethodID'])
                                                        
        serializer = stripeChargesSerializer(chargeObject)
        return Response (serializer.data, status=200)
    except:
        return Response(data=serializer.errors, status=404)

#Generic Views for stripeCHarges model instance.

class StripeChargesList(generics.ListCreateAPIView):
    queryset = stripeCharges.objects.all()
    serializer_class = stripeChargesSerializer

class StripeChargesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = stripeCharges.objects.all()
    serializer_class = stripeChargesSerializer



#STRIPE SUBSCRIPTION CODE 


#Create a Payment Method which will have customer's credit card information and then pass the PM ID to a new Customer.
@api_view(['POST'])
def createStripeCustomer(request):

    customer = stripe.Customer.create(
                                      name = request.data['name'], 
                                      email = request.data['email'], 
                                      
    )
    paymentMethod = stripe.PaymentMethod.create(
                                                type="card", 
                                                card ={
                                                    "number" : request.data['number'], 
                                                    "exp_month": request.data['exp_month'], 
                                                    "exp_year": request.data['exp_year'],
                                                    "cvc": request.data['cvc'],
                                                },
    )
    #Attaching Payment method to the Customer ID 
    attachPaymentMethod = stripe.PaymentMethod.attach(
                                                        paymentMethod.id, 
                                                        customer=customer.id,
    )

    #Setting Invoice Settings for Customer for Subscription Services
    modifiedCustomer = stripe.Customer.modify(
                                                customer.id, 
                                                invoice_settings =
                                                                    {
                                                                        "default_payment_method": paymentMethod.id,
                                                                    }
                                                
    )
    try:
        customerObject = customerPayment.objects.create(
                                                        metauserID = MetaUser.objects.get(pk=request.data['metauserID']), 
                                                        name = request.data['name'],
                                                        email = request.data['email'],
                                                        customerID = customer.id,
                                                        paymentMethodID = paymentMethod.id
        )
        serializer = bodegaCustomerSerializer(customerObject)
        return Response(serializer.data, status=200)
    except:
        return Response(data="Payment Method Failed", status=404)


#Views for bodegaCustomer Data 
class bodegaCustomerList(generics.ListCreateAPIView):
    queryset = customerPayment.objects.all()
    serializer_class = bodegaCustomerSerializer

class bodegaCustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = customerPayment.objects.all()
    serializer_class = bodegaCustomerSerializer



#1/2 - first part of creating subscription for creators.
#the creator creates a Product and Prices it  - Like a tier in subscription design
@api_view(['POST'])
def createStripeSubscriptionProduct(request):
    stripeProduct = stripe.Product.create( 
                                        name = request.data['subscriptionName'], 
                                        description = request.data['subscriptionDescription']
    )

    #Create Price and charging intervals for subscription
    stripePrice = stripe.Price.create(
                                        product = stripeProduct.id, 
                                        unit_amount = request.data['amount'], 
                                        currency = request.data['currency'], 
                                        recurring = {"interval": request.data['chargingFrequency']},
                                        tax_behavior = "inclusive"

    )

    #Store the creators's subscription detail to the DB
    try:
        creatorSubscriptionObject = creatorSubscription.objects.create(
                                                                        metauserID = MetaUser.objects.get(pk=request.data['metauserID']), 
                                                                        subscriptionName = request.data['subscriptionName'], 
                                                                        subscriptionDescription = request.data['subscriptionDescription'],
                                                                        amount =request.data['amount'],
                                                                        currency=request.data['currency'],
                                                                        chargingFrequency = request.data['chargingFrequency'],
                                                                        stripeProductID = stripeProduct.id, 
                                                                        stripePriceID = stripePrice.id
        )
        serializer = creatorSubscriptionSerializer(creatorSubscriptionObject)
        return Response(serializer.data, status=200)
    
    except:
        return Response(data="Unable to create Subscription product", status=404)


class creatorSubscriptionList(generics.ListCreateAPIView):
    queryset = creatorSubscription.objects.all()
    serializer_class = creatorSubscriptionSerializer

class creatorSubscriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = creatorSubscription.objects.all()
    serializer_class = creatorSubscriptionSerializer



#2/2 - second part of subscription design process
#Now, the customer comes to the creator and subscribes to their subscription plans
#We pass the Customer ID and Price ID to the Subscription Object.

@api_view(['POST'])
def subscribe(request):
    #Pass customerID of the user who wants to subscribe to their subscriptionand price ID which was created by the Creator
    stripeSubscription = stripe.Subscription.create(
                                                    customer = request.data['customerID'],
                                                    items =[
                                                            {
                                                                "price": request.data['stripePriceID']
                                                            }
                                                    ],
                                                    payment_settings =[
                                                                        {

                                                                        }
                                                    ]
    )

    try:
        subscribersObject = Subscribers.objects.create(
                                                        metauserID = MetaUser.objects.get(pk=request.data['metauserID']),
                                                        customerID = request.data['customerID'], 
                                                        priceID = request.data['stripePriceID'],
                                                        subscriptionID = stripeSubscription.id,
                                                        productID = stripeSubscription.plan["product"],
                                                        amount = stripeSubscription.plan["amount"], 
                                                        invoiceID = stripeSubscription.latest_invoice,
                                                        status = stripeSubscription.status
        )
        serializer = subscribersSerializer(subscribersObject)
        return Response(serializer.data, status=200)
    
    except:
        return Response(data="Unable to Subscribe", status=404)

        


#Notification View Settings
class notificationsList(generics.ListCreateAPIView):
    queryset = Notifications.objects.all()
    serializer_class = notificationsSerializer

class notificationsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notifications.objects.all()
    serializer_class = notificationsSerializer

    

@api_view(['POST'])
def FetchNotificationsByMetaUserID(request):
    try: 
        instance = Notifications.objects.filter(metauserID=request.data['metauserID'])
        serializer = notificationsSerializer(instance, many=True)
        return Response(serializer.data, status=200)
    except Notifications.DoesNotExist:
        return Response(data="No Notifications Found", status=404)



#Fetch Products by BoostTagsID
@api_view(['POST'])
def FetchBoostTagsByProductID(request):
    try:
        instance = Product.objects.filter(boostTagsID=request.data['boostTagsID'])
        serializer = ProductSerializer(instance, many=True)
        return Response (serializer.data, status=200)
    except Product.DoesNotExist:
        return Response(data="Product not found", status=404)