from dataclasses import fields
from pyexpat import model
from django.contrib.auth.models import User, Group
from .models import BLAScore, BodegaCognitiveInventory, BodegaCognitiveItem, BodegaCognitivePerson, BodegaDept, \
    BodegaFace, BodegaPersonalizer, BodegaVision, CartItem, ChatRoom, Collaboration, Discount, Level, MetaUser, \
    OrderDetail, OrderItem, Product, ProductCategory, ProductThemes, ProductMetaData, SentinoInventory, \
    SentinoItemClassification, SentinoItemProjection, SentinoItemProximity, SentinoProfile, \
    SentinoSelfDescription, ShopPayout, ShoppingSession, Social, Shop, Solomonv0, SysOpsAgent, SysOpsDemandNode, SysOpsProject, SysOpsSupplyNode, UserAddress, UserPayment, \
    UserType, Particpant, Message, SysOpsAgentRepo, ShoppingCartItem
from rest_framework import serializers



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


#MetaUser Serializer Class
class MetaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaUser
        fields = ['id', 'meta_username', 'passcode', 'private_hashkey', 'public_hashkey', 'discord_username', 'created_at', 'modified_at']

#MetaUser Auth Serializer 
class MetaUserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaUser
        fields = ['id', 'meta_username', 'public_hashkey']

#MetaUserAuth Serializer TBD - meta_username + public hashkey

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
        fields = ['id', 'metauserID', 'payment_type', 'payment_provider', 'total_money_out','total_money_in', 'user_payment_profile_status', 'created_at', 'modified_at']

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
class ParticpantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Particpant
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
class ProductThemesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductThemes
        fields = ['id', 'collection_name', 'collection_desc', 'audience_traits', 'marketing_funnel','created_at', 'modified_at']

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
        fields = ['id', 'numberoflikes', 'numberofcomments','numberofclicks','totaltimespentonproduct_hours','metauserID_of_likes','metauserID_of_dislikes','metauserID_of_comments', 'total_sales', 'clicks_on_product', 'is_product_digital', 'assistance_ask', 'nsfw_content', 'production_cost', 'production_time_days', 'hours_invested', 'encrypt_product', 'unit_sold_expectation', 'size_chart', 'product_image2', 'product_image3', 'product_image4', 'created_at', 'modified_at']

#Product Serializer Class
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'metauserID', 'productMetaDataID','product_categoryID', 'product_themesID','discount_ID', 'shop_ID','name', 'description','selling_price', 'discounted_price','quantity','is_product_digital','product_image1','hashkey','created_at', 'modified_at']

#Collaboration Serializer Class
class CollaborationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaboration
        fields = ['id', 'name', 'description', 'creator_collab_choice', 'metauserID', 'product_ID', 'shop_ID', 'creator_pitch', 'bid_type', 'bid_amount', 'accept_bid', 'created_at', 'modified_at']

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
        fields = ['id','order_ID','product_ID', 'quantity','created_at', 'modified_at']


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





#BDGMRKT API / SERIALIZER CODE V1.0
#Old code designed for API endpoints  
#the code below can be used for further customization of API endpoints 
#I did not delete the below code because I feel that shows versions of my progress  
#As we march ahead, my code will get more leaner and efficient  - which is the whole purpose of design  

# # Serializer template for MetaUser
# class MetaUserSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     meta_username = serializers.CharField(required=True)
#     passcode = serializers.CharField(required=False, max_length=100)
#     private_hashkey = serializers.CharField(required=False, read_only=True)
#     public_hashkey = serializers.CharField(required=False, read_only=True)
#     discord_username = serializers.CharField(required=False)
#     created_at = serializers.CharField(required=False)
#     modified_at = serializers.CharField(required=False)

#     # creating functions which will execute on Serializers and create model instances.
#     # this allows us to secure the access to db directly.
#     def create(self, validated_data):
#         # Creating new instances of the MetaUser model

#         return MetaUser.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # Updating instances of our model - here instance refers to id number and validated_data refers to body of the instance
#         instance.meta_username = validated_data.get(
#             'meta_username', instance.meta_username)
#         instance.passcode = validated_data.get('passcode', instance.passcode)
#         instance.private_hashkey = validated_data.get(
#             'private_hashkey', instance.private_hashkey)
#         instance.public_hashkey = validated_data.get(
#             'public_hashkey', instance.public_hashkey)
#         instance.discord_username = validated_data.get(
#             'discord_username', instance.discord_username)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Serializer for Level Model
# class LevelSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     metauserID = serializers.PrimaryKeyRelatedField(
#         queryset=MetaUser.objects.all())
#     number = serializers.FloatField(default=3.0)

#     def create(self, validated_data):
#         # Creating new instances of the Level model
#         return Level.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # Updating instances of our model
#         instance.metauserID = validated_data.get(
#             'metauserID', instance.metauserID)
#         instance.number = validated_data.get('number', instance.number)

#         instance.save()
#         return instance


# #Serializer for Solomon Class
# class SolomonSerializer(serializers.Serializer):
#      id = serializers.IntegerField(read_only=True)
#      psy_traits = serializers.CharField(required=False)
#      engagement_traits = serializers.CharField(required=False)
#      created_at = serializers.CharField(required=False)
#      modified_at = serializers.CharField(required=False)


#      def create(self, validated_data):
#          return Solomonv0.objects.create(**validated_data)

#      def update(self, instance, validated_data):
#          #Updating instances of SolomonVo model
#          instance.psy_traits = validated_data.get('psy_traits', instance.psy_traits)
#          instance.engagement_traits = validated_data.get('engagement_traits', instance.engagement_traits)
#          instance.created_at = validated_data.get('created_at', instance.created_at)
#          instance.modified_at = validated_data.get('modified_at', instance.modified_at)

#          instance.save()
#          return instance


# # Serializer for BLAScore Model
# class BLASerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     metauserID = serializers.PrimaryKeyRelatedField(
#         queryset=MetaUser.objects.all())
#     levelID = serializers.PrimaryKeyRelatedField(queryset=Level.objects.all())
#     ReviewCycleNo = serializers.FloatField(default=1.0)
#     current_score = serializers.FloatField(default=3.0)
#     predicted_score = serializers.FloatField(default=3.0)
#     created_at = serializers.CharField(required=False)
#     modified_at = serializers.CharField(required=False)

#     def create(self, validated_data):
#         # Creating new instanced of BLAScore Model
#         return BLAScore.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # updating instances of our model
#         instance.metauserID = validated_data.get(
#             'metauserID', instance.metauserID)
#         instance.levelID = validated_data.get('levelID', instance.levelID)
#         instance.ReviewCycleNo = validated_data.get(
#             'ReviewCycleNo', instance.ReviewCycleNo)
#         instance.current_score = validated_data.get(
#             'current_score', instance.current_score)
#         instance.predicted_score = validated_data.get(
#             'predicted_score', instance.predicted_score)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Serializer for Sentino Item Proximity Model
# class SentinoItemProximitySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     content_metadata = serializers.CharField(required=False)
#     content_metadata2 = serializers.CharField(required=False)
#     content_metadata3 = serializers.CharField(required=False)
#     syslog_metadata = serializers.CharField(required=False)
#     self_statements = serializers.CharField(required=False)
#     created_at = serializers.CharField(required=False)
#     modified_at = serializers.CharField(required=False)

