from rest_framework import status, generics, mixins, request, viewsets
from rest_framework.decorators import api_view
from rest_framework.views import exception_handler
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response
import datetime
from django.utils import timezone
import requests
from rest_framework.request import Request



from backend.models import MetaUser, UserAddress, UserPayment, UserType, ChatRoom, Particpant, Message, ProductCategory, ProductThemes, Discount, Social, ShopPayout, Shop, Product,  Collaboration, private_metauser_hashkey_generator, public_metauser_hashkey_generator, agent_hashkey_generator, project_hashkey_generator, product_hashkey_generator, project_hashkey_generator, chatroom_hashkey_generator, message_hashkey_generator, Level, BLAScore, BodegaCognitiveInventory, BodegaCognitiveItem, BodegaCognitivePerson, BodegaDept, BodegaFace, BodegaPersonalizer, BodegaVision, ProductMetaData, SentinoInventory, SentinoItemClassification, SentinoItemProjection, SentinoItemProximity, SentinoProfile, SentinoSelfDescription, CartItem, ShoppingSession, OrderDetail, OrderItem, SysOpsAgent, SysOpsAgentRepo, SysOpsProject, SysOpsDemandNode, SysOpsSupplyNode, ShoppingCartItem
from backend.serializers import KillSwitchSerializer, MetaUserSerializer, UserAddressSerializer, UserPaymentSerializer, UserTypeSerializer, ChatRoomSerializer, ParticpantSerializer, MessageSerializer, ProductCategorySerializer, ProductThemesSerializer, DiscountSerializer, SocialSerializer, ShopSerializer, ProductSerializer, CollaborationSerializer, ProductMetaDataSerializer, BLASerializer, BodegaCognitiveInventorySerializer, BodegaCognitiveInventorySerializer, BodegaCognitivePersonSerializer, BodegaDeptSerializer, BodegaFaceSerializer, BodegaPersonalizerSerializer, BodegaVisionSerializer, LevelSerializer, SentinoDescriptionSerializer, SentinoDescriptionSerializer, SentinoInventorySerializer, SentinoItemClassificationSerializer, SentinoItemProjectionSerializer, SentinoItemProximitySerializer, SentinoProfileSerializer, CartItemSerializer, ShoppingSessionSerializer, OrderDetailsSerializer, OrderItemSerializer, SysOpsAgentSerializer, SysOpsAgentRepoSerializer, SysOpsProjectSerializer, SysOpsDemandNodeSerializer, SysOpsSupplyNodeSerializer, SentinoItemClassificationSerializer, BodegaCongnitiveItemSerializer, OrderDetailsSerializer, SysOpsSupplyNodeSerializer, MetaUserAuthSerializer





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

def metauserauth(request):
    #this will be linked to the authorization view on any frontend 
    #this will be the template for any auth needed across any of our platforms  
    
    return (request)


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
    serializer = MetaUserAuthSerializer(instance)
    #print(request.data['passcode'])
    if instance.passcode == request.data['passcode'] and instance.public_hashkey == request.data['public_hashkey']:
        print("Authentication successful")
        return Response(data='Authentication Successful',status=200)
    else:
        print("Authentication failed")
        return Response(data='Authentication Failed',status=404)


@api_view(['POST'])    
def killswitch(request, pk):
    instance = MetaUser.objects.get(meta_username=pk)
    serializer = KillSwitchSerializer(instance)
    #print(request.data['passcode'])
    if instance.passcode == request.data['passcode'] and instance.public_hashkey == request.data['public_hashkey'] and instance.private_hashkey == request.data['private_hashkey']:
        print("Authentication successful")
        return Response(data='KILL SWITCH Successful',status=200)
    else:
        print("Authentication failed")
        return Response(data='KILL SWITCH Failed',status=404)


@api_view(['GET'])
def cartbymetauser(request, pk):
    instance = ShoppingCartItem.objects.get(metauserID=pk)
    serializer = CartItemSerializer(instance)
    return Response(serializer.data, status=200)


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
class ParticpantList(generics.ListCreateAPIView):
    queryset = Particpant.objects.all()
    serializer_class = ParticpantSerializer

#@csrf_exempt
class ParticpantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Particpant.objects.all()
    serializer_class = ParticpantSerializer


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
class ProductThemesList(generics.ListCreateAPIView):
    queryset = ProductThemes.objects.all()
    serializer_class = ProductThemesSerializer

#@csrf_exempt
class ProductThemesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductThemes.objects.all()
    serializer_class = ProductThemesSerializer


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


#SysOps Agnet Generic Views
#@csrf_exempt
class SysOpsAgentList(generics.ListCreateAPIView):
    queryset = SysOpsAgent.objects.all()
    serializer_class = SysOpsAgentSerializer

#@csrf_exempt
class SysOpsAgentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SysOpsAgent.objects.all()
    serializer_class = SysOpsAgentSerializer


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



#Views Code V1.0 without Generic API Viewsets

