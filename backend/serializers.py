


from .models import *
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator



# Serializer Class for Developers
# wherever possible, apply constraints
# GET functions arent defined explicitly because we are just reading data - so no corruption can be done

# validated_data = data which needs to be requested or posted
# instance = this is the instance of the model with pk=id

collab_type_array = [
    # the bid our creator wants to do but depends on mutual consent of other party - because freedom of fucking choice
    ('FIXED-PAYMENT', 'FIXED-PAYMENT'),
    ('BARTER-DEAL', 'BARTER-DEAL'),
    ('COMMISSION-%-ON-SALES', 'COMMISSION-%-ON-SALES'),
    ('FREE-HELP-FROM-THE-COMMUNITY', 'FREE-HELP-FROM-THE-COMMUNITY')
]

marketing_funnel_array = [
    ('Community', 'Creator-Community'),
    ('Performance-ADs', 'Performance-ADs-IG/FB'),
    ('Influencer-Marketing', 'Influencer-Marketing'),
]

country_list = [
    ('INDIA', 'IN'),
    ('USA', 'US'),
]

payment_types = [
    ('DEBIT/CREDIT-CARD', 'DEBIT/CREDIT-CARD'),
    ('PAYPAL', 'PAYPAL'),

    ('CRYPTO(BETA)', 'CRYPTO(BETA)')
]

user_role_array = [
    ('Creator', 'Creator'),
    ('Business', 'Business'),
    ('Bodega-Community-Member', 'Bodega-Community-Member'),
]
type_of_room_array = [
    # only people with meta_key can join the secure_room
    ('CLOSED-SECURE-ROOM', 'CLOSED-SECURE-ROOM'),
    ('OPEN-SECURE-ROOM', 'OPEN-SECURE-ROOM'),  # anyone can join the secure room
    # leads ro the deletion of the room
    ('INITIATE-ROOM-TERMINATION', 'INITIATE-ROOM-TERMINATION')
]
# Before deployment -> use this link for data: https://github.com/hampusborgos/country-flags/blob/main/countries.json

ProductCategory_array = [
    ('SHIRTS', 'SHIRTS'),
    ('BOTTOMS', 'BOTTOMS'),
    ('SNEAKERS', 'SNEAKERS'),
    ('THERMALS', 'THERMALS'),
    ('SHORTS', 'SHORTS'),
    ('HOME-DECOR', 'HOME-DECOR'),
    ('DIGITAL-ART', 'DIGITAL-ART'),
    ('MUSIC-FILE', 'MUSIC-FILE'),
    ('COLLECTIBLES', 'COLLECTIBLES'),
    ('PHYSICAL-ACCESSORIES', 'PHYSICAL-ACCESSORIES'),
    ('DIGITAL-ACCESSORIES', 'DIGITAL-ACCESSORIES'),
    ('POTRAIT-VIDEO-FILE', 'POTRAIT-VIDEO-FILE'), ]



#BDGMRKT API / SERIALIZER CODE V2.0.0


#Pocket Serializer Classes
#These Serializer functions are used to do quick read-only data processing
#MetaUser Serializer Class
class MetaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaUser
        fields = '__all__'

#MetaUser Auth Serializer 
class MetaUserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaUser
        fields = ['id', 'meta_username', 'passcode', 'public_hashkey']


class MetaUserTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaUserTags
        fields = '__all__'


#Shop Serializer 
class ShopMetaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'metauserID', 'all_products', 'all_user_data', 'name', 'description', 'logo', 'cover_image', 'address_line1','address_state', 'address_line2', 'city', 'state', 'postal_code', 'country','bodega_vision_tags', 'bodega_customer_tags', 'uniquesellingprop', 'data_mining_status', 'created_on', 'modified_on']

#KillSwitch Serializer
class KillSwitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaUser
        fields = ['id', 'meta_username', 'passcode', 'private_hashkey', 'public_hashkey']


#Level Serializer Class
class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'
        
#Solomon Serializer Class
class SolomonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solomonv0
        fields = '__all__'

#BLASerializer Class
class BLASerializer(serializers.ModelSerializer):
    class Meta:
        model = BLAScore
        fields = '__all__'

#Sentino Item Proximity Class
class SentinoItemProximitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SentinoItemProximity
        fields = '__all__'

#Sentino Item Projection Class 
class SentinoItemProjectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentinoItemProjection
        fields = '__all__'
    
        
#Sentino Item Classification Class 
class SentinoItemClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentinoItemClassification
        fields = '__all__'

#Sentino Inventory Serializer Class
class SentinoInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SentinoInventory
        fields = '__all__'


#Sentino Description Serializer Class
class SentinoDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentinoSelfDescription
        fields = '__all__'

#Sentino Profile Serializer Class
class SentinoProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentinoProfile
        fields = '__all__'

