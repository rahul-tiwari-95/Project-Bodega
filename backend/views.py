from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
import datetime
from django.utils import timezone
import requests



from backend.models import MetaUser, User_Address, User_Payment, User_Type, Chat_Room, Particpant, Message, Product_Category, Product_Themes, Discount, Social, Shop_Payout, Shop, Product,  Collaboration
from backend.serializers import MetaUserSerializer, UserAddressSerializer, UserPaymentSerializer, UserTypeSerializer, ChatRoomSerializer, ParticpantSerializer, MessageSerializer, ProductCategorySerializer, ProductThemesSerializer, DiscountSerializer, SocialSerializer, ShopSerializer, ProductSerializer, CollaborationSerializer



#HTML files for Bodega Landing Page

def landing_page(request):
    metausers = MetaUser.objects.all()
    time = timezone.now()
    kanye = requests.get('https://api.kanye.rest')
    kanye = kanye.text
    return render(request, 'backend/landingpage.html', {'metausers': metausers, 'time':time, 'kanye': kanye})


@csrf_exempt
def metauser_list(request):
    #GET, POST request for metauser/
    if request.method == 'GET':
        metauser = MetaUser.objects.all()
        serializer = MetaUserSerializer(metauser, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MetaUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)

    


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




#Fetching data via UserID - Parent ID - RESTRICTED USE


@csrf_exempt
def address_list(request):
    #GET, POST request for metauser_address/
    if request.method == 'GET':
        user_address = User_Address.objects.all()
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
        user_address = User_Address.objects.get(user_ID=pk)
    
    except User_Address.DoesNotExist:
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




#Fetching data via User_AddressID - Child Table ID - FREE USE

@csrf_exempt
def child_address_detail(request, pk):
    #GET, PUT, DELETE requests for metauser_address/

    try:
        user_address = User_Address.objects.get(pk=pk)
    
    except User_Address.DoesNotExist:
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



#-------------------------------------------------------------------------------------------------------------------------------------------------

#User_Payment Model Instance 
#Fetching data via UserID - Parent ID - RESTRICTED USE