# #MetaUser Views
# #@csrf_exempt
# def metauser_list(request):
#     #GET, POST request for metauser/
#     if request.method == 'GET':
#         metauser = MetaUser.objects.all()
#         serializer = MetaUserSerializer(metauser, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = MetaUserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
        
#         return JsonResponse(serializer.errors, status=400)
#         #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# #@csrf_exempt
# def metauser_detail(request, pk):
#     #GET,PUT,DELETE request for metauser{id}
#     try:
#         metauser = MetaUser.objects.get(pk=pk)
#     except MetaUser.DoesNotExist:
#         return JsonResponse(status=404)

    
#     if request.method == 'GET':
#         serializer = MetaUserSerializer(metauser)
#         return JsonResponse(serializer.data)

    
#     elif request.method == 'PUT':
#         serializer = MetaUserSerializer(metauser, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         metauser.delete()
#         return HttpResponse(status=204)




# #Level Views
# #@csrf_exempt
# def level_list(request):
#     #GET, POST request for Level
#     if request.method == 'GET':
#         level = Level.objects.all()
#         serializer = LevelSerializer(level, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = LevelSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
        
#         return JSONParser(serializer.errors, status=400)



# #@csrf_exempt
# def level_detail(request, pk):
#     #GET, PUT, DELETE request for level{id}
#     try:
#         level = Level.objects.get(pk=pk)
#     except Level.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         serializer = LevelSerializer(level)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = LevelSerializer(level, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         level.delete()
#         return HttpResponse(status=204)




# #BLA Views
# #@csrf_exempt
# def blascore_list(request):
#     #GET, POST request for BLAScore
#     if request.method == 'GET':
#         base_line_analysis = BLAScore.objects.all()
#         serializer = BLASerializer(base_line_analysis, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = BLASerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
        
#         return JSONParser(serializer.errors, status=400)




# #@csrf_exempt
# def blascore_detail(request, pk):
#     #GET, PUT, DELETE request for  blascore{id}
#     try:
#         base_line_analysis = BLAScore.objects.get(pk=pk)
#     except BLAScore.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         serializer = BLASerializer(base_line_analysis)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = BLASerializer(base_line_analysis, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         base_line_analysis.delete()
#         return HttpResponse(status=204)




# #Sentino Item Proximity Model
# #@csrf_exempt
# def sentino_item_proximity_list(request):
#     #GET, POST request for sentino_item_proximity model
#     if request.method == 'GET':
#         sentino_item_proximity = SentinoItemProximity.objects.all()
#         serializer = SentinoItemProximitySerializer(sentino_item_proximity, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SentinoItemProximitySerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
        
#         return JSONParser(serializer.errors, status=400)

# #@csrf_exempt
# def sentino_item_proximity_detail(request, pk):
#     #GET, PUT, DELETE request for  sentino_item_proximity{id}
#     try:
#         sentino_item_proximity = SentinoItemProximity.objects.get(pk=pk)
#     except SentinoItemProximity.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         serializer = SentinoItemProximitySerializer(sentino_item_proximity)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = SentinoItemProximitySerializer(sentino_item_proximity, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         sentino_item_proximity.delete()
#         return HttpResponse(status=204)





# #Sentino Item Projection Model
# #@csrf_exempt
# def sentino_item_projection_list(request):
#     #GET, POST request for sentino_item_projection model
#     if request.method == 'GET':
#         sentino_item_projection = SentinoItemProjection.objects.all()
#         serializer = SentinoItemProjectionSerializer(sentino_item_projection, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SentinoItemProjectionSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
        
#         return JSONParser(serializer.errors, status=400)


# #@csrf_exempt
# def sentino_item_projection_detail(request, pk):
#     #GET, PUT, DELETE request for  sentino_item_projection{id}
#     try:
#         sentino_item_projection = SentinoItemProjection.objects.get(pk=pk)
#     except SentinoItemProjection.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         serializer = SentinoItemProjectionSerializer(sentino_item_projection)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = SentinoItemProjectionSerializer(sentino_item_projection, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         sentino_item_projection.delete()
#         return HttpResponse(status=204)





# #Sentino Item Classification Model
# #@csrf_exempt
# def sentino_item_classification_list(request):
#     #GET, POST request for sentino_item_classification model
#     if request.method == 'GET':
#         sentino_item_classification = SentinoItemClassification.objects.all()
#         serializer = SentinoItemClassficationSerializer(sentino_item_classification, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SentinoItemClassficationSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
        
#         return JSONParser(serializer.errors, status=400)



# #@csrf_exempt
# def sentino_item_classification_detail(request, pk):
#     #GET, PUT, DELETE request for  sentino_item_classification{id}
#     try:
#         sentino_item_classification = SentinoItemClassification.objects.get(pk=pk)
#     except SentinoItemClassification.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         serializer = SentinoItemClassficationSerializer(sentino_item_classification)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = SentinoItemClassficationSerializer(sentino_item_classification, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         sentino_item_classification.delete()
#         return HttpResponse(status=204)





