from dataclasses import fields
from pyexpat import model
from attr import field
from django.contrib.auth.models import User, Group
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
        fields = ['id', 'metauserID','number']
        
#Solomon Serializer Class
class SolomonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solomonv0
        fields = ['id', 'psy_traits', 'engagement_traits', 'created_at', 'modified_at']

#BLASerializer Class
class BLASerializer(serializers.ModelSerializer):
    class Meta:
        model = BLAScore
        fields = ['id', 'metauserID', 'levelID', 'ReviewCycleNo','current_score', 'predicted_score', 'created_at', 'modified_at']

#Sentino Item Proximity Class
class SentinoItemProximitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SentinoItemProximity
        fields = ['id', 'content_metadata', 'content_metadata2','content_metadata3', 'syslog_metadata', 'self_statements','created_at', 'modified_at']

#Sentino Item Projection Class 
class SentinoItemProjectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentinoItemProjection
        fields = ['id', 'content_metadata', 'content_metadata2', 'content_metadata3', 'syslog_metadata', 'self_statements','created_at', 'modified_at']
    
        
#Sentino Item Classification Class 
class SentinoItemClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentinoItemClassification
        fields = ['id', 'content_metadata', 'content_metadata2', 'content_metadata3', 'syslog_metadata', 'self_statements','created_at', 'modified_at']

#Sentino Inventory Serializer Class
class SentinoInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SentinoInventory
        fields = ['id', 'content_metadata', 'content_metadata2', 'content_metadata3', 'syslog_metadata', 'self_statements','created_at', 'modified_at']


#Sentino Description Serializer Class
class SentinoDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentinoSelfDescription
        fields = ['id', 'content_metadata', 'content_metadata2', 'content_metadata3', 'syslog_metadata', 'self_statements','created_at', 'modified_at']

#Sentino Profile Serializer Class
class SentinoProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentinoProfile
        fields = ['id', 'content_metadata', 'content_metadata2', 'content_metadata3', 'syslog_metadata', 'self_statements','created_at', 'modified_at']

#Bodega Vision Serializer Class
class BodegaVisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodegaVision
        fields = ['id', 'metauserID','image_metadata','video_metadata','syslog_metadata','created_at', 'modified_at']

#Bodega Face  Serializer Class
class BodegaFaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodegaFace
        fields = ['id', 'metauserID', 'facial_metadata', 'syslog_metadata', 'created_at', 'modified_at']

#Bodega Personalizer Serializer Class
class BodegaPersonalizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodegaPersonalizer
        fields = ['id', 'metauserID', 'content_metadata', 'syslog_metadata', 'created_at', 'modified_at']

#Bodega Cognitive Serializer Class
class BodegaCongnitiveItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodegaCognitiveItem
        fields = ['id', 'metauserID', 'proximityID','classificationID','projectionID', 'self_statements','content_metadata','syslog_metadata','created_at', 'modified_at']

#Bodega Cognitive Inventory Serializer Class
class BodegaCognitiveInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BodegaCognitiveInventory
        fields = ['id', 'metauserID','inventoryID','self_statements','content_metadata','syslog_metadata', 'created_at', 'modified_at']

#Bodega Cognitive Person Serializer Class
class BodegaCognitivePersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodegaCognitivePerson
        fields = ['id', 'metauserID', 'self_descriptionID', 'profileID', 'self_statements', 'content_metadata', 'syslog_metadata', 'created_at', 'modified_at']
#Bodega Dept Serializer Class
class BodegaDeptSerializer(serializers.ModelSerializer):
    class Meta: 
        model = BodegaDept
        fields = ['id', 'metauserID', 'departmentname','content_metadata','created_at', 'modified_at']

#User Address Serializer Class
class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ['id', 'metauserID', 'address_line1','address_line2','address_state','city','postal_code','country', 'created_at', 'modified_at']

#User Payment Serializer Class
class UserPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPayment
        fields = ['id', 'metauserID', 'payment_type', 'stripeAccountID', 'total_money_out','total_money_in', 'user_payment_profile_status', 'created_at', 'modified_at']

#User Type Serializer Class
class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = ['id', 'metauserID', 'bodega_vision_ID','level_ID','solomon_person_ID','user_role','created_at', 'modified_at']