#     def create(self, validated_data):
#         # Creating new instances of SentinoItemProximity
#         return SentinoItemProximity.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # updating new instances of Sentino Item Proximity
#         instance.content_metadata = validated_data.get(
#             'content_metadata', instance.content_metadata)
#         instance.content_metadata2 = validated_data.get(
#             'content_metadata2', instance.content_metadata2)
#         instance.content_metadata3 = validated_data.get(
#             'content_metadata3', instance.content_metadata3)
#         instance.syslog_metadata = validated_data.get(
#             'syslog_metadata', instance.syslog_metadata)
#         instance.self_statements = validated_data.get(
#             'self_statements', instance.self_statements)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Serializer for Sentino Item Projection Model
# class SentinoItemProjectionSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     content_metadata = serializers.CharField(required=False)
#     content_metadata2 = serializers.CharField(required=False)
#     content_metadata3 = serializers.CharField(required=False)
#     syslog_metadata = serializers.CharField(required=False)
#     self_statements = serializers.CharField(required=False)
#     created_at = serializers.CharField(required=False)
#     modified_at = serializers.CharField(required=False)

#     def create(self, validated_data):
#         # Creating new instances of SentinoItemProjection
#         return SentinoItemProjection.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # updating new instances of Sentino Item Projection
#         instance.content_metadata = validated_data.get(
#             'content_metadata', instance.content_metadata)
#         instance.content_metadata2 = validated_data.get(
#             'content_metadata2', instance.content_metadata2)
#         instance.content_metadata3 = validated_data.get(
#             'content_metadata3', instance.content_metadata3)
#         instance.syslog_metadata = validated_data.get(
#             'syslog_metadata', instance.syslog_metadata)
#         instance.self_statements = validated_data.get(
#             'self_statements', instance.self_statements)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Serializer for Sentino Item Classfication Model
# class SentinoItemClassficationSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     content_metadata = serializers.CharField(required=False)
#     content_metadata2 = serializers.CharField(required=False)
#     content_metadata3 = serializers.CharField(required=False)
#     syslog_metadata = serializers.CharField(required=False)
#     self_statements = serializers.CharField(required=False)
#     created_at = serializers.CharField(required=False)
#     modified_at = serializers.CharField(required=False)

#     def create(self, validated_data):
#         # Creating new instances of SentinoItemProjection
#         return SentinoItemClassification.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # updating new instances of Sentino Item Projection
#         instance.content_metadata = validated_data.get(
#             'content_metadata', instance.content_metadata)
#         instance.content_metadata2 = validated_data.get(
#             'content_metadata2', instance.content_metadata2)
#         instance.content_metadata3 = validated_data.get(
#             'content_metadata3', instance.content_metadata3)
#         instance.syslog_metadata = validated_data.get(
#             'syslog_metadata', instance.syslog_metadata)
#         instance.self_statements = validated_data.get(
#             'self_statements', instance.self_statements)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Serializer for Sentino  Inventory Model
# class SentinoInventorySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     content_metadata = serializers.CharField(required=False)
#     content_metadata2 = serializers.CharField(required=False)
#     content_metadata3 = serializers.CharField(required=False)
#     syslog_metadata = serializers.CharField(required=False)
#     self_statements = serializers.CharField(required=False)
#     created_at = serializers.CharField(required=False)
#     modified_at = serializers.CharField(required=False)

#     def create(self, validated_data):
#         # Creating new instances of SentinoItemProjection
#         return SentinoInventory.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # updating new instances of Sentino Inventory
#         instance.content_metadata = validated_data.get(
#             'content_metadata', instance.content_metadata)
#         instance.content_metadata2 = validated_data.get(
#             'content_metadata2', instance.content_metadata2)
#         instance.content_metadata3 = validated_data.get(
#             'content_metadata3', instance.content_metadata3)
#         instance.syslog_metadata = validated_data.get(
#             'syslog_metadata', instance.syslog_metadata)
#         instance.self_statements = validated_data.get(
#             'self_statements', instance.self_statements)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Serializer for Sentino Self Description Model
# class SentinoDescriptionSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     content_metadata = serializers.CharField(required=False)
#     content_metadata2 = serializers.CharField(required=False)
#     content_metadata3 = serializers.CharField(required=False)
#     syslog_metadata = serializers.CharField(required=False)
#     self_statements = serializers.CharField(required=False)
#     created_at = serializers.CharField(required=False)
#     modified_at = serializers.CharField(required=False)

#     def create(self, validated_data):
#         # Creating new instances of SentinoSelfDescription
#         return SentinoSelfDescription.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # updating new instances of SentinoSelfDescription
#         instance.content_metadata = validated_data.get(
#             'content_metadata', instance.content_metadata)
#         instance.content_metadata2 = validated_data.get(
#             'content_metadata2', instance.content_metadata2)
#         instance.content_metadata3 = validated_data.get(
#             'content_metadata3', instance.content_metadata3)
#         instance.syslog_metadata = validated_data.get(
#             'syslog_metadata', instance.syslog_metadata)
#         instance.self_statements = validated_data.get(
#             'self_statements', instance.self_statements)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Serializer for Sentino Profile Model
# class SentinoProfileSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     content_metadata = serializers.CharField(required=False)
#     content_metadata2 = serializers.CharField(required=False)
#     content_metadata3 = serializers.CharField(required=False)
#     syslog_metadata = serializers.CharField(required=False)
#     self_statements = serializers.CharField(required=False)
#     created_at = serializers.CharField(required=False)
#     modified_at = serializers.CharField(required=False)

#     def create(self, validated_data):
#         # Creating new instances of SentinoProfile
#         return SentinoProfile.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # updating new instances of SentinoSelfDescription
#         instance.content_metadata = validated_data.get(
#             'content_metadata', instance.content_metadata)
#         instance.content_metadata2 = validated_data.get(
#             'content_metadata2', instance.content_metadata2)
#         instance.content_metadata3 = validated_data.get(
#             'content_metadata3', instance.content_metadata3)
#         instance.syslog_metadata = validated_data.get(
#             'syslog_metadata', instance.syslog_metadata)
#         instance.self_statements = validated_data.get(
#             'self_statements', instance.self_statements)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Serializer for Bodega Vision Model
# class BodegaVisionSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     metauserID = serializers.PrimaryKeyRelatedField(
#         queryset=MetaUser.objects.all())
#     image_metadata = serializers.CharField(required=False)
#     video_metadata = serializers.CharField(required=False)
#     content_metadata = serializers.CharField(required=False)
#     syslog_metadata = serializers.CharField(required=False)
#     created_at = serializers.CharField(required=False)
#     modified_at = serializers.CharField(required=False)

#     def create(self, validated_data):
#         # Creating new instances of BodegaVision Model
#         return BodegaVision.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # updating new instances of Bodega Vision
#         instance.metauserID = validated_data.get(
#             'metauserID', instance.metauserID)
#         instance.image_metadata = validated_data.get(
#             'image_metadata', instance.image_metadata)
#         instance.video_metadata = validated_data.get(
#             'video_metadata', instance.video_metadata)
#         instance.content_metadata = validated_data.get(
#             'content_metadata', instance.content_metadata)
#         instance.syslog_metadata = validated_data.get(
#             'syslog_metadata', instance.syslog_metadata)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Seriazlier for Bodega Face Model
# class BodegaFaceSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     metauserID = serializers.PrimaryKeyRelatedField(
#         queryset=MetaUser.objects.all())
#     facial_metadata = serializers.CharField(required=False)
#     syslog_metadata = serializers.CharField(required=False)
#     created_at = serializers.CharField(required=False)
#     modified_at = serializers.CharField(required=False)