# #Sentino  Inventory Model
# #@csrf_exempt
# def sentino_inventory_list(request):
#     #GET, POST request for sentino_inventory model
#     if request.method == 'GET':
#         sentino_inventory = SentinoInventory.objects.all()
#         serializer = SentinoInventorySerializer(sentino_inventory, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SentinoInventorySerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
        
#         return JSONParser(serializer.errors, status=400)



# #@csrf_exempt
# def sentino_inventory_detail(request, pk):
#     #GET, PUT, DELETE request for  sentino_inventory{id}
#     try:
#         sentino_inventory = SentinoInventory.objects.get(pk=pk)
#     except SentinoInventory.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         serializer = SentinoInventorySerializer(sentino_inventory)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = SentinoInventorySerializer(sentino_inventory, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         sentino_inventory.delete()
#         return HttpResponse(status=204)




# #Sentino Description Model
# #@csrf_exempt
# def sentino_description_list(request):
#     #GET, POST request for sentino_description model
#     if request.method == 'GET':
#         sentino_description = SentinoSelfDescription.objects.all()
#         serializer = SentinoDescriptionSerializer(sentino_description, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SentinoDescriptionSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
        
#         return JSONParser(serializer.errors, status=400)



# #@csrf_exempt
# def sentino_description_detail(request, pk):
#     #GET, PUT, DELETE request for  sentino_description{id}
#     try:
#         sentino_description = SentinoSelfDescription.objects.get(pk=pk)
#     except SentinoSelfDescription.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         serializer = SentinoDescriptionSerializer(sentino_description)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = SentinoDescriptionSerializer(sentino_description, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         sentino_description.delete()
#         return HttpResponse(status=204)


# #Sentino Profile Model
# #@csrf_exempt
# def sentino_profile_list(request):
#     #GET, POST request for sentino_profile model
#     if request.method == 'GET':
#         sentino_profile = SentinoProfile.objects.all()
#         serializer = SentinoProfileSerializer(sentino_profile, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SentinoProfileSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
        
#         return JSONParser(serializer.errors, status=400)



# #@csrf_exempt
# def sentino_profile_detail(request, pk):
#     #GET, PUT, DELETE request for  sentino_profile{id}
#     try:
#         sentino_profile = SentinoProfile.objects.get(pk=pk)
#     except SentinoProfile.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         serializer = SentinoProfileSerializer(sentino_profile)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = SentinoProfileSerializer(sentino_profile, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         sentino_profile.delete()
#         return HttpResponse(status=204)



# #Bodega Vision Model
# #@csrf_exempt
# def bodega_vision_list(request):
#     #GET, POST request for bodega_vision model
#     if request.method == 'GET':
#         bodega_vision = BodegaVision.objects.all()
#         serializer = BodegaVisionSerializer(bodega_vision, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = BodegaVisionSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
        
#         return JSONParser(serializer.errors, status=400)



# #@csrf_exempt
# def bodega_vision_detail(request, pk):
#     #GET, PUT, DELETE request for  bodega_vision{id}
#     try:
#         bodega_vision = BodegaVision.objects.get(pk=pk)
#     except BodegaVision.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         serializer = BodegaVisionSerializer(bodega_vision)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = BodegaVisionSerializer(bodega_vision, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         bodega_vision.delete()
#         return HttpResponse(status=204)




# #Bodega Face Model
# #@csrf_exempt
# def bodega_face_list(request):
#     #GET, POST request for bodega_face model
#     if request.method == 'GET':
#         bodega_face = BodegaFace.objects.all()
#         serializer = BodegaFaceSerializer(bodega_face, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = BodegaFaceSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
        
#         return JSONParser(serializer.errors, status=400)



# #@csrf_exempt
# def bodega_face_detail(request, pk):
#     #GET, PUT, DELETE request for  bodega_face{id}
#     try:
#         bodega_face = BodegaFace.objects.get(pk=pk)
#     except BodegaFace.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         serializer = BodegaFaceSerializer(bodega_face)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = BodegaFaceSerializer(bodega_face, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         bodega_face.delete()
#         return HttpResponse(status=204)





# #Bodega Personalizer Model
# #@csrf_exempt
# def bodega_personalizer_list(request):
#     #GET, POST request for bodega_personalizer model
#     if request.method == 'GET':
#         bodega_personalizer = BodegaPersonalizer.objects.all()
#         serializer = BodegaPersonalizerSerializer(bodega_personalizer, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = BodegaPersonalizerSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
        
#         return JSONParser(serializer.errors, status=400)



# #@csrf_exempt
# def bodega_personalizer_detail(request, pk):
#     #GET, PUT, DELETE request for  bodega_personalizer{id}
#     try:
#         bodega_personalizer = BodegaPersonalizer.objects.get(pk=pk)
#     except BodegaPersonalizer.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         serializer = BodegaPersonalizerSerializer(bodega_personalizer)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = BodegaPersonalizerSerializer(bodega_personalizer, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         bodega_personalizer.delete()
#         return HttpResponse(status=204)





