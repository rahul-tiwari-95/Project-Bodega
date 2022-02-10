from pyexpat import model
from django.contrib.auth.models import User, Group
from .models import Chat_Room, Collaboration, Discount, MetaUser, Product, Product_Category, Product_Themes, Social, User_Address, User_Payment, User_Type, Particpants, Message
from rest_framework import serializers


#Serializer Class
#Call your models here and safely plug into REST API's format
#Its very secure, because only the fields you will call can be edited.
#Fields which arent mentioned wont be retreived, keeping the DB safe & "technically" untouchec



#Admin Serializer Class


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        model = User
        fields = ['url', 'username']


#--------END-ADMIN-Serializer-Class-------------------


#Backend Models Serializer Class - This data is for Engineers. So, all fields were requested. '
#We will make another version for the user


#Serializer for MetaUser
class MetaUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MetaUser
        fields = ['meta_username', 'password', 'hashkey', 'email', 'created_at', 'modified_at   ']




#Serializer for User Address Class
class UserAddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_Address
        fields = ['user_ID', 'address_line1', 'address_line2', 'address_state', 'city', 'postal_code', 'country']



#Serializer for User Payment Class
class UserPaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_Payment
        fields = ['user_ID', 'payment_type', 'payment_status']



#Serializer for User Type Class
class UserTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_Type
        fields = ['user_ID','user_role', 'created_at']


#Serializer for Chat_Room Class
class ChatRoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chat_Room
        fields = ['name', 'type_of_room', 'is_room_active']



#Serializer for Particpants Class
class ParticpantsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Particpants
        fields = ['user_ID', 'chat_room_ID']



#Serializer for Message Class
class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ['chat_room_ID', 'user_ID', 'message_body', 'upload_file', 'created_at', 'modified_at', 'hashkey']



#Serializer for Product Category Class
class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product_Category
        fields = ['category_name', 'category_desc', 'category_image1', 'category_image2', 'category_image3', 'modified_at']



#Serializer for Product Themes Class
class ProductThemesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product_Themes
        fields = ['collection_name', 'collection_desc', 'audience_traits', 'marketing_funnel', 'modified_at', 'created_at']




#Serializer for Discount Class
class DiscountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Discount
        fields = ['discount_name', 'discount_desc', 'discount_percent', 'active_status', 'created_by', 'modified_at']


#Serializer for Social Class
class SocialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Social
        fields = ['user_ID', 'following', 'followers', 'likes', 'comments', 'products_clickedOn', 'bio', 'data_mining_status', 'account_active', 'delete_metauser']




#Serializer for Collab class
class CollaborationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Collaboration
        fields = ['collab_name', 'collab_desc', 'collab_type', 'user_ID', 'collab_status', 'creator_pitch', 'bid_type', 'bid_amount', 'accept_bid', 'created_at','modified_at' ]




#Serializer for Product Class
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'desc',
            'sku',
            'product_categoryID',
            'product_themesID',
            'collaborationID',
            'has_multiple_variants',
            'discount_ID',
            'shop_ID',
            'total_sales',
            'clicks_on_product',
            'created_by',
            'is_product_digital',
            'is_product_sharable',
            'product_unique_traits',
            'customer_unique_traits',
            'nsfw_content',
            'production_cost',
            'production_time_days',
            'hours_invested',
            'encrypt_product',
            'units_sold_expectation',
            'size_chart',
            'product_image1',
            'product_image2',
            'product_images3',
            'hashkey',
            'created_at',
            'modified_at',
        ]