#     def create(self, validated_data):
#         # Creating new instances of Bodega Face Model
#         return BodegaFace.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # updating new instances of Bodega Face Model
#         instance.metauserID = validated_data.get(
#             'metauserID', instance.metauserID)
#         instance.facial_metadata = validated_data.get(
#             'facial_metadata', instance.facial_metadata)
#         instance.syslog_metadata = validated_data.get(
#             'syslog_metadata', instance.syslog_metadata)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Serializer for Bodega Personalizer Model
# class BodegaPersonalizerSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     metauserID = serializers.PrimaryKeyRelatedField(
#         queryset=MetaUser.objects.all())
#     content_metadata = serializers.CharField(required=False)
#     syslog_metadata = serializers.CharField(required=False)
#     created_at = serializers.CharField(required=False)
#     modified_at = serializers.CharField(required=False)

#     def create(self, validated_data):
#         # Creating new instances of Bodega Personalizer Model
#         return BodegaPersonalizer.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # updating new instances of Bodega Personalizer Model
#         instance.metauserID = validated_data.get(
#             'metauserID', instance.metauserID)
#         instance.content_metadata = validated_data.get(
#             'content_metadata', instance.content_metadata)
#         instance.syslog_metadata = validated_data.get(
#             'syslog_metadata', instance.syslog_metadata)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Serializer for Bodega Cognitive Item Model
# class BodegaCognitiveItemSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     metauserID = serializers.PrimaryKeyRelatedField(
#         queryset=MetaUser.objects.all())
#     proximityID = serializers.PrimaryKeyRelatedField(
#         queryset=SentinoItemProximity.objects.all())
#     classificationID = serializers.PrimaryKeyRelatedField(
#         queryset=SentinoItemClassification.objects.all())
#     projectionID = serializers.PrimaryKeyRelatedField(
#         queryset=SentinoItemProjection.objects.all())
#     self_statements = serializers.CharField(required=False)
#     content_metadata = serializers.CharField(required=False)
#     syslog_metadata = serializers.CharField(required=False)
#     created_at = serializers.CharField(required=False)
#     modified_at = serializers.CharField(required=False)

#     def create(self, validated_data):
#         # Creating new instances of Bodega Cognitive Model
#         return BodegaCognitiveItem.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # updating new instances of Bodega Cognitive Model
#         instance.metauserID = validated_data.get(
#             'metauserID', instance.metauserID)
#         instance.proximityID = validated_data.get(
#             'proximityID', instance.proximityID)
#         instance.classificationID = validated_data.get(
#             'classificationID', instance.classificationID)
#         instance.projectionID = validated_data.get(
#             'projectionID', instance.projectionID)
#         instance.self_statements = validated_data.get(
#             'self_statements', instance.self_statements)
#         instance.content_metadata = validated_data.get(
#             'content_metadata', instance.content_metadata)
#         instance.syslog_metadata = validated_data.get(
#             'syslog_metadata', instance.syslog_metadata)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Serializer for Bodega Cognitive Inventory
# class BodegaCognitiveInventorySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     metauserID = serializers.PrimaryKeyRelatedField(
#         queryset=MetaUser.objects.all())
#     inventoryID = serializers.PrimaryKeyRelatedField(
#         queryset=SentinoInventory.objects.all())
#     self_statements = serializers.CharField(required=False)
#     content_metadata = serializers.CharField(required=False)
#     syslog_metadata = serializers.CharField(required=False)
#     created_at = serializers.CharField(required=False)
#     modified_at = serializers.CharField(required=False)

#     def create(self, validated_data):
#         # Creating new instances of Bodega Cognitive Inventory Model
#         return BodegaCognitiveInventory.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # updating new instances of Bodega Cognitive Model
#         instance.metauserID = validated_data.get(
#             'metauserID', instance.metauserID)
#         instance.inventoryID = validated_data.get(
#             'inventoryID', instance.inventoryID)
#         instance.self_statements = validated_data.get(
#             'self_statements', instance.self_statements)
#         instance.content_metadata = validated_data.get(
#             'content_metadata', instance.content_metadata)
#         instance.syslog_metadata = validated_data.get(
#             'syslog_metadata', instance.syslog_metadata)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Serializer for Bodega Cognitive Person
# class BodegaCognitivePersonSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     metauserID = serializers.PrimaryKeyRelatedField(
#         queryset=MetaUser.objects.all())
#     self_descriptionID = serializers.PrimaryKeyRelatedField(
#         queryset=SentinoSelfDescription.objects.all())
#     profileID = serializers.PrimaryKeyRelatedField(
#         queryset=SentinoProfile.objects.all())
#     self_statements = serializers.CharField(required=False)
#     content_metadata = serializers.CharField(required=False)
#     syslog_metadata = serializers.CharField(required=False)
#     created_at = serializers.CharField(required=False)
#     modified_at = serializers.CharField(required=False)

#     def create(self, validated_data):
#         # Creating new instances of Bodega Cognitive Person  Model
#         return BodegaCognitivePerson.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # updating new instances of Bodega Cognitive Person Model
#         instance.metauserID = validated_data.get(
#             'metauserID', instance.metauserID)
#         instance.self_descriptionID = validated_data.get(
#             'self_descriptionID', instance.self_descriptionID)
#         instance.profileID = validated_data.get(
#             'profileID', instance.profileID)
#         instance.self_statements = validated_data.get(
#             'self_statements', instance.self_statements)
#         instance.content_metadata = validated_data.get(
#             'content_metadata', instance.content_metadata)
#         instance.syslog_metadata = validated_data.get(
#             'syslog_metadata', instance.syslog_metadata)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Serializer for Bodega Department Model
# class BodegaDeptSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     metauserID = serializers.PrimaryKeyRelatedField(
#         queryset=MetaUser.objects.all())
#     departmentname = serializers.CharField(required=False)
#     content_metadata = serializers.CharField(required=False)
#     created_at = serializers.CharField(required=False)
#     modified_at = serializers.CharField(required=False)

#     def create(self, validated_data):
#         # Creating new instances of Bodega Dept Model
#         return BodegaDept.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # updating new instances of Bodega Dept Model
#         instance.metauserID = validated_data.get(
#             'metauserID', instance.metauserID)
#         instance.departmentname = validated_data.get(
#             'departmentname', instance.departmentname)
#         instance.content_metadata = validated_data.get(
#             'content_metadata', instance.content_metadata)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Serializer for User Address Class
# class UserAddressSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     metauserID = serializers.PrimaryKeyRelatedField(
#         queryset=MetaUser.objects.all())
#     address_line1 = serializers.CharField(required=False)
#     address_line2 = serializers.CharField(required=False)
#     address_state = serializers.CharField(required=False)
#     city = serializers.CharField(required=False)
#     postal_code = serializers.CharField(required=False)
#     country = serializers.ChoiceField(choices=country_list, default='ISR')
#     created_at = serializers.CharField(required=False)
#     modified_at = serializers.CharField(required=False)

#     # create() and update() functions interact with our DB not the APIs directly
#     def create(self, validated_data):
#         # creating a new instance of the UserAddress Model
#         return UserAddress.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # updating a model instance with only the validated_fields
#         instance.metauserID = validated_data.get(
#             'metauserID', instance.metauserID)
#         instance.address_line1 = validated_data.get(
#             'address_line1', instance.address_line1)
#         instance.address_line2 = validated_data.get(
#             'address_line2', instance.address_line2)
#         instance.address_state = validated_data.get(
#             'address_state', instance.address_state)
#         instance.city = validated_data.get('city', instance.city)
#         instance.postal_code = validated_data.get(
#             'postal_code', instance.postal_code)
#         instance.country = validated_data.get('country', instance.country)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modfied_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Serializer User Payment Class
# class UserPaymentSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     metauserID = serializers.PrimaryKeyRelatedField(
#         queryset=MetaUser.objects.all())
#     payment_type = serializers.ChoiceField(
#         choices=payment_types, default='PAYPAL')
#     payment_provider = serializers.CharField(required=False)
#     payment_status = serializers.BooleanField(required=False)
#     total_money_out = serializers.FloatField()
#     total_money_in = serializers.FloatField()
#     user_payment_profile_status = serializers.BooleanField(required=False)
#     # add code for routing money via Stripe to multiple vendors
#     # all data can be fetched via FE, they can route this data here
#     created_at = serializers.CharField(required=False)
#     modified_at = serializers.CharField(required=False)