#Chat Room Serializer Class
class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['id', 'name', 'desc', 'rules', 'type_of_room','is_room_active','room_hashkey','created_on', 'modified_on']

#ParticpantSerializer Class
class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['id', 'metauserID', 'chat_room_ID']

#Message Serializer Class
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'chat_room_ID', 'metauserID', 'message_body', 'upload_file', 'created_at', 'modified_at', 'hashkey']

#Product Category Serializer Class
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'category_name', 'category_desc', 'category_image1', 'category_image2', 'category_image3', 'created_at', 'modified_at']

#Product Themes Serializer Class
class BoostTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoostTags
        fields = '__all__'

#Discount Serializer Class
class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['id','name', 'description','discount_percent', 'active_status','created_by','created_at', 'modified_at']

#Social Serializer Class
class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ['id', 'metauserID', 'following','followers','makeprofileprivate','saved_content','likes','dislikes','comments', 'products_clickedOn', 'bio', 'blocked_list', 'data_mining_status', 'account_active', 'delete_metauser', 'created_on', 'modified_on']

#Shop Serializer Class
class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'metauserID', 'all_products', 'all_user_data', 'name', 'description', 'logo', 'cover_image', 'address_line1', 'address_line2', 'city', 'state', 'postal_code', 'country','bodega_vision_tags', 'bodega_customer_tags', 'uniquesellingprop', 'data_mining_status', 'created_on', 'modified_on']
        
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
        model = Collaboration
        fields = '__all__'

#Shopping Session Serializer Class  
class ShoppingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingSession
        fields = ['id', 'metauserID', 'total_amount', 'created_at', 'modified_at']

#Cart Item Serializer Class
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCartItem
        fields = ['id', 'metauserID', 'product_ID', 'quantity', 'created_at', 'modified_at']

#Order Details Serializer Class
class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ['id', 'total_amount', 'payment_info','created_at', 'modified_at'] 

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



#Shop Payout Serializer Class -- Not completed

#SysOps Agent Serializer Class
class SysOpsAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysOpsAgent
        fields = ['id', 'metauserID', 'levelID', 'departmentID', 'agent_hashkey', 'bio', 'reporting_officer', 'created_at', 'modified_at']

#SysOps Agent Repo Serializer Class
class SysOpsAgentRepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysOpsAgentRepo
        fields = ['id', 'metauserID', 'sysops_agentID', 'project_hashkey', 'created_at', 'modified_at']

#SysOps Product Serializer Class
class SysOpsProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysOpsProject
        fields = ['id', 'owner_metauserID', 'owner_agentID', 'levelID', 'divisionID','name', 'problem_statement', 'problem_impact_size', 'hypothesis', 'key_performance_indicators', 'status', 'ttc_hours','allocated_ttc_hours','tasks', 'team_hashkey_json','hashkey', 'genesis_project_hashkey', 'parent_project_hashkey', 'child_project_hashkey', 'created_at', 'modified_at']

#SysOps Supply Node Serializer Class
class SysOpsSupplyNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysOpsSupplyNode
        fields = ['id', 'supply_metauserID','supply_shopID', 'bla_ScoreID', 'opsec_agent_hashkey', 'name', 'location', 'status', 'tokens_allocated', 'creator_hypothesis', 'sysops_agent_hypothesis', 'creator_identity_status', 'all_digital_url', 'influence_size','genre', 'category_vertical1', 'category_vertical2', 'product_traits', 'creator_traits', 'production_type', 'current_revenue', 'current_aov', 'predicted_revenue', 'creator_audience_traits', 'sysops_solution_hypothesis', 'additional_notes', 'created_at', 'modified_at']

#SysOps Demand Node Serializer Class
class SysOpsDemandNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysOpsDemandNode
        fields = ['id', 'demand_metauserID', 'bla_ScoreID', 'opsec_agent_hashkey','name', 'location','status', 'tokens_allocated','creator_hypothesis','sysops_agent_hypothesis','creator_identity_status','all_digital_url','influence_size','genre','category_vertical', 'category_vertical2', 'product_traits', 'creator_traits', 'production_type', 'current_revenue','predicted_revenue', 'creator_audience_traits','sysops_solution_hypothesis','additional_notes','created_at','modified_at']


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