#Bodega Vision Serializer Class
class BodegaVisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodegaVision
        fields = '__all__'

#Bodega Face  Serializer Class
class BodegaFaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodegaFace
        fields = '__all__'

#Bodega Personalizer Serializer Class
class BodegaPersonalizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodegaPersonalizer
        fields = '__all__'

#Bodega Cognitive Serializer Class
class BodegaCongnitiveItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodegaCognitiveItem
        fields = '__all__'

#Bodega Cognitive Inventory Serializer Class
class BodegaCognitiveInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BodegaCognitiveInventory
        fields = '__all__'

#Bodega Cognitive Person Serializer Class
class BodegaCognitivePersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodegaCognitivePerson
        fields = '__all__'
#Bodega Dept Serializer Class
class BodegaDeptSerializer(serializers.ModelSerializer):
    class Meta: 
        model = BodegaDept
        fields = '__all__'

#User Address Serializer Class
class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = '__all__'

#User Payment Serializer Class
class UserPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPayment
        fields = '__all__'

#User Type Serializer Class
class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = '__all__'

#Chat Room Serializer Class
class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = '__all__'

#ParticpantSerializer Class
class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'

#Message Serializer Class
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

#Product Category Serializer Class
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

#Product Themes Serializer Class
class BoostTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoostTags
        fields = '__all__'

#Discount Serializer Class
class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

#Social Serializer Class
class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'

#Shop Serializer Class
class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
        
#Product MetaData Serializer Class
class ProductMetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMetaData
        fields = '__all__'

#Product Serializer Class
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventory
        fields = '__all__'

#Munchies Page Serializer Classes
class MunchiesPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MunchiesPage
        fields = '__all__'

#Munchies Page Video Serializer Classes 
class MunchiesVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MunchiesVideo
        fields = '__all__'


#Collaboration Serializer Class
class CollaborationSerializer(serializers.ModelSerializer):
    class Meta:
        model = yerrrCollaboration
        fields = '__all__'

#Shopping Session Serializer Class  
class ShoppingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingSession
        fields = '__all__'

#Cart Item Serializer Class
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCartItem
        fields = '__all__'

#Order Details Serializer Class
class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'

#Order Items Serializer Class
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

#Order Success Serializer Class
class OrderSuccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderSuccess
        fields = '__all__'

#Order Failure Serializer Class
class OrderFailureSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderFailure
        fields = '__all__'


class OrderLedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderLedger
        fields = '__all__'


#Shop Payout Serializer Class -- Not completed

#SysOps Agent Serializer Class
class SysOpsAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysOpsAgent
        fields = '__all__'

#SysOps Agent Repo Serializer Class
class SysOpsAgentRepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysOpsAgentRepo
        fields = '__all__'

#SysOps Product Serializer Class
class SysOpsProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysOpsProject
        fields = '__all__'

#SysOps Supply Node Serializer Class
class SysOpsSupplyNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysOpsSupplyNode
        fields = '__all__'

#SysOps Demand Node Serializer Class
class SysOpsDemandNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysOpsDemandNode
        fields = '__all__'


#Stripe Account Info Serializer Classes
class stripeAccountInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = stripeAccountInfo
        fields = '__all__'

#Stripe Account Transfer Serializer Class 
class stripeAccountTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = stripeAccountTransfer
        fields = '__all__'


#Stripe Charges Serializer Class
class stripeChargesSerializer(serializers.ModelSerializer):
    class Meta:
        model = stripeCharges
        fields = '__all__'


#Stripe Subscription Serializer Class
class creatorSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = creatorSubscription
        fields = '__all__'

#All Subscribers Serializer Classes
class subscribersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribers
        fields ='__all__'



#Serializer Class for Notifications Model Instance 
#The Notification model will be instantiated all over the program to run it in sync 
class notificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = '__all__'


class bodegaCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customerPayment
        fields = '__all__'

class cashFlowLedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashFlowLedger
        fields = '__all__'



class SentinoItemClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentinoItemClassification
        fields = '__all__'

class BodegaCognitiveItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodegaCognitiveItem
        fields = '__all__'


class bodegaSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = bodegaSocial
        fields = '__all__'

class bodegaSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = bodegaSupport
        fields = '__all__'


class contentPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = contentPage
        fields = '__all__'

class collectionPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = collectionPage
        fields = '__all__'

class textPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = textPage
        fields = '__all__'


class navigationBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = navigationBar
        fields = '__all__'

class footerBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = footerBar
        fields = '__all__'


class websiteSiteMapConfigSerializer(serializers.ModelSerializer): 
    class Meta:
        model = websiteSiteMapConfig
        fields = '__all__'


class collectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'

class MetaUserAccountStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaUserAccountStatus
        fields = '__all__'