@csrf_exempt
def user_payment_list(request):
    #GET, POST request for metauser_address/
    if request.method == 'GET':
        user_payment = User_Payment.objects.all()
        serializer = UserPaymentSerializer(user_payment, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = UserPaymentSerializer(data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def user_payment_detail(request, pk):
    #GET, PUT, DELETE requests for metauser_address/

    try:
        user_payment = User_Payment.objects.get(user_ID=pk)
    
    except User_Payment.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        return JsonResponse(UserPaymentSerializer(user_payment).data)

    elif request.method == 'PUT':
        serializer = UserPaymentSerializer(user_payment, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user_payment.delete()
        return HttpResponse(status=204)




#Fetching data via User_AddressID - Child Table ID - FREE USE

@csrf_exempt
def child_payment_detail(request, pk):
    #GET, PUT, DELETE requests for metauser_address/

    try:
        user_payment = User_Payment.objects.get(pk=pk)
    
    except User_Payment.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        return JsonResponse(UserPaymentSerializer(user_payment).data)

    elif request.method == 'PUT':
        serializer = UserPaymentSerializer(user_payment, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user_payment.delete()
        return HttpResponse(status=204)



#------------------------------------------------------------------------------------


#User_Payment Model Instance 
#Fetching data via UserID - Parent ID - RESTRICTED USE


@csrf_exempt
def user_type_list(request):

    if request.method == 'GET':
        user_type = User_Type.objects.all()
        serializer = UserTypeSerializer(user_type, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = UserTypeSerializer(data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def user_type_detail(request, pk):


    try:
        user_type = User_Type.objects.get(user_ID=pk)
    
    except User_Type.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        return JsonResponse(UserTypeSerializer(user_type).data)

    elif request.method == 'PUT':
        serializer = UserTypeSerializer(user_type, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user_type.delete()
        return HttpResponse(status=204)




#Fetching data via User_AddressID - Child Table ID - FREE USE

@csrf_exempt
def child_type_detail(request, pk):


    try:
        user_type = User_Type.objects.get(pk=pk)
    
    except User_Type.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        return JsonResponse(UserTypeSerializer(user_type).data)

    elif request.method == 'PUT':
        serializer = UserTypeSerializer(user_type, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user_type.delete()
        return HttpResponse(status=204)



#------------------------------------------------------------------------------------


#Chat Room Model Instance 
#No primary ket attached to this table
#Fetching data by ChatRoomID, simply  


@csrf_exempt
def chat_room_list(request):

    if request.method == 'GET':
        chat_room_type = Chat_Room.objects.all()
        serializer = ChatRoomSerializer(chat_room_type, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = ChatRoomSerializer(data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def chat_room_detail(request, pk):


    try:
        chat_room_type = Chat_Room.objects.get(pk=pk)
    
    except Chat_Room.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        return JsonResponse(ChatRoomSerializer(chat_room_type).data)

    elif request.method == 'PUT':
        serializer = ChatRoomSerializer(chat_room_type, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        chat_room_type.delete()
        return HttpResponse(status=204)

#------------------------------------------------------------------------------------


#Particpant Model Instance 
#Fetching data via chat_room_ID - Parent ID - FREE USE
#The code can be replicated for fetching via:  User_ID as well - but thats restricted.


@csrf_exempt
def participant_list(request):

    if request.method == 'GET':
        participant = Particpant.objects.all()
        serializer = ParticpantSerializer(participant, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = ParticpantSerializer(data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def participant_detail(request, pk):


    try:
        participant = Particpant.objects.get(chat_room_ID=pk)
    
    except Particpant.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        return JsonResponse(ParticpantSerializer(participant).data)

    elif request.method == 'PUT':
        serializer = ParticpantSerializer(participant, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        participant.delete()
        return HttpResponse(status=204)




#----------------------------------------------------------------------------------

#Message Model Instance 
#Fetching data via messageID - Child ID - FREE USE
#The code can be replicated for fetching via:  User_ID as well 
#many messageIDs can have same UserID or ChatRoomID - So, iterate via messageID


@csrf_exempt
def message_list(request):

    if request.method == 'GET':
        message = Message.objects.all()
        serializer = MessageSerializer(message, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = MessageSerializer(data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def message_detail(request, pk):


    try:
        message = Message.objects.get(pk=pk)
    
    except Message.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        return JsonResponse(MessageSerializer(message).data)

    elif request.method == 'PUT':
        serializer = MessageSerializer(message, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        message.delete()
        return HttpResponse(status=204)



#----------------------------------------------------------------------------------

#Product Category Model Instance 
#Fetching data via ProductCategoryID - Child ID - FREE USE
#No FK relationships here to worry about.


@csrf_exempt
def product_category_list(request):

    if request.method == 'GET':
        product_category = Product_Category.objects.all()
        serializer = ProductCategorySerializer(product_category, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = ProductCategorySerializer(data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def product_category_detail(request, pk):


    try:
        product_category = Product_Category.objects.get(pk=pk)
    
    except Product_Category.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        return JsonResponse(ProductCategorySerializer(product_category).data)

    elif request.method == 'PUT':
        serializer = ProductCategorySerializer(product_category, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product_category.delete()
        return HttpResponse(status=204)





#----------------------------------------------------------------------------------

#Product Theme Model Instance 
#Fetching data via ProductThemeID - Child ID - FREE USE
#No FK relationships here to worry about.


@csrf_exempt
def product_theme_list(request):

    if request.method == 'GET':
        product_theme = Product_Themes.objects.all()
        serializer = ProductThemesSerializer(product_theme, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = ProductThemesSerializer(data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def product_theme_detail(request, pk):


    try:
        product_theme = Product_Themes.objects.get(pk=pk)
    
    except Product_Themes.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        return JsonResponse(ProductThemesSerializer(product_theme).data)

    elif request.method == 'PUT':
        serializer = ProductThemesSerializer(product_theme, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product_theme.delete()
        return HttpResponse(status=204)





#----------------------------------------------------------------------------------

#Discount Model Instance 
#Fetching data via DiscountID - Child ID - FREE USE
#One FK with MetaUser --> But read_only is sufficient.


@csrf_exempt
def discount_list(request):

    if request.method == 'GET':
        discount = Discount.objects.all()
        serializer = DiscountSerializer(discount, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = DiscountSerializer(data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def discount_detail(request, pk):


    try:
        discount = Discount.objects.get(pk=pk)
    
    except Discount.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        return JsonResponse(DiscountSerializer(discount).data)

    elif request.method == 'PUT':
        serializer = DiscountSerializer(discount, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        discount.delete()
        return HttpResponse(status=204)





#----------------------------------------------------------------------------------

#Social Model Instance 
#Fetching data via SocialID - Child ID - FREE USE
#One FK with MetaUser --> use metauser_social/<parent_ID=pk>/ to access via UserID
#But access via UserID is RESTRCITED ACCESS - We onky want one source of manipulation for MetaUser 


@csrf_exempt
def social_list(request):

    if request.method == 'GET':
        social = Social.objects.all()
        serializer = SocialSerializer(social, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = SocialSerializer(data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def social_detail(request, pk):


    try:
        social = Social.objects.get(pk=pk)
    
    except Social.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        return JsonResponse(SocialSerializer(social).data)

    elif request.method == 'PUT':
        serializer = SocialSerializer(social, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        social.delete()
        return HttpResponse(status=204)



#Fetching data via User_ID - Parent Table ID - RESTRICTED USE

@csrf_exempt
def parent_social_detail(request, pk):


    try:
        social = Social.objects.get(user_ID=pk)
    
    except Social.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        return JsonResponse(SocialSerializer(social).data)

    elif request.method == 'PUT':
        serializer = SocialSerializer(social, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        social.delete()
        return HttpResponse(status=204)




#----------------------------------------------------------------------------------

#Shop Model Instance 
#Fetching data via ShopID - Child ID - FREE USE
#One FK with MetaUser --> use metauser_shop/<parent_ID=pk>/ to access via UserID
#But access via UserID is RESTRCITED ACCESS - We onky want one source of manipulation for MetaUser - For security purposes


@csrf_exempt
def shop_list(request):

    if request.method == 'GET':
        shop = Shop.objects.all()
        serializer = ShopSerializer(shop, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = ShopSerializer(data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def shop_detail(request, pk):


    try:
        shop = Shop.objects.get(pk=pk)
    
    except Shop.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        return JsonResponse(ShopSerializer(shop).data)

    elif request.method == 'PUT':
        serializer = ShopSerializer(shop, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        shop.delete()
        return HttpResponse(status=204)



#Fetching data via User_ID - Parent Table ID - RESTRICTED USE

@csrf_exempt
def parent_shop_detail(request, pk):


    try:
        shop = Shop.objects.get(user_ID=pk)
    
    except Shop.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        return JsonResponse(ShopSerializer(shop).data)

    elif request.method == 'PUT':
        serializer = ShopSerializer(shop, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        shop.delete()
        return HttpResponse(status=204)




#----------------------------------------------------------------------------------

#Product Model Instance 
#Fetching data via ProductID - Child ID - FREE USE - syntax: bodega-api/product/1/
#5 FK's - user_ID, product_categoryID, product_themesID, discount_ID, shop_ID
#Access Shop by user_ID and shop_ID as well
#Syntax1: bodega-api/product/user_ID=<int:pk>/
#Syntax2: bodega-api/product/shop_ID=<int:pk>
#These endpoints can be coded later - they need few edits to QuerySet - but this is not urgent  


@csrf_exempt
def product_list(request):

    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def product_detail(request, pk):


    try:
        product = Product.objects.get(pk=pk)
    
    except Product.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        return JsonResponse(ProductSerializer(product).data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=204)




#----------------------------------------------------------------------------------

#Collaboration Model Instance 
#Fetching data via CollaborationID - Child ID - FREE USE - syntax: bodega-api/collaboration/1/



@csrf_exempt
def collaboration_list(request):

    if request.method == 'GET':
        collaboration = Collaboration.objects.all()
        serializer = CollaborationSerializer(collaboration, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = CollaborationSerializer(data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def collaboration_detail(request, pk):


    try:
        collaboration = Collaboration.objects.get(pk=pk)
    
    except Collaboration.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        return JsonResponse(CollaborationSerializer(collaboration).data)

    elif request.method == 'PUT':
        serializer = CollaborationSerializer(collaboration, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        collaboration.delete()
        return HttpResponse(status=204)