# #Bodega Cognitive Item Model
# #@csrf_exempt
# def bodega_item_list(request):
#     #GET, POST request for bodega_item model
#     if request.method == 'GET':
#         bodega_item = BodegaCognitiveItem.objects.all()
#         serializer = BodegaCognitiveItemSerializer(bodega_item, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = BodegaCognitiveItemSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
        
#         return JSONParser(serializer.errors, status=400)

# #@csrf_exempt
# def bodega_item_detail(request, pk):
#     #GET, PUT, DELETE request for  bodega_item{id}
#     try:
#         bodega_item = BodegaCognitiveItem.objects.get(pk=pk)
#     except BodegaCognitiveItem.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         serializer = BodegaCognitiveItemSerializer(bodega_item)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = BodegaCognitiveItemSerializer(bodega_item, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         bodega_item.delete()
#         return HttpResponse(status=204)



# #Bodega Cognitive Inventory Model
# #@csrf_exempt
# def bodega_inventory_list(request):
#     #GET, POST request for bodega_inventory model
#     if request.method == 'GET':
#         bodega_inventory = BodegaCognitiveInventory.objects.all()
#         serializer = BodegaCognitiveInventorySerializer(bodega_inventory, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = BodegaCognitiveInventorySerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
        
#         return JSONParser(serializer.errors, status=400)



# #@csrf_exempt
# def bodega_inventory_detail(request, pk):
#     #GET, PUT, DELETE request for  bodega_inventory{id}
#     try:
#         bodega_inventory = BodegaCognitiveInventory.objects.get(pk=pk)
#     except BodegaCognitiveInventory.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         serializer = BodegaCognitiveInventorySerializer(bodega_inventory)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = BodegaCognitiveInventorySerializer(bodega_inventory, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         bodega_inventory.delete()
#         return HttpResponse(status=204)





# #Bodega Cognitive Person Model
# #@csrf_exempt
# def bodega_person_list(request):
#     #GET, POST request for bodega_person model
#     if request.method == 'GET':
#         bodega_person = BodegaCognitivePerson.objects.all()
#         serializer = BodegaCognitivePersonSerializer(bodega_person, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = BodegaCognitivePersonSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
        
#         return JSONParser(serializer.errors, status=400)

# #@csrf_exempt
# def bodega_person_detail(request, pk):
#     #GET, PUT, DELETE request for  bodega_person{id}
#     try:
#         bodega_person = BodegaCognitivePerson.objects.get(pk=pk)
#     except BodegaCognitivePerson.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         serializer = BodegaCognitivePersonSerializer(bodega_person)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = BodegaCognitivePersonSerializer(bodega_person, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         bodega_person.delete()
#         return HttpResponse(status=204)





# #Bodega Department Model
# #@csrf_exempt
# def bodega_dept_list(request):
#     #GET, POST request for bodega_dept model
#     if request.method == 'GET':
#         bodega_dept = BodegaDept.objects.all()
#         serializer = BodegaDeptSerializer(bodega_dept, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = BodegaDeptSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
        
#         return JSONParser(serializer.errors, status=400)

# #@csrf_exempt
# def bodega_dept_detail(request, pk):
#     #GET, PUT, DELETE request for  bodega_dept{id}
#     try:
#         bodega_dept = BodegaDept.objects.get(pk=pk)
#     except BodegaDept.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         serializer = BodegaDeptSerializer(bodega_dept)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = BodegaDeptSerializer(bodega_dept, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         bodega_dept.delete()
#         return HttpResponse(status=204)





# #USER ADDRESS MODEL

# #Fetching data via UserID - Parent ID - RESTRICTED USE
# #@csrf_exempt
# def address_list(request):
#     #GET, POST request for metauser_address/
#     if request.method == 'GET':
#         user_address = UserAddress.objects.all()
#         serializer = UserAddressSerializer(user_address, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         serializer = UserAddressSerializer(data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# #@csrf_exempt
# def address_detail(request, pk):
#     #GET, PUT, DELETE requests for metauser_address/

#     try:
#         user_address = UserAddress.objects.get(user_ID=pk)
    
#     except UserAddress.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         return JsonResponse(UserAddressSerializer(user_address).data)

#     elif request.method == 'PUT':
#         serializer = UserAddressSerializer(user_address, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         user_address.delete()
#         return HttpResponse(status=204)




# #Fetching data via User_AddressID - Child Table ID - FREE USE

# #@csrf_exempt
# def child_address_detail(request, pk):
#     #GET, PUT, DELETE requests for metauser_address/

#     try:
#         user_address = UserAddress.objects.get(pk=pk)
    
#     except UserAddress.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         return JsonResponse(UserAddressSerializer(user_address).data)

#     elif request.method == 'PUT':
#         serializer = UserAddressSerializer(user_address, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         user_address.delete()
#         return HttpResponse(status=204)



# #-------------------------------------------------------------------------------------------------------------------------------------------------

# #User_Payment Model Instance 
# #Fetching data via UserID - Parent ID - RESTRICTED USE