#     # create() and update() functions to interact with our DB
#     def create(self, validated_data):
#         # returns a new model instance with yhe validated data as input
#         return UserPayment.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # passes validated_data field to instance
#         # .get() fetches that field name from the POST request data and updates the field of UserPayment table
#         instance.metauserID = validated_data.get(
#             'metauserID', instance.metauserID)
#         instance.payment_type = validated_data.get(
#             'payment_type', instance.payment_type)
#         instance.payment_provider = validated_data.get(
#             'payment_provider', instance.payment_provider)
#         instance.payment_status = validated_data.get(
#             'payment_status', instance.payment_status)
#         instance.total_money_out = validated_data.get(
#             'total_money_out', instance.total_money_out)
#         instance.total_money_in = validated_data.get(
#             'total_money_in', instance.total_money_in)
#         instance.user_payment_profile_status = validated_data.get('user_payment_profile_status',
#                                                                   instance.user_payment_profile_status)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Serializer for User Type Class
# class UserTypeSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     metauserID = serializers.PrimaryKeyRelatedField(
#         queryset=MetaUser.objects.all())
#     bodega_vision_ID = serializers.PrimaryKeyRelatedField(
#         queryset=BodegaVision.objects.all())
#     level_ID = serializers.PrimaryKeyRelatedField(queryset=Level.objects.all())
#     solomon_person_ID = serializers.PrimaryKeyRelatedField(
#         queryset=Solomonv0.objects.all())
#     user_role = serializers.CharField(required=False)
#     created_at = serializers.CharField(required=False)
#     modified_at = serializers.CharField(required=False)

#     def create(self, validated_data):
#         # Creating new instances of User Type Model
#         return UserType.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # Updating instances of User Type Model
#         instance.metauserID = validated_data.get(
#             'metauserID', instance.metauserID)
#         instance.bodega_vision_ID = validated_data.get(
#             'bodega_vision_ID', instance.bodega_vision_ID)
#         instance.level_ID = validated_data.get('level_ID', instance.level_ID)
#         instance.solomon_person_ID = validated_data.get(
#             'solomon_person_ID', instance.solomon_person_ID)
#         instance.user_role = validated_data.get(
#             'user_role', instance.user_role)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Serializer Class for Chat Room Model
# class ChatRoomSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required=True)
#     desc = serializers.CharField(required=True)
#     rules = serializers.CharField(required=False)
#     type_of_room = serializers.ChoiceField(
#         choices=type_of_room_array, required=True)
#     is_room_active = serializers.BooleanField(required=True)
#     room_hashkey = serializers.CharField(
#         default='ROOM HASHKEY', read_only=True)
#     created_on = serializers.CharField(required=True)
#     modified_on = serializers.CharField(required=True)

#     # create() and update() funrctions to interaact with our DB
#     def create(self, validated_data):
#         # returns a new model instance
#         return ChatRoom.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.desc = validated_data.get('desc', instance.desc)
#         instance.rules = validated_data.get('rules', instance.rules)
#         instance.type_of_room = validated_data.get(
#             'type_of_room', instance.type_of_room)
#         instance.created_on = validated_data.get(
#             'created_on', instance.created_on)
#         instance.is_room_active = validated_data.get(
#             'is_room_active', instance.is_room_active)

#         instance.save()
#         return instance


# # Serializer class for Particpant model
# class ParticpantSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     metauserID = serializers.PrimaryKeyRelatedField(
#         queryset=MetaUser.objects.all())  # FK
#     chat_room_ID = serializers.PrimaryKeyRelatedField(
#         queryset=ChatRoom.objects.all())  # FK2

#     # create() and update() functions to interact with our DB
#     def create(self, validated_data):
#         # returns a new model instance
#         return Particpant.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.metauserID = validated_data.get(
#             'metauserID', instance.metauserID)
#         instance.chat_room_ID = validated_data.get(
#             'chat_room_ID', instance.chat_room_ID)

#         instance.save()
#         return instance


# # # Serializer class for Message model
# # class MessageSerializer(serializers.Serializer):
# #     id = serializers.IntegerField(read_only=True)
# #     chat_room_ID = serializers.PrimaryKeyRelatedField(
# #         queryset=ChatRoom.objects.all())
# #     metauserID = serializers.PrimaryKeyRelatedField(
# #         queryset=MetaUser.objects.all())
# #     message_body = serializers.CharField(required=True)
# #     upload_file = serializers.FileField()
# #     created_at = serializers.CharField()
# #     modified_at = serializers.CharField()
# #     hashkey = serializers.CharField(read_only=True)

# #     # create() and update() functions to interact with our DB
# #     def create(self, validated_data):
# #         # returns a new model instance
# #         return Message.objects.create(**validated_data)

# #     def update(self, instance, validated_data):
# #         instance.chat_room_ID = validated_data.get(
# #             'chat_room_ID', instance.chat_room_ID)
# #         instance.metauserID = validated_data.get(
# #             'metauserID', instance.metauserID)
# #         instance.message_body = validated_data.get(
# #             'message_body', instance.message_body)
# #         instance.upload_file = validated_data.get(
# #             'upload_file', instance.upload_file)
# #         instance.created_at = validated_data.get(
# #             'created_at', instance.created_at)
# #         instance.modified_at = validated_data.get(
# #             'modified_at', instance.modified_at)
# #         instance.hashkey = validated_data.get('hashkey', instance.hashkey)

# #         instance.save()
# #         return instance
    



# # Serializer for Product Category Model
# class ProductCategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     category_name = serializers.ChoiceField(
#         required=True, choices=ProductCategory_array)
#     category_desc = serializers.CharField()
#     created_at = serializers.CharField()
#     modified_at = serializers.CharField()
#     category_image1 = serializers.CharField()
#     category_image2 = serializers.CharField()
#     category_image3 = serializers.CharField()

#     # no default on image can create issues when using POST

#     def create(self, validated_data):
#         # returns a new model instance
#         return ProductCategory.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.category_name = validated_data.get(
#             'category_name', instance.category_name)
#         instance.category_desc = validated_data.get(
#             'category_desc', instance.category_desc)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)
#         instance.category_image1 = validated_data.get(
#             'category_image1', instance.category_image1)
#         instance.category_image2 = validated_data.get(
#             'category_image2', instance.category_image2)
#         instance.category_image3 = validated_data.get(
#             'category_image3', instance.category_image1)

#         instance.save()
#         return instance


# # Serializer for Product Themes Model
# class ProductThemesSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     collection_name = serializers.CharField()
#     collection_desc = serializers.CharField()
#     audience_traits = serializers.CharField()
#     marketing_funnel = serializers.ChoiceField(choices=marketing_funnel_array)
#     created_at = serializers.CharField()
#     modified_at = serializers.CharField()

