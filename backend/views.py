from dataclasses import fields
from locale import currency
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
    #return Response(data=transferFunds, status=200)


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
    stripeCharge = stripe.Charge.create(
                                        amount=request.data['amount'], 
                                        currency=request.data['currency'], 
                                        source='tok_visa', 
                                        description=request.data['description']
    )
    stripeCustomer = stripe.Customer.create()

    try:
        chargeObject=stripeCharges.objects.create(amount=request.data['amount'], 
                                                        currency=request.data['currency'],
                                                        description=request.data['description'],
                                                        stripeAccountInfoID = stripeAccountInfo.objects.get(pk=request.data['stripeAccountInfoID']),
                                                        stripeChargeID = stripeCharge.id, 
                                                        capturedStatus=stripeCharge.captured,
                                                        riskScore=stripeCharge.outcome['risk_score'], 
                                                        last4=stripeCharge.source['last4'], 
                                                        paymentStatus=True, 
                                                        stripeCustomerID = stripeCustomer.id)
        serializer = stripeChargesSerializer(chargeObject)
        return Response (serializer.data, status=200)
    except:
        return Response(data="Payment Failed", status=200)
    
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

    return Response(data=modifiedCustomer, status=200)






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