# #@csrf_exempt
# def user_payment_list(request):
#     #GET, POST request for metauser_address/
#     if request.method == 'GET':
#         user_payment = UserPayment.objects.all()
#         serializer = UserPaymentSerializer(user_payment, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         serializer = UserPaymentSerializer(data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# #@csrf_exempt
# def user_payment_detail(request, pk):
#     #GET, PUT, DELETE requests for metauser_address/

#     try:
#         user_payment = UserPayment.objects.get(user_ID=pk)
    
#     except UserPayment.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         return JsonResponse(UserPaymentSerializer(user_payment).data)

#     elif request.method == 'PUT':
#         serializer = UserPaymentSerializer(user_payment, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         user_payment.delete()
#         return HttpResponse(status=204)




# #Fetching data via User_AddressID - Child Table ID - FREE USE

# #@csrf_exempt
# def child_payment_detail(request, pk):
#     #GET, PUT, DELETE requests for metauser_address/

#     try:
#         user_payment = UserPayment.objects.get(pk=pk)
    
#     except UserPayment.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         return JsonResponse(UserPaymentSerializer(user_payment).data)

#     elif request.method == 'PUT':
#         serializer = UserPaymentSerializer(user_payment, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         user_payment.delete()
#         return HttpResponse(status=204)



# #------------------------------------------------------------------------------------


# #User_Payment Model Instance 
# #Fetching data via UserID - Parent ID - RESTRICTED USE


# #@csrf_exempt
# def user_type_list(request):

#     if request.method == 'GET':
#         user_type = UserType.objects.all()
#         serializer = UserTypeSerializer(user_type, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         serializer = UserTypeSerializer(data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# #@csrf_exempt
# def user_type_detail(request, pk):


#     try:
#         user_type = UserType.objects.get(user_ID=pk)
    
#     except UserType.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         return JsonResponse(UserTypeSerializer(user_type).data)

#     elif request.method == 'PUT':
#         serializer = UserTypeSerializer(user_type, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         user_type.delete()
#         return HttpResponse(status=204)




# #Fetching data via User_AddressID - Child Table ID - FREE USE

# #@csrf_exempt
# def child_type_detail(request, pk):


#     try:
#         user_type = UserType.objects.get(pk=pk)
    
#     except UserType.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         return JsonResponse(UserTypeSerializer(user_type).data)

#     elif request.method == 'PUT':
#         serializer = UserTypeSerializer(user_type, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         user_type.delete()
#         return HttpResponse(status=204)



# #------------------------------------------------------------------------------------


# #Chat Room Model Instance 
# #No primary ket attached to this table
# #Fetching data by ChatRoomID, simply  


# #@csrf_exempt
# def chat_room_list(request):

#     if request.method == 'GET':
#         chat_room_type = ChatRoom.objects.all()
#         serializer = ChatRoomSerializer(chat_room_type, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         serializer = ChatRoomSerializer(data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# #@csrf_exempt
# def chat_room_detail(request, pk):


#     try:
#         chat_room_type = ChatRoom.objects.get(pk=pk)
    
#     except ChatRoom.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         return JsonResponse(ChatRoomSerializer(chat_room_type).data)

#     elif request.method == 'PUT':
#         serializer = ChatRoomSerializer(chat_room_type, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         chat_room_type.delete()
#         return HttpResponse(status=204)

# #------------------------------------------------------------------------------------


# #Particpant Model Instance 
# #Fetching data via chat_room_ID - Parent ID - FREE USE
# #The code can be replicated for fetching via:  User_ID as well - but thats restricted.


# #@csrf_exempt
# def participant_list(request):

#     if request.method == 'GET':
#         participant = Particpant.objects.all()
#         serializer = ParticpantSerializer(participant, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         serializer = ParticpantSerializer(data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# #@csrf_exempt
# def participant_detail(request, pk):


#     try:
#         participant = Particpant.objects.get(chat_room_ID=pk)
    
#     except Particpant.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         return JsonResponse(ParticpantSerializer(participant).data)

#     elif request.method == 'PUT':
#         serializer = ParticpantSerializer(participant, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         participant.delete()
#         return HttpResponse(status=204)




# #----------------------------------------------------------------------------------

# #Message Model Instance 
# #Fetching data via messageID - Child ID - FREE USE
# #The code can be replicated for fetching via:  User_ID as well 
# #many messageIDs can have same UserID or ChatRoomID - So, iterate via messageID

# # #LONG VERSION of the code -- allows more customization  
# # #@csrf_exempt
# # @api_view(['GET', 'POST'])
# # def message_list(request, format=None):
    
# #     if request.method == 'GET':
# #         message = Message.objects.all()
# #         serializer = MessageSerializer(message, many=True)
# #         return Response(serializer.data)
    
# #     elif request.method == 'POST':
# #         serializer = MessageSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# # #@csrf_exempt
# # @api_view(['GET', 'PUT', 'DELETE'])
# # def message_detail(request, pk, format=None):
    
# #     try:
# #         message = Message.objects.get(pk=pk)
# #     except Message.DoesNotExist:
# #         return Response(status=status.HTTP_404_NOT_FOUND)
    