#     def create(self, validated_data):
#         # returns a new model instance
#         return ProductThemes.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.collection_name = validated_data.get(
#             'collection_name', instance.collection_name)
#         instance.collection_desc = validated_data.get(
#             'collection_desc', instance.collection_desc)
#         instance.audience_traits = validated_data.get(
#             'audience_traits', instance.audience_traits)
#         instance.marketing_funnel = validated_data.get(
#             'marketing_funnel', instance.marketing_funnel)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Serializer for Discount model
# class DiscountSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     discount_percent = serializers.FloatField()
#     active_status = serializers.BooleanField()
#     created_by = serializers.PrimaryKeyRelatedField(
#         queryset=MetaUser.objects.all())
#     created_at = serializers.CharField()
#     modified_at = serializers.CharField()

#     def create(self, validated_data):
#         return Discount.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get(
#             'description', instance.description)
#         instance.discount_percent = validated_data.get(
#             'discount_percent', instance.discount_percent)
#         instance.active_status = validated_data.get(
#             'active_status', instance.active_status)
#         instance.created_by = validated_data.get(
#             'created_by', instance.created_by)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Serializer for Social model
# class SocialSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     metauserID = serializers.PrimaryKeyRelatedField(
#         queryset=MetaUser.objects.all())
#     following = serializers.CharField()
#     followers = serializers.CharField()
#     makeprofileprivate = serializers.BooleanField()
#     saved_content = serializers.CharField()
#     likes = serializers.CharField()
#     dislikes = serializers.CharField()
#     comments = serializers.CharField()
#     products_clickedOn = serializers.CharField()
#     bio = serializers.CharField(allow_blank=True)
#     blocked_list = serializers.CharField()
#     data_mining_status = serializers.BooleanField()
#     account_active = serializers.BooleanField(default=True)
#     delete_metauser = serializers.BooleanField(default=False)
#     created_on = serializers.CharField()
#     modified_on = serializers.CharField()

#     def create(self, validated_data):
#         return Social.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.metauserID = validated_data.get(
#             'metauserID', instance.metauserID)
#         instance.following = validated_data.get(
#             'following', instance.following)
#         instance.followers = validated_data.get(
#             'followers', instance.followers)
#         instance.makeprofileprivate = validated_data.get(
#             'makeprofileprivate', instance.makeprofileprivate)
#         instance.saved_content = validated_data.get(
#             'saved_content', instance.saved_content)
#         instance.likes = validated_data.get('likes', instance.likes)
#         instance.dislikes = validated_data.get('dislikes', instance.dislikes)
#         instance.comments = validated_data.get('comments', instance.comments)
#         instance.products_clickedOn = validated_data.get(
#             'products_clickedOn', instance.products_clickedOn)
#         instance.bio = validated_data.get('bio', instance.bio)
#         instance.blocked_list = validated_data.get(
#             'blocked_list', instance.blocked_list)
#         instance.data_mining_status = validated_data.get(
#             'data_mining_status', instance.data_mining_status)
#         instance.account_active = validated_data.get(
#             'account_active', instance.account_active)
#         instance.delete_metauser = validated_data.get(
#             'delete_metauser', instance.delete_metauser)
#         instance.created_on = validated_data.get(
#             'created_on', instance.created_on)
#         instance.modified_on = validated_data.get(
#             'modified_on', instance.modified_on)

#         instance.save()
#         return instance


# # Serializer for Shop Model
# class ShopSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     metauserID = serializers.PrimaryKeyRelatedField(
#         queryset=MetaUser.objects.all())
#     all_products = serializers.CharField(required=True)
#     all_user_data = serializers.CharField(required=True)
#     name = serializers.CharField(required=True)
#     description = serializers.CharField(required=True)
#     logo = serializers.CharField(required=True)
#     cover_image = serializers.CharField(required=True)
#     address_line1 = serializers.CharField(required=True)
#     address_line2 = serializers.CharField(required=True)
#     city = serializers.CharField(required=True)
#     state = serializers.CharField(required=True)
#     postal_code = serializers.CharField(required=True)
#     country = serializers.ChoiceField(
#         choices=country_list)  # Before deployment -> use this link for data: https://github.com/hampusborgos/country-flags/blob/main/countries.json
#     bodega_vision_tags = serializers.CharField(required=False)
#     bodega_customer_tags = serializers.CharField(required=False)
#     unqiuesellingprop = serializers.CharField(required=False)
#     data_mining_status = serializers.CharField(required=False)
#     created_on = serializers.CharField(required=False)
#     modified_on = serializers.CharField(required=False)