# #     if request.method == 'GET':
# #         serializer = MessageSerializer(message)
# #         return Response(serializer.data)
    
# #     elif request.method == 'PUT':
# #         serializer = MessageSerializer(message, data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# #     elif request.method == 'DELETE':
# #         message.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)
    
   


# #----------------------------------------------------------------------------------

# #Product Category Model Instance 
# #Fetching data via ProductCategoryID - Child ID - FREE USE
# #No FK relationships here to worry about.


# #@csrf_exempt
# def product_category_list(request):

#     if request.method == 'GET':
#         product_category = ProductCategory.objects.all()
#         serializer = ProductCategorySerializer(product_category, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         serializer = ProductCategorySerializer(data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# #@csrf_exempt
# def product_category_detail(request, pk):


#     try:
#         product_category = ProductCategory.objects.get(pk=pk)
    
#     except ProductCategory.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         return JsonResponse(ProductCategorySerializer(product_category).data)

#     elif request.method == 'PUT':
#         serializer = ProductCategorySerializer(product_category, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         product_category.delete()
#         return HttpResponse(status=204)





# #----------------------------------------------------------------------------------

# #Product Theme Model Instance 
# #Fetching data via ProductThemeID - Child ID - FREE USE
# #No FK relationships here to worry about.


# #@csrf_exempt
# def product_theme_list(request):

#     if request.method == 'GET':
#         product_theme = ProductThemes.objects.all()
#         serializer = ProductThemesSerializer(product_theme, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         serializer = ProductThemesSerializer(data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# #@csrf_exempt
# def product_theme_detail(request, pk):


#     try:
#         product_theme = ProductThemes.objects.get(pk=pk)
    
#     except ProductThemes.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         return JsonResponse(ProductThemesSerializer(product_theme).data)

#     elif request.method == 'PUT':
#         serializer = ProductThemesSerializer(product_theme, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         product_theme.delete()
#         return HttpResponse(status=204)





# #----------------------------------------------------------------------------------

# #Discount Model Instance 
# #Fetching data via DiscountID - Child ID - FREE USE
# #One FK with MetaUser --> But read_only is sufficient.


# #@csrf_exempt
# def discount_list(request):

#     if request.method == 'GET':
#         discount = Discount.objects.all()
#         serializer = DiscountSerializer(discount, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         serializer = DiscountSerializer(data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# #@csrf_exempt
# def discount_detail(request, pk):


#     try:
#         discount = Discount.objects.get(pk=pk)
    
#     except Discount.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         return JsonResponse(DiscountSerializer(discount).data)

#     elif request.method == 'PUT':
#         serializer = DiscountSerializer(discount, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         discount.delete()
#         return HttpResponse(status=204)





# #----------------------------------------------------------------------------------

# #Social Model Instance 
# #Fetching data via SocialID - Child ID - FREE USE
# #One FK with MetaUser --> use metauser_social/<parent_ID=pk>/ to access via UserID
# #But access via UserID is RESTRCITED ACCESS - We onky want one source of manipulation for MetaUser 


# #@csrf_exempt
# def social_list(request):

#     if request.method == 'GET':
#         social = Social.objects.all()
#         serializer = SocialSerializer(social, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         serializer = SocialSerializer(data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# #@csrf_exempt
# def social_detail(request, pk):


#     try:
#         social = Social.objects.get(pk=pk)
    
#     except Social.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         return JsonResponse(SocialSerializer(social).data)

#     elif request.method == 'PUT':
#         serializer = SocialSerializer(social, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         social.delete()
#         return HttpResponse(status=204)



# #Fetching data via User_ID - Parent Table ID - RESTRICTED USE

# #@csrf_exempt
# def parent_social_detail(request, pk):


#     try:
#         social = Social.objects.get(user_ID=pk)
    
#     except Social.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         return JsonResponse(SocialSerializer(social).data)

#     elif request.method == 'PUT':
#         serializer = SocialSerializer(social, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         social.delete()
#         return HttpResponse(status=204)




# #----------------------------------------------------------------------------------

# #Shop Model Instance 
# #Fetching data via ShopID - Child ID - FREE USE
# #One FK with MetaUser --> use metauser_shop/<parent_ID=pk>/ to access via UserID
# #But access via UserID is RESTRCITED ACCESS - We onky want one source of manipulation for MetaUser - For security purposes


# #@csrf_exempt
# def shop_list(request):

#     if request.method == 'GET':
#         shop = Shop.objects.all()
#         serializer = ShopSerializer(shop, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         serializer = ShopSerializer(data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# #@csrf_exempt
# def shop_detail(request, pk):


#     try:
#         shop = Shop.objects.get(pk=pk)
    
#     except Shop.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         return JsonResponse(ShopSerializer(shop).data)

#     elif request.method == 'PUT':
#         serializer = ShopSerializer(shop, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         shop.delete()
#         return HttpResponse(status=204)



# #Fetching data via User_ID - Parent Table ID - RESTRICTED USE

# #@csrf_exempt
# def parent_shop_detail(request, pk):