#     def create(self, validated_data):
#         return Shop.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.metauserID = validated_data.get(
#             'metauserID', instance.metauserID)
#         instance.all_products = validated_data.get(
#             'all_products', instance.all_products)
#         instance.all_user_data = validated_data.get(
#             'all_user_data', instance.all_user_data)
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get(
#             'description', instance.description)
#         instance.logo = validated_data.get('logo', instance.logo)
#         instance.cover_image = validated_data.get(
#             'cover_image', instance.cover_image)
#         instance.address_line1 = validated_data.get(
#             'address_line1', instance.address_line1)
#         instance.address_line2 = validated_data.get(
#             'address_line2', instance.address_line2)
#         instance.city = validated_data.get('city', instance.city)
#         instance.state = validated_data.get('state', instance.state)
#         instance.postal_code = validated_data.get(
#             'postal_code', instance.postal_code)
#         instance.country = validated_data.get('country', instance.country)
#         instance.bodega_vision_tags = validated_data.get(
#             'bodega_vision_tags', instance.bodega_vision_tags)
#         instance.bodega_customer_tags = validated_data.get(
#             'bodega_customer_tags', instance.bodega_customer_tags)
#         instance.unqiuesellingprop = validated_data.get(
#             'unqiuesellingprop', instance.unqiuesellingprop)
#         instance.data_mining_status = validated_data.get(
#             'data_mining_status', instance.data_mining_status)
#         instance.created_on = validated_data.get(
#             'created_on', instance.created_on)
#         instance.modified_on = validated_data.get(
#             'modified_on', instance.modified_on)

#         instance.save()
#         return instance


# # most important fucking serializer class - be extra careful
# # Serializer for ProductMetaData Model

# class ProductMetaDataSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     numberoflikes = serializers.IntegerField(required=False)
#     numberofcomments = serializers.IntegerField(required=False)
#     numberofclicks = serializers.IntegerField(required=False)
#     totaltimespentonproduct_hours = serializers.IntegerField(required=False)
#     metauserID_of_likes = serializers.CharField(required=False)
#     metauserID_of_dislikes = serializers.CharField(required=False)
#     metauserID_of_comments = serializers.CharField(required=False)
#     total_sales = serializers.FloatField(required=False)
#     clicks_on_product = serializers.IntegerField(required=False)
#     is_product_digital = serializers.BooleanField(required=False)
#     assistance_ask = serializers.CharField(required=False)
#     nsfw_content = serializers.BooleanField(required=True)
#     production_cost = serializers.FloatField(required=False)
#     production_time_days = serializers.IntegerField(required=True)
#     hours_invested = serializers.FloatField(required=False)
#     encrypt_product = serializers.BooleanField(required=False)
#     unit_sold_expectation = serializers.IntegerField(required=False)
#     size_chart = serializers.CharField(required=False)
#     product_image2 = serializers.CharField(required=False)
#     product_image3 = serializers.CharField(required=False)
#     product_image4 = serializers.CharField(required=False)
#     created_at = serializers.CharField(required=False)
#     modified_at = serializers.CharField(required=False)

#     def create(self, validated_data):
#         # Creating new instances of ProductMetaData Model Instance
#         return ProductMetaData.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # updating instances of ProductMetaData Model
#         instance.numberoflikes = validated_data.get(
#             'numberoflikes', instance.numberoflikes)
#         instance.numberofcomments = validated_data.get(
#             'numberofcomments', instance.numberofcomments)
#         instance.numberofclicks = validated_data.get(
#             'numberofclicks', instance.numberofclicks)
#         instance.totaltimespentonproduct_hours = validated_data.get('totaltimespentonproduct_hours',
#                                                                     instance.totaltimespentonproduct_hours)
#         instance.metauserID_of_likes = validated_data.get(
#             'metauserID_of_likes', instance.metauserID_of_likes)
#         instance.metauserID_of_dislikes = validated_data.get(
#             'metauserID_of_dislikes', instance.metauserID_of_dislikes)
#         instance.metauserID_of_comments = validated_data.get(
#             'metauserID_of_comments', instance.metauserID_of_comments)
#         instance.total_sales = validated_data.get(
#             'total_sales', instance.total_sales)
#         instance.clicks_on_product = validated_data.get(
#             'clicks_on_product', instance.clicks_on_product)
#         instance.is_product_digital = validated_data.get(
#             'is_product_digital', instance.is_product_digital)
#         instance.assistance_ask = validated_data.get(
#             'assistance_ask', instance.assistance_ask)
#         instance.nsfw_content = validated_data.get(
#             'nsfw_content', instance.nsfw_content)
#         instance.production_cost = validated_data.get(
#             'production_cost', instance.production_cost)
#         instance.production_time_days = validated_data.get(
#             'production_time_days', instance.production_time_days)
#         instance.hours_invested = validated_data.get(
#             'hours_invested', instance.hours_invested)
#         instance.encrypt_product = validated_data.get(
#             'encrypt_product', instance.encrypt_product)
#         instance.unit_sold_expectation = validated_data.get(
#             'unit_sold_expectation', instance.unit_sold_expectation)
#         instance.size_chart = validated_data.get(
#             'size_chart', instance.size_chart)
#         instance.product_image2 = validated_data.get(
#             'product_image2', instance.product_image2)
#         instance.product_image3 = validated_data.get(
#             'product_image3', instance.product_image3)
#         instance.product_image4 = validated_data.get(
#             'product_image4', instance.product_image4)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Serializer for Product Model

# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     metauserID = serializers.PrimaryKeyRelatedField(
#         queryset=MetaUser.objects.all())
#     productMetaDataID = serializers.PrimaryKeyRelatedField(
#         queryset=ProductMetaData.objects.all())
#     product_categoryID = serializers.PrimaryKeyRelatedField(
#         queryset=ProductCategory.objects.all())
#     product_themesID = serializers.PrimaryKeyRelatedField(
#         queryset=ProductThemes.objects.all())
#     discount_ID = serializers.PrimaryKeyRelatedField(
#         queryset=Discount.objects.all())
#     shop_ID = serializers.PrimaryKeyRelatedField(queryset=Shop.objects.all())
#     name = serializers.CharField(required=True)
#     description = serializers.CharField(required=True)
#     selling_price = serializers.FloatField(required=False)
#     discounted_price = serializers.FloatField(required=False)
#     quanity = serializers.IntegerField(required=False)
#     is_product_digital = serializers.BooleanField(required=True)
#     product_image1 = serializers.CharField(required=True)
#     hashkey = serializers.CharField(read_only=True)
#     created_at = serializers.CharField(required=False)
#     modified_at = serializers.CharField(required=False)

#     def create(self, validated_data):
#         # Creating new instance of Product Model
#         return Product.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # Updating instances of Product Model
#         instance.metauserID = validated_data.get(
#             'metauserID', instance.metauserID)
#         instance.productMetaDataID = validated_data.get(
#             'productMetaDataID', instance.productMetaDataID)
#         instance.product_categoryID = validated_data.get(
#             'product_categoryID', instance.product_categoryID)
#         instance.product_themesID = validated_data.get(
#             'product_themesID', instance.product_themesID)
#         instance.discount_ID = validated_data.get(
#             'discount_ID', instance.discount_ID)
#         instance.shop_ID = validated_data.get('shop_ID', instance.shop_ID)
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get(
#             'description', instance.description)
#         instance.selling_price = validated_data.get(
#             'selling_price', instance.selling_price)
#         instance.discounted_price = validated_data.get(
#             'discounted_price', instance.discounted_price)
#         instance.quantity = validated_data.get('quantity', instance.quantity)
#         instance.is_product_digital = validated_data.get(
#             'is_product_digital', instance.is_product_digital)
#         instance.product_image1 = validated_data.get(
#             'product_image1', instance.product_image1)
#         instance.hashkey = validated_data.get('hashkey', instance.hashkey)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Serializer for Collaboration class

# class CollaborationSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     creator_collab_choice = serializers.ChoiceField(choices=collab_type_array)
#     metauserID = serializers.PrimaryKeyRelatedField(
#         queryset=MetaUser.objects.all())
#     product_ID = serializers.PrimaryKeyRelatedField(
#         queryset=Product.objects.all())
#     shop_ID = serializers.PrimaryKeyRelatedField(queryset=Shop.objects.all())
#     creator_pitch = serializers.CharField()
#     bid_type = serializers.ChoiceField(choices=collab_type_array)
#     bid_amount = serializers.FloatField()
#     accept_bid = serializers.BooleanField()
#     created_at = serializers.CharField()
#     modified_at = serializers.CharField()

#     def create(self, validated_data):
#         return Collaboration.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get(
#             'description', instance.description)
#         instance.creator_collab_choice = validated_data.get(
#             'creator_collab_choice', instance.creator_collab_choice)
#         instance.metauserID = validated_data.get(
#             'metauserID', instance.metauserID)
#         instance.product_ID = validated_data.get(
#             'product_ID', instance.product_ID)
#         instance.shop_ID = validated_data.get('shop_ID', instance.shop_ID)
#         instance.creator_pitch = validated_data.get(
#             'creator_pitch', instance.creator_pitch)
#         instance.bid_type = validated_data.get('bid_type', instance.bid_type)
#         instance.bid_amount = validated_data.get(
#             'bid_amount', instance.bid_amount)
#         instance.accept_bid = validated_data.get(
#             'accept_bid', instance.accept_bid)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Shopping Session Serializer Class
# class ShoppingSessionSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     metauserID = serializers.PrimaryKeyRelatedField(
#         queryset=MetaUser.objects.all())
#     total_amount = serializers.FloatField(required=True)
#     created_at = serializers.CharField(required=True)
#     modified_at = serializers.CharField(required=True)

#     def create(self, validated_data):
#         return ShoppingSession.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.metauserID = validated_data.get(
#             'metauserID', instance.metauserID)
#         instance.total_amount = validated_data.get(
#             'total_amount', instance.total_amount)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Cart Item Serializer
# class CartItemSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     session_ID = serializers.PrimaryKeyRelatedField(queryset=ShoppingSession.objects.all())
#     product_ID = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
#     quantity = serializers.IntegerField(required=True)
#     created_at = serializers.CharField(required=True)
#     modified_at = serializers.CharField(required=True)

#     def create(self, validated_data):
#         return CartItem.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.session_ID = validated_data.get(
#             'session_ID', instance.session_ID)
#         instance.product_ID = validated_data.get(
#             'product_ID', instance.product_ID)
#         instance.quantity = validated_data.get('quantity', instance.quantity)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Order Details Serializer class
# class OrderDetailsSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     total_amount = serializers.FloatField(required=True)
#     payment_info = serializers.PrimaryKeyRelatedField(queryset=UserPayment.objects.all())
#     created_at = serializers.CharField(required=True)
#     modified_at = serializers.CharField(required=True)

#     def create(self, validated_data):
#         return OrderDetail.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.total_amount = validated_data.get(
#             'total_amount', instance.total_amount)
#         instance.payment_info = validated_data.get(
#             'payment_info', instance.payment_info)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Order Items Serializer Class
# class OrderItemSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     order_ID = serializers.PrimaryKeyRelatedField(queryset=OrderDetail.objects.all())
#     product_ID = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
#     quantity = serializers.IntegerField(required=True)
#     created_at = serializers.CharField(required=True)
#     modified_at = serializers.CharField(required=True)

#     def create(self, validated_data):
#         return OrderItem.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.order_ID = validated_data.get('order_ID', instance.order_ID)
#         instance.product_ID = validated_data.get(
#             'product_ID', instance.product_ID)
#         instance.quantity = validated_data.get('quantity', instance.quantity)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Shop Payout Serializer Class
# # NOT COMPLETED
# # Need to revisit after seeing Stipe Connect
# class ShopPayoutSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     order_detail_ID = serializers.PrimaryKeyRelatedField(queryset=OrderDetail.objects.all())

#     def create(self, validated_idea):
#         return ShopPayout.objects.create(**validated_idea)

#     def update(self, instance, validated_idea):
#         instance.order_detail_ID = validated_idea.get(
#             'order_detail_ID', instance.order_detail_ID)
#         instance.save()
#         return instance


# # Serializers for SysOps Agent Models


# # Serialzier for SysOpsAgent
# class SysOpsAgentSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     metauserID = serializers.PrimaryKeyRelatedField(
#         queryset=MetaUser.objects.all())
#     levelID = serializers.PrimaryKeyRelatedField(queryset=Level.objects.all())
#     departmentID = serializers.PrimaryKeyRelatedField(
#         queryset=BodegaDept.objects.all())
#     agent_hashkey = serializers.CharField(required=True)
#     bio = serializers.CharField(required=False)
#     reporting_officer = serializers.CharField(required=True)
#     created_at = serializers.CharField(required=False)
#     modified_at = serializers.CharField(required=False)

#     def create(self, validated_data):
#         return SysOpsAgent.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.metauserID = validated_data.get(
#             'metauserID', instance.metauserID)
#         instance.levelID = validated_data.get('levelID', instance.levelID)
#         instance.departmentID = validated_data.get(
#             'departmentID', instance.departmentID)
#         instance.agent_hashkey = validated_data.get(
#             'agent_hashkey', instance.agent_hashkey)
#         instance.bio = validated_data.get('bio', instance.bio)
#         instance.reporting_officer = validated_data.get(
#             'reporting_officer', instance.reporting_officer)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Serializer for SysOps Agent Repo Model
# class SysOpsAgentRepoSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     metauserID = serializers.PrimaryKeyRelatedField(
#         queryset=MetaUser.objects.all())
#     sysops_agentID = serializers.PrimaryKeyRelatedField(
#         queryset=SysOpsAgent.objects.all())
#     project_hashkey = serializers.CharField(required=True)
#     created_at = serializers.CharField(required=False)
#     modified_at = serializers.CharField(required=False)

#     def create(self, validated_data):
#         return SysOpsProject.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.metauserID = validated_data.get(
#             'metauserID', instance.metauserID)
#         instance.sysops_agentID = validated_data.get(
#             'sysops_agentID', instance.sysops_agentID)
#         instance.project_hashkey = validated_data.get(
#             'project_hashkey', instance.project_hashkey)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Serializer for SysOps Project Model
# class SysOpsProjectSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     owner_metauserID = serializers.PrimaryKeyRelatedField(
#         queryset=MetaUser.objects.all())
#     owner_agentID = serializers.PrimaryKeyRelatedField(
#         queryset=SysOpsAgent.objects.all())
#     levelID = serializers.PrimaryKeyRelatedField(queryset=Level.objects.all())
#     divisionID = serializers.PrimaryKeyRelatedField(
#         queryset=BodegaDept.objects.all())
#     name = serializers.CharField(required=True)
#     problem_statement = serializers.CharField(required=False)
#     problem_impact_size = serializers.CharField(required=False)
#     hypothesis = serializers.CharField(required=False)
#     key_performance_indicators = serializers.CharField(required=False)
#     status = serializers.CharField(required=True)
#     ttc_hours = serializers.FloatField(required=False)
#     allocated_ttc_hours = serializers.FloatField(required=False)
#     tasks = serializers.CharField(required=False)
#     team_hashkey_json = serializers.CharField(required=False)
#     hashkey = serializers.CharField(required=False)
#     genesis_project_hashkey = serializers.CharField(required=False)
#     parent_project_hashkey = serializers.CharField(required=False)
#     child_project_hashkey = serializers.CharField(required=False)
#     created_at = serializers.CharField(required=False)
#     modified_at = serializers.CharField(required=False)

#     def create(self, validated_data):
#         return SysOpsProject.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.owner_metauserID = validated_data.get(
#             'owner_metauserID', instance.owner_metauserID)
#         instance.owner_agentID = validated_data.get(
#             'owner_agentID', instance.owner_agentID)
#         instance.levelID = validated_data.get('levelID', instance.levelID)
#         instance.divisionID = validated_data.get(
#             'divisionID', instance.divisionID)
#         instance.name = validated_data.get('name', instance.name)
#         instance.problem_statement = validated_data.get(
#             'problem_statement', instance.problem_statement)
#         instance.problem_impact_size = validated_data.get(
#             'problem_impact_size', instance.problem_impact_size)
#         instance.hypothesis = validated_data.get(
#             'hypothesis', instance.hypothesis)
#         instance.key_performance_indicators = validated_data.get(
#             'key_performance_indicators', instance.key_performance_indicators)
#         instance.status = validated_data.get('status', instance.status)
#         instance.ttc_hours = validated_data.get(
#             'ttc_hours', instance.ttc_hours)
#         instance.allocated_ttc_hours = validated_data.get(
#             'allocated_ttc_hours', instance.allocated_ttc_hours)
#         instance.tasks = validated_data.get('tasks', instance.tasks)
#         instance.team_hashkey_json = validated_data.get(
#             'team_hashkey_json', instance.team_hashkey_json)
#         instance.hashkey = validated_data.get('hashkey', instance.hashkey)
#         instance.genesis_project_hashkey = validated_data.get(
#             'genesis_project_hashkey', instance.genesis_project_hashkey)
#         instance.parent_project_hashkey = validated_data.get(
#             'parent_project_hashkey', instance.parent_project_hashkey)
#         instance.child_project_hashkey = validated_data.get(
#             'child_project_hashkey', instance.child_project_hashkey)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Serializer for SysOpsSupplyNode Model
# class SysOpsSupplyNodeSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     supply_metauserID = serializers.PrimaryKeyRelatedField(
#         queryset=MetaUser.objects.all())
#     supply_shopID = serializers.PrimaryKeyRelatedField(
#         queryset=Shop.objects.all())
#     bla_ScoreID = serializers.PrimaryKeyRelatedField(
#         queryset=BLAScore.objects.all())
#     opsec_agent_hashkey = serializers.CharField(required=True)
#     name = serializers.CharField(required=True)
#     location = serializers.CharField(required=True)
#     status = serializers.CharField(required=False)
#     tokens_allocated = serializers.FloatField(required=False)
#     creator_hypothesis = serializers.CharField(required=False)
#     SysOpsAgent_hypothesis = serializers.CharField(required=False)
#     creator_identity_status = serializers.BooleanField(required=True)
#     all_digital_url = serializers.CharField(required=False)
#     influence_size = serializers.CharField(required=False)
#     genre = serializers.CharField(required=False)
#     category_vertical = serializers.CharField(required=False)
#     category_vertical2 = serializers.CharField(required=False)
#     product_traits = serializers.CharField(required=False)
#     creator_traits = serializers.CharField(required=False)
#     production_type = serializers.CharField(required=False)
#     current_revenue = serializers.CharField(required=False)
#     current_aov = serializers.CharField(required=False)
#     predicted_revenue = serializers.CharField(required=False)
#     creator_audience_traits = serializers.CharField(required=False)
#     sysops_solution_hypothesis = serializers.CharField(required=False)
#     additional_notes = serializers.CharField(required=False)
#     created_at = serializers.CharField(required=False)
#     modified_at = serializers.CharField(required=False)

#     def create(self, validated_data):
#         return SysOpsSupplyNode.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.supply_metauserID = validated_data.get(
#             'supply_metauserID', instance.supply_metauserID)
#         instance.supply_shopID = validated_data.get(
#             'supply_shopID', instance.supply_shopID)
#         instance.bla_ScoreID = validated_data.get(
#             'bla_ScoreID', instance.bla_ScoreID)
#         instance.opsec_agent_hashkey = validated_data.get(
#             'opsec_agent_hashkey', instance.opsec_agent_hashkey)
#         instance.name = validated_data.get('name', instance.name)
#         instance.location = validated_data.get('location', instance.location)
#         instance.status = validated_data.get('status', instance.status)
#         instance.tokens_allocated = validated_data.get(
#             'tokens_allocated', instance.tokens_allocated)
#         instance.creator_hypothesis = validated_data.get(
#             'creator_hypothesis', instance.creator_hypothesis)
#         instance.SysOpsAgent_hypothesis = validated_data.get(
#             'SysOpsAgent_hypothesis', instance.SysOpsAgent_hypothesis)
#         instance.creator_identity_status = validated_data.get(
#             'creator_identity_status', instance.creator_identity_status)
#         instance.all_digital_url = validated_data.get(
#             'all_digital_url', instance.all_digital_url)
#         instance.influence_size = validated_data.get(
#             'influence_size', instance.influence_size)
#         instance.genre = validated_data.get('genre', instance.genre)
#         instance.category_vertical = validated_data.get(
#             'category_vertical', instance.category_vertical)
#         instance.category_vertical2 = validated_data.get(
#             'category_vertical2', instance.category_vertical2)
#         instance.product_traits = validated_data.get(
#             'product_traits', instance.product_traits)
#         instance.creator_traits = validated_data.get(
#             'creator_traits', instance.creator_traits)
#         instance.production_type = validated_data.get(
#             'production_type', instance.production_type)
#         instance.current_revenue = validated_data.get(
#             'current_revenue', instance.current_revenue)
#         instance.current_aov = validated_data.get(
#             'current_aov', instance.current_aov)
#         instance.predicted_revenue = validated_data.get(
#             'predicted_revenue', instance.predicted_revenue)
#         instance.creator_audience_traits = validated_data.get(
#             'creator_audience_traits', instance.creator_audience_traits)
#         instance.sysops_solution_hypothesis = validated_data.get(
#             'sysops_solution_hypothesis', instance.sysops_solution_hypothesis)
#         instance.additional_notes = validated_data.get(
#             'additional_notes', instance.additional_notes)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance


# # Serializer for SysOpsDemandNode Model
# class SysOpsDemandNodeSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     demand_metauserID = serializers.PrimaryKeyRelatedField(
#         queryset=MetaUser.objects.all())
#     bla_ScoreID = serializers.PrimaryKeyRelatedField(
#         queryset=BLAScore.objects.all())
#     opsec_agent_hashkey = serializers.CharField(required=True)
#     name = serializers.CharField(required=True)
#     location = serializers.CharField(required=True)
#     status = serializers.BooleanField(required=False)
#     tokens_allocated = serializers.FloatField(required=False)
#     creator_hypothesis = serializers.CharField(required=False)
#     SysOpsAgent_hypothesis = serializers.CharField(required=False)
#     creator_identity_status = serializers.BooleanField(required=False)
#     all_digital_url = serializers.CharField(required=False)
#     influence_size = serializers.CharField(required=False)
#     genre = serializers.CharField(required=False)
#     category_vertical = serializers.CharField(required=False)
#     category_vertical2 = serializers.CharField(required=False)
#     product_traits = serializers.CharField(required=False)
#     creator_traits = serializers.CharField(required=False)
#     production_type = serializers.CharField(required=False)
#     current_revenue = serializers.CharField(required=False)
#     predicted_revenue = serializers.CharField(required=False)
#     creator_audience_traits = serializers.CharField(required=False)
#     sysops_solution_hypothesis = serializers.CharField(required=False)
#     additional_notes = serializers.CharField(required=False)
#     created_at = serializers.CharField(required=False)
#     modified_at = serializers.CharField(required=False)

#     def create(self, validated_data):
#         return SysOpsDemandNode.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.demand_metauserID = validated_data.get(
#             'demand_metauserID', instance.demand_metauserID)
#         instance.bla_ScoreID = validated_data.get(
#             'bla_ScoreID', instance.bla_ScoreID)
#         instance.opsec_agent_hashkey = validated_data.get(
#             'opsec_agent_hashkey', instance.opsec_agent_hashkey)
#         instance.name = validated_data.get('name', instance.name)
#         instance.location = validated_data.get('location', instance.location)
#         instance.status = validated_data.get('status', instance.status)
#         instance.tokens_allocated = validated_data.get(
#             'tokens_allocated', instance.tokens_allocated)
#         instance.creator_hypothesis = validated_data.get(
#             'creator_hypothesis', instance.creator_hypothesis)
#         instance.SysOpsAgent_hypothesis = validated_data.get(
#             'SysOpsAgent_hypothesis', instance.SysOpsAgent_hypothesis)
#         instance.creator_identity_status = validated_data.get(
#             'creator_identity_status', instance.creator_identity_status)
#         instance.all_digital_url = validated_data.get(
#             'all_digital_url', instance.all_digital_url)
#         instance.influence_size = validated_data.get(
#             'influence_size', instance.influence_size)
#         instance.genre = validated_data.get('genre', instance.genre)
#         instance.category_vertical = validated_data.get(
#             'category_vertical', instance.category_vertical)
#         instance.category_vertical2 = validated_data.get(
#             'category_vertical2', instance.category_vertical2)
#         instance.product_traits = validated_data.get(
#             'product_traits', instance.product_traits)
#         instance.creator_traits = validated_data.get(
#             'creator_traits', instance.creator_traits)
#         instance.production_type = validated_data.get(
#             'production_type', instance.production_type)
#         instance.current_revenue = validated_data.get(
#             'current_revenue', instance.current_revenue)
#         instance.predicted_revenue = validated_data.get(
#             'predicted_revenue', instance.predicted_revenue)
#         instance.creator_audience_traits = validated_data.get(
#             'creator_audience_traits', instance.creator_audience_traits)
#         instance.sysops_solution_hypothesis = validated_data.get(
#             'sysops_solution_hypothesis', instance.sysops_solution_hypothesis)
#         instance.additional_notes = validated_data.get(
#             'additional_notes', instance.additional_notes)
#         instance.created_at = validated_data.get(
#             'created_at', instance.created_at)
#         instance.modified_at = validated_data.get(
#             'modified_at', instance.modified_at)

#         instance.save()
#         return instance