#     try:
#         shop = Shop.objects.get(user_ID=pk)
    
#     except Shop.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         return JsonResponse(ShopSerializer(shop).data)

#     elif request.method == 'PUT':
#         serializer = ShopSerializer(shop, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         shop.delete()
#         return HttpResponse(status=204)


# #----------------------------------------------------------------------------------

# #Product MetaData Instance 
# #@csrf_exempt
# def product_metadata_list(request):

#     if request.method == 'GET':
#         product_metadata = ProductMetaData.objects.all()
#         serializer = ProductMetaDataSerializer(product_metadata, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         serializer = ProductMetaDataSerializer(data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# #@csrf_exempt
# def product_metadata_detail(request, pk):


#     try:
#         product_metadata = ProductMetaData.objects.get(pk=pk)
    
#     except ProductMetaData.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         return JsonResponse(ProductMetaDataSerializer(product_metadata).data)

#     elif request.method == 'PUT':
#         serializer = ProductMetaDataSerializer(product_metadata, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         product_metadata.delete()
#         return HttpResponse(status=204)


# #----------------------------------------------------------------------------------

# #Product Model Instance 
# #Fetching data via ProductID - Child ID - FREE USE - syntax: bodega-api/product/1/
# #5 FK's - user_ID, product_categoryID, product_themesID, discount_ID, shop_ID
# #Access Shop by user_ID and shop_ID as well
# #Syntax1: bodega-api/product/user_ID=<int:pk>/
# #Syntax2: bodega-api/product/shop_ID=<int:pk>
# #These endpoints can be coded later - they need few edits to QuerySet - but this is not urgent  


# #@csrf_exempt
# def product_list(request):

#     if request.method == 'GET':
#         product = Product.objects.all()
#         serializer = ProductSerializer(product, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# #@csrf_exempt
# def product_detail(request, pk):


#     try:
#         product = Product.objects.get(pk=pk)
    
#     except Product.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         return JsonResponse(ProductSerializer(product).data)

#     elif request.method == 'PUT':
#         serializer = ProductSerializer(product, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         product.delete()
#         return HttpResponse(status=204)





# #----------------------------------------------------------------------------------

# #Collaboration Model Instance 
# #Fetching data via CollaborationID - Child ID - FREE USE - syntax: bodega-api/collaboration/1/



# #@csrf_exempt
# def collaboration_list(request):

#     if request.method == 'GET':
#         collaboration = Collaboration.objects.all()
#         serializer = CollaborationSerializer(collaboration, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         serializer = CollaborationSerializer(data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# #@csrf_exempt
# def collaboration_detail(request, pk):


#     try:
#         collaboration = Collaboration.objects.get(pk=pk)
    
#     except Collaboration.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         return JsonResponse(CollaborationSerializer(collaboration).data)

#     elif request.method == 'PUT':
#         serializer = CollaborationSerializer(collaboration, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         collaboration.delete()
#         return HttpResponse(status=204)



# #Shopping Session Views 
# #@csrf_exempt
# def shopping_session_list(request):

#     if request.method == 'GET':
#         shopping_session = ShoppingSession.objects.all()
#         serializer = ShoppingSessionSerializer(shopping_session, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         serializer = ShoppingSessionSerializer(data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# #@csrf_exempt
# def shopping_session_detail(request, pk):


#     try:
#         shopping_session = ShoppingSession.objects.get(pk=pk)
    
#     except ShoppingSession.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         return JsonResponse(ShoppingSessionSerializer(shopping_session).data)

#     elif request.method == 'PUT':
#         serializer = ShoppingSessionSerializer(shopping_session, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         shopping_session.delete()
#         return HttpResponse(status=204)






# #Cart Item Views 
# #@csrf_exempt
# def cart_item_list(request):

#     if request.method == 'GET':
#         cart_item = CartItem.objects.all()
#         serializer = CartItemSerializer(cart_item, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         serializer = CartItemSerializer(data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)




# #@csrf_exempt
# def cart_item_detail(request, pk):


#     try:
#         cart_item = CartItem.objects.get(pk=pk)
    
#     except CartItem.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         return JsonResponse(CartItemSerializer(cart_item).data)

#     elif request.method == 'PUT':
#         serializer = CartItemSerializer(cart_item, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         cart_item.delete()
#         return HttpResponse(status=204)




# #Order Detail Views 
# #@csrf_exempt
# def order_detail_list(request):

#     if request.method == 'GET':
#         order_detail = OrderDetail.objects.all()
#         serializer = OrderDetailsSerializer(order_detail, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         serializer = OrderDetailsSerializer(data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# #@csrf_exempt
# def order_detail_detail(request, pk):


#     try:
#         order_detail = OrderDetail.objects.get(pk=pk)
    
#     except OrderDetail.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         return JsonResponse(OrderDetailsSerializer(order_detail).data)

#     elif request.method == 'PUT':
#         serializer = OrderDetailsSerializer(order_detail, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         order_detail.delete()
#         return HttpResponse(status=204)







# #Order Item Views 
# #@csrf_exempt
# def order_item_list(request):

#     if request.method == 'GET':
#         order_item = OrderItem.objects.all()
#         serializer = OrderItemSerializer(order_item, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         serializer = OrderItemSerializer(data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# #@csrf_exempt
# def order_item_detail(request, pk):


#     try:
#         order_item = OrderItem.objects.get(pk=pk)
    
#     except OrderItem.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         return JsonResponse(OrderItemSerializer(order_item).data)

#     elif request.method == 'PUT':
#         serializer = OrderItemSerializer(order_item, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         order_item.delete()
#         return HttpResponse(status=204)
    
    
    


# #SysOpsAgent Views
# #@csrf_exempt
# def sysops_agent_list(request):

#     if request.method == 'GET':
#         sysops_agent = SysOpsAgent.objects.all()
#         serializer = SysOpsAgentSerializer(sysops_agent, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         serializer = SysOpsAgentSerializer(data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# #@csrf_exempt
# def sysops_agent_detail(request, pk):


#     try:
#         sysops_agent = SysOpsAgent.objects.get(pk=pk)
    
#     except SysOpsAgent.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         return JsonResponse(SysOpsAgentSerializer(sysops_agent).data)

#     elif request.method == 'PUT':
#         serializer = SysOpsAgentSerializer(sysops_agent, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         sysops_agent.delete()
#         return HttpResponse(status=204)
    
    
    
    




# #SysOpsAgent Repo Views
# #@csrf_exempt
# def sysops_agent_repo_list(request):

#     if request.method == 'GET':
#         sysops_agent_repo = SysOpsAgentRepo.objects.all()
#         serializer = SysOpsAgentRepoSerializer(sysops_agent_repo, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         serializer = SysOpsAgentRepoSerializer(data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# #@csrf_exempt
# def sysops_agent_repo_detail(request, pk):


#     try:
#         sysops_agent_repo = SysOpsAgentRepo.objects.get(pk=pk)
    
#     except SysOpsAgentRepo.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         return JsonResponse(SysOpsAgentRepoSerializer(sysops_agent_repo).data)

#     elif request.method == 'PUT':
#         serializer = SysOpsAgentRepoSerializer(sysops_agent_repo, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         sysops_agent_repo.delete()
#         return HttpResponse(status=204)
    
    
    




# #SysOpsAgent Project Views
# #@csrf_exempt
# def sysops_agent_project_list(request):

#     if request.method == 'GET':
#         sysops_agent_project = SysOpsProject.objects.all()
#         serializer = SysOpsProjectSerializer(sysops_agent_project, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         serializer = SysOpsProjectSerializer(data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# #@csrf_exempt
# def sysops_agent_project_detail(request, pk):


#     try:
#         sysops_agent_project = SysOpsProject.objects.get(pk=pk)
    
#     except SysOpsProject.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         return JsonResponse(SysOpsProjectSerializer(sysops_agent_project).data)

#     elif request.method == 'PUT':
#         serializer = SysOpsProjectSerializer(sysops_agent_project, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         sysops_agent_project.delete()
#         return HttpResponse(status=204)
    
    
    
    


# #SysOpsDemandNode Views
# #@csrf_exempt
# def sysopsdemandnode_list(request):

#     if request.method == 'GET':
#         sysopsdemandnode = SysOpsDemandNode.objects.all()
#         serializer = SysOpsDemandNodeSerializer(sysopsdemandnode, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         serializer = SysOpsDemandNodeSerializer(data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# #@csrf_exempt
# def sysopsdemandnode_detail(request, pk):


#     try:
#         sysopsdemandnode = SysOpsDemandNode.objects.get(pk=pk)
    
#     except SysOpsDemandNode.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         return JsonResponse(SysOpsDemandNodeSerializer(sysopsdemandnode).data)

#     elif request.method == 'PUT':
#         serializer = SysOpsDemandNodeSerializer(sysopsdemandnode, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         sysopsdemandnode.delete()
#         return HttpResponse(status=204)
    
    
    
    



# #SysOpsSupplyNode Views
# #@csrf_exempt
# def sysopssupplynode_list(request):

#     if request.method == 'GET':
#         sysopssupplynode = SysOpsSupplyNode.objects.all()
#         serializer = SysOpsSupplyNodeSerializer(sysopssupplynode, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         serializer = SysOpsSupplyNodeSerializer(data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# #@csrf_exempt
# def sysopssupplynode_detail(request, pk):


#     try:
#         sysopssupplynode = SysOpsSupplyNode.objects.get(pk=pk)
    
#     except SysOpsSupplyNode.DoesNotExist:
#         return JsonResponse(status=404)

#     if request.method == 'GET':
#         return JsonResponse(SysOpsSupplyNodeSerializer(sysopssupplynode).data)

#     elif request.method == 'PUT':
#         serializer = SysOpsSupplyNodeSerializer(sysopssupplynode, data=JSONParser().parse(request))
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         sysopssupplynode.delete()
#         return HttpResponse(status=204)
    
    
# #login api, error handling, file, signup pass