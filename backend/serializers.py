from django.contrib.auth.models import User, Group
from .models import Cart_Item, Chat_Room, Collaboration, Discount, MetaUser, Order_Detail, Order_Item, Product, Product_Category, Product_Themes, Shop_Payout, Shopping_Session, Social, Shop, User_Address, User_Payment, User_Type,  Particpant, Message
from rest_framework import serializers


#Serializer Class for Developers
#wherever possible, apply constraints
#GET functions arent defined explicitly because we are just reading data - so no corruption can be done  

#validated_data = data which needs to be requested or posted
#instance = this is the instance of the model with pk=id

collab_type_array = [ #the bid our creator wants to do but depends on mutual consent of other party - because freedom of fucking choice
        ('FIXED-PAYMENT', 'FIXED-PAYMENT'),
        ('BARTER-DEAL', 'BARTER-DEAL'),
        ('COMMISSION-%-ON-SALES','COMMISSION-%-ON-SALES'),
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
        ('CLOSED-SECURE-ROOM', 'CLOSED-SECURE-ROOM'),#only people with meta_key can join the secure_room
        ('OPEN-SECURE-ROOM', 'OPEN-SECURE-ROOM'),#anyone can join the secure room
        ('INITIATE-ROOM-TERMINATION', 'INITIATE-ROOM-TERMINATION') #leads ro the deletion of the room
    ]
#Before deployment -> use this link for data: https://github.com/hampusborgos/country-flags/blob/main/countries.json

product_category_array = [
        ('SHIRTS', 'SHIRTS' ),
        ('BOTTOMS', 'BOTTOMS'),
        ('SNEAKERS', 'SNEAKERS'),
        ('THERMALS', 'THERMALS'),
        ('SHORTS', 'SHORTS'),
        ('HOME-DECOR', 'HOME-DECOR'),
        ('DIGITAL-ART', 'DIGITAL-ART'),
        ('MUSIC-FILE', 'MUSIC-FILE'),
        ('COLLECTIBLES','COLLECTIBLES'),
        ('PHYSICAL-ACCESSORIES', 'PHYSICAL-ACCESSORIES'),
        ('DIGITAL-ACCESSORIES', 'DIGITAL-ACCESSORIES'),
        ('POTRAIT-VIDEO-FILE', 'POTRAIT-VIDEO-FILE'),]

#Serializer for User Class under Django-Admin 





#Serializer template for MetaUser
class MetaUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) 
    password = serializers.CharField(required=True, max_length=100)
    hashkey = serializers.CharField(default='sha1 hash key', read_only=True)
    email = serializers.CharField(required=False)
    created_at = serializers.CharField(required=True)
    modified_at = serializers.CharField(required=True)
    #creating functions which will execute on Serializers and create model instances.
    #this allows us to secure the access to db directly.
    def create(self, validated_data):
        #Creating new instances of the MetaUser model  

        return MetaUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        #Updating instances of our model - here instance refers to id number and validated_data refers to body of the instance

        instance.password = validated_data.get('password', instance.password)
        instance.hashkey = validated_data.get('hashkey', instance.hashkey)
        instance.email = validated_data.get('email', instance.email)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.modified = validated_data.get('modified_at', instance.modified_at)

        instance.save()
        return instance




#Serializer for User Address Class
class UserAddressSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_ID = serializers.CharField(required=True)
    address_line1 = serializers.CharField(required=False)
    address_line2 = serializers.CharField(required=False)
    address_state = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    postal_code = serializers.CharField(required=False)
    country = serializers.ChoiceField(choices=country_list, default='ISR')
    created_at = serializers.CharField(required=True)
    modified_at = serializers.CharField(required=True)

    #create() and update() functions interact with our DB not the APIs directly  
    def create(self, validated_data):
        #creating a new instance of the UserAddress Model
        return User_Address.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        #updating a model instance with only the validated_fields  
        instance.address_line1 = validated_data.get('address_line1', instance.address_line1)
        instance.address_line2 = validated_data.get('address_line2', instance.address_line2)
        instance.address_state = validated_data.get('address_state', instance.address_line2)
        instance.city = validated_data.get('city', instance.city)
        instance.postal_code = validated_data.get('postal_code', instance.postal_code)
        instance.country = validated_data.get('country', instance.country)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.modfied_at = validated_data.get('modified_at', instance.modified_at)

        instance.save()
        return instance



#Serializer User Payment Class
class UserPaymentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_ID = serializers.CharField(required=True)
    payment_type = serializers.ChoiceField( choices=payment_types, default='PAYPAL')
    payment_provider = serializers.CharField(required=True)
    payment_status = serializers.BooleanField(required=True)
    total_money_out = serializers.FloatField()
    total_money_in = serializers.FloatField()
    user_payment_profile_status = serializers.BooleanField(required=True)
    #add code for routing money via Stripe to multiple vendors  
    #all data can be fetched via FE, they can route this data here  
    created_at = serializers.CharField(required=True)
    modified_at = serializers.CharField(required=True)


    #create() and update() functions to interact with our DB
    def create(self, validated_data):
        #returns a new model instance with yhe validated data as input 
        return User_Payment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        #passes validated_data field to instance
        #.get() fetches that field name from the POST request data and updates the field of User_Payment table
        instance.user_ID = validated_data.get('user_ID', instance.user_ID)
        instance.payment_type = validated_data.get('payment_type', instance.payment_ID)
        instance.payment_provider = validated_data.get('payment_provider', instance.payment_provider)
        instance.payment_status = validated_data.get('payment_status', instance.payment_status)
        instance.total_money_out = validated_data.get('total_money_out', instance.total_money_out)
        instance.total_money_in = validated_data.get('total_money_in', instance.total_money_in)
        instance.user_payment_profile_status = validated_data.get('user_payment_profile_status', instance.user_payment_profile_status)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.modified_at = validated_data.get('modified_at', instance.modified_at)

        instance.save()
        return instance



#Serializer for User Type Class
class UserTypeSerializer (serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_ID = serializers.CharField(required=True)
    user_role = serializers.ChoiceField(choices=user_role_array, default='Creator')
    created_at = serializers.CharField(required=True)
    modified_at = serializers.CharField(required=True)
    digital_base_personality = serializers.CharField(required=False)
    digital_future_personality = serializers.CharField(required=False) 
    about_you_belief = serializers.CharField(required=True)
    about_you_belief2 = serializers.CharField(required=True)
    about_you_disbelief = serializers.CharField(required=True)
    why_did_you_join_bodega = serializers.CharField(required=True)
    explore_bodega_preferences = serializers.CharField(required=True)
    member_feedback_preferences = serializers.CharField(default='What new features would you like to see?')
    feedback_bodega = serializers.CharField(required=True)
    describe_yourself = serializers.CharField(required=True)
    shoe_size = serializers.FloatField(required=False)
    waist_size = serializers.CharField(required=False)
    chest_size = serializers.CharField(required=True)

    #create() and update() functions to interact with our DB
    def create(self, validated_data):
        #returns a new instance of our model
        return User_Type.objects.create(**validated_data)

    
    def update(self, instance, validated_data):
        #appends model instance values
        instance.user_ID = validated_data.get('user_ID', instance.user_ID)
        instance.user_role = validated_data.get('user_role', instance.user_role)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.modified_at = validated_data.get('modified_at', instance.modified_at) 
        instance.digital_base_personality = validated_data.get('digital_base_personality', instance.digital_base_personality)
        instance.digital_future_personality = validated_data.get('digital_future_personality', instance.digital_future_personality)
        instance.about_you_belief = validated_data.get('about_you_belief', instance.about_you_belief)
        instance.about_you_belief2 = validated_data.get('about_you_belief2', instance.about_you_belief2)
        instance.about_you_disbelief = validated_data.get('about_you_disbelief', instance.about_you_disbelief)
        instance.why_did_you_join_bodega = validated_data.get('why_did_you_join_bodega', instance.why_did_you_join_bodega)
        instance.explore_bodega_preferences = validated_data.get('explore_bodega_preferences', instance.explore_bodega_preferences)
        instance.member_feedback_preferences = validated_data.get('member_feedback_preferences', instance.member_feedback_preferences)
        instance.feedback_bodega = validated_data.get('feedback_bodega', instance.feedback_bodega)
        instance.describe_yourself = validated_data.get('describe_yourself', instance.describe_yourself)
        instance.shoe_size = validated_data.get('shoe_size', instance.shoe_size)
        instance.waist_size = validated_data.get('waist_size ', instance.waist_size )
        instance.chest_size = validated_data.get('chest_size', instance.chest_size)

        instance.save()
        return instance



#Serializer Class for Chat Room Model
class ChatRoomSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    desc = serializers.CharField(required=True)
    rules = serializers.CharField(required=False)
    type_of_room = serializers.ChoiceField(choices=type_of_room_array, required=True)
    created_on = serializers.CharField(required=True)
    modified_on = serializers.CharField(required=True)
    is_room_active = serializers.BooleanField(required=True)

    #create() and update() funrctions to interaact with our DB
    def create(self, validated_data):
        #returns a new model instance
        return Chat_Room.objects.create(**validated_data)

    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.rules = validated_data.get('rules', instance.rules)
        instance.type_of_room = validated_data.get('type_of_room', instance.type_of_room)
        instance.created_on = validated_data.get('created_on', instance.created_on)
        instance.is_room_active = validated_data.get('is_room_active', instance.is_room_active)

        instance.save()
        return instance



#Serializer class for Particpant model 
class ParticpantSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_ID = serializers.CharField(required=True) #FK
    chat_room_ID = serializers.CharField(required=True) #FK2

    #create() and update() functions to interact with our DB
    def create(self, validated_data):
        #returns a new model instance 
        return Particpant.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_ID = validated_data.get('user_ID', instance.user_ID)
        instance.chat_room_ID = validated_data.get('chat_room_ID', instance.chat_room_ID)

        instance.save()
        return instance


#Serializer class for Message model
class MessageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    chat_room_ID = serializers.CharField(required=True)
    user_ID = serializers.CharField(required=True)
    message_body = serializers.CharField(required=True)
    upload_file = serializers.CharField(required=False)
    created_at = serializers.CharField(required=True)
    modified_at = serializers.CharField(required=True)
    hashkey = serializers.CharField(read_only=True)

    #create() and update() functions to interact with our DB
    def create(self, validated_data):
        #returns a new model instance
        return Message.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.chat_room_ID = validated_data.get('chat_room_ID', instance.chat_room_ID)
        instance.user_ID = validated_data.get('user_ID', instance.user_ID)
        instance.message_body = validated_data.get('message_body', instance.message_body)
        instance.upload_file = validated_data.get('upload_file', instance.upload_file)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.modified_at = validated_data.get('modified_at', instance.modified_at)
        instance.hashkey = validated_data.get('hashkey', instance.hashkey)

        instance.save()
        return instance


#Serializer for Product Category Model
class ProductCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category_name = serializers.ChoiceField(required=True,choices=product_category_array)
    category_desc = serializers.CharField(required=True)
    created_at = serializers.CharField(required=True)
    modified_at = serializers.CharField(required=True)
    category_image1 = serializers.CharField(required=True)
    category_image2 = serializers.CharField(required=True)
    category_image3 = serializers.CharField(required=True)


    def create(self, validated_data):
        #returns a new model instance
        return Product_Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category_name = validated_data.get('category_name', instance.category_name)
        instance.category_desc = validated_data.get('category_desc', instance.category_desc)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.modified_at = validated_data.get('modified_at', instance.modified_at)
        instance.category_image1 = validated_data.get('category_image1', instance.category_image1)
        instance.category_image2 = validated_data.get('category_image2', instance.category_image2)
        instance.category_image3 = validated_data.get('category_image3', instance.category_image1)

        instance.save()
        return instance



#Serializer for Product Themes Model
class ProductThemesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    collection_name = serializers.CharField(required=True)
    collection_desc = serializers.CharField(required=True)
    audience_traits = serializers.CharField(required=True)
    marketing_funnel = serializers.ChoiceField(choices=marketing_funnel_array, required=True)
    created_at = serializers.CharField(required=True)
    modified_at = serializers.CharField(required=True)

    def create(self, validated_data):
        #returns a new model instance
        return Product_Themes.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.collection_name = validated_data.get('collection_name', instance.collection_name)
        instance.collection_desc = validated_data.get('collection_desc', instance.collection_desc)
        instance.audience_traits = validated_data.get('audience_traits', instance.audience_traits)
        instance.marketing_funnel = validated_data.get('marketing_funnel', instance.marketing_funnel)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.modified_at = validated_data.get('modified_at', instance.modified_at)
        
        instance.save()
        return instance





#Serializer for Discount model
class DiscountSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    discount_percent = serializers.FloatField(required=True)
    active_status = serializers.BooleanField(required=True)
    created_by = serializers.CharField(required=True)
    modified_at = serializers.CharField(required=True)

    def create(self, validated_data):
        return Discount.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.discount_percent = validated_data.get('discount_percent', instance.discount_percent)
        instance.active_status = validated_data.get('active_status', instance.active_status)
        instance.created_by = validated_data.get('created_by', instance.created_by)
        instance.modified_at = validated_data.get('modified_at', instance.modified_at)

        instance.save()
        return instance


#Serializer for Social model
class SocialSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_ID = serializers.CharField(required=True)
    following = serializers.CharField(required=True)
    followers = serializers.CharField(required=True)
    makeprofileprivate = serializers.BooleanField(required=True)
    saved_content = serializers.CharField(required=True)
    likes = serializers.CharField(required=True)
    comments = serializers.CharField(required=True)
    products_clickedOn = serializers.CharField(required=True)
    bio = serializers.CharField(required=True, allow_blank=True)
    blocked_list = serializers.CharField(required=True)
    data_mining_status = serializers.BooleanField(required=True)
    account_active = serializers.BooleanField( default=True)
    delete_metauser = serializers.BooleanField(default=False)
    created_on = serializers.CharField(required=True)
    modified_on = serializers.CharField(required=True)

    def create(self, validated_data):
        return Social.objects.create(**validated_data)

    
    def update(self, instance, validated_data):
        instance.user_ID = validated_data.get('user_ID', instance.user_ID)
        instance.following = validated_data.get('following', instance.following)
        instance.followers = validated_data.get('followers', instance.followers)
        instance.makeprofileprivate = validated_data.get('makeprofileprivate', instance.makeprofileprivate)
        instance.saved_content = validated_data.get('saved_content', instance.saved_content)
        instance.likes = validated_data.get('likes', instance.likes)
        instance.dislikes = validated_data.get('dislikes', instance.dislikes)
        instance.comments = validated_data.get('comments', instance.comments)
        instance.products_clickedOn = validated_data.get('products_clickedOn', instance.products_clickedOn)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.blocked_list = validated_data.get('blocked_list', instance.blocked_list)
        instance.data_mining_status = validated_data.get('data_mining_status', instance.data_mining_status)
        instance.account_active = validated_data.get('account_active', instance.account_active)
        instance.delete_metauser = validated_data.get('delete_metauser', instance.delete_metauser)
        instance.created_on = validated_data.get('created_on', instance.created_on)
        instance.modified_on = validated_data.get('modified_on', instance.modified_on)

        instance.save()
        return instance


#Serializer for Shop Model
class ShopSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_ID = serializers.CharField(required=True)
    all_products = serializers.CharField(required=True)
    all_user_data = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True) 
    logo = serializers.CharField(required=True)
    cover_image = serializers.CharField(required=True)
    address_line1 = serializers.CharField(required=True)
    address_line2 = serializers.CharField(required=True)
    city = serializers.CharField(required=True)
    state = serializers.CharField(required=True)
    postal_code = serializers.CharField(required=True)
    country = serializers.ChoiceField(choices=country_list) #Before deployment -> use this link for data: https://github.com/hampusborgos/country-flags/blob/main/countries.json
    shop_traits = serializers.CharField(required=True)
    assistance_ask = serializers.CharField(required=True)
    uniquesellingprop = serializers.CharField(required=True)
    data_mining_status = serializers.CharField(required=True)
    created_on = serializers.CharField(required=True)
    modified_on = serializers.CharField(required=True)


    def create(self, validated_data):
        return Shop.objects.create(**validated_data)

    
    def update(self, instance, validated_data):
        instance.user_ID = validated_data.get('user_ID', instance.user_ID)
        instance.all_products = validated_data.get('all_products', instance.all_products)
        instance.all_user_data = validated_data.get('all_user_data', instance.all_user_data)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.cover_image = validated_data.get('cover_image', instance.cover_image)
        instance.address_line1 = validated_data.get('address_line1', instance.address_line1)
        instance.address_line2 = validated_data.get('address_line2', instance.address_line2)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.postal_code = validated_data.get('postal_code', instance.postal_code)
        instance.country = validated_data.get('country', instance.country)
        instance.shop_traits = validated_data.get('shop_traits', instance.shop_traits)
        instance.assistance_ask = validated_data.get('assistance_ask', instance.assistance_ask)
        instance.uniquesellingprop = validated_data.get('uniquesellingprop', instance.uniquesellingprop)
        instance.data_mining_status = validated_data.get('data_mining_status', instance.data_mining_status)
        instance.created_on = serializers.CharField(required=True)
        instance.modified_on = serializers.CharField(required=True)

        instance.save()
        return instance




#most important fucking serializer class - be extra careful 
#Serializer for Product Model

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    selling_price = serializers.CharField(required=True)
    discounted_price = serializers.CharField(required=True)
    product_categoryID = serializers.CharField(required=True)
    product_themesID = serializers.CharField(required=True)
    discount_ID = serializers.CharField(required=True)
    shop_ID = serializers.CharField(required=True)
    quanity = serializers.IntegerField(required=True)
    total_sales = serializers.FloatField(required=True)
    clicks_on_product = serializers.IntegerField(required=True)
    created_by = serializers.CharField(required=True)
    is_product_digital = serializers.BooleanField(required=True)
    is_product_sharable = serializers.BooleanField(required=True)
    product_unqiue_traits = serializers.CharField(required=True)
    customer_unique_traits = serializers.CharField(required=True)
    nsfw_content = serializers.BooleanField(required=True)
    production_cost = serializers.FloatField(required=True)
    production_time_days = serializers.IntegerField(required=True)
    hours_invested = serializers.FloatField(required=True)
    encrypt_product = serializers.BooleanField(required=True)
    unit_sold_expectation = serializers.IntegerField()
    size_chart = serializers.CharField(allow_blank=True)
    product_image1 = serializers.CharField(required=True)
    product_image2 = serializers.CharField(allow_blank=True)
    product_image3 = serializers.CharField(allow_blank=True)
    hashkey = serializers.CharField(read_only=True) #Should be hidden by default
    created_at = serializers.CharField(required=True)
    modified_at = serializers.CharField(required=True)


    def create(self, validated_data):
        #returns a new model instance
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.selling_price = validated_data.get('selling_price', instance.selling_price)
        instance.discounted_price = validated_data.get('discounted_price', instance.discounted_price)
        instance.product_categoryID = validated_data.get('product_categoryID', instance.product_categoryID)
        instance.product_themesID = validated_data.get('product_themesID', instance.product_themesID)
        instance.discount_ID = validated_data.get('discount_ID', instance.discount_ID)
        instance.shop_ID = validated_data.get('shop_ID', instance.shop_ID)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.total_sales = validated_data.get('total_sales', instance.total_sales)
        instance.clicks_on_product = validated_data.get('clicks_on_product', instance.clicks_on_product)
        instance.created_by = validated_data.get('created_by', instance.created_by)
        instance.is_product_digital = validated_data.get('is_product_digital', instance.is_product_digital)
        instance.is_product_sharable = validated_data.get('is_product_sharable', instance.is_product_sharable)
        instance.product_unqiue_traits = validated_data.get('product_unqiue_traits', instance.product_unqiue_traits)
        instance.customer_unique_traits = validated_data.get('customer_unique_traits', instance.customer_unique_traits)
        instance.nsfw_content = validated_data.get('nsfw_content', instance.nsfw_content)
        instance.production_cost = validated_data.get('production_cost', instance.production_cost)
        instance.production_time_days = validated_data.get('production_time_days', instance.production_time_days)
        instance.encrypt_product = validated_data.get('encrypt_product', instance.encrypt_product)
        instance.unit_sold_expectation = validated_data.get('unit_sold_expectations', instance.unit_sold_expectations)
        instance.size_chart = validated_data.get('size_chart', instance.size_chart)
        instance.product_image1 = validated_data.get('product_image1', instance.product_image1)
        instance.product_image2 = validated_data.get('product_image2', instance.product_image2)
        instance.product_image3 = validated_data.get('product_image3', instance.product_image1)
        instance.hashkey = validated_data.get('hashkey', instance.hashkey)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.modified_at = validated_data.get('modified_at', instance.modified_at)

        instance.save()
        return instance



#Serializer for Collaboration class

class CollaborationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name =  serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    creator_collab_choice = serializers.ChoiceField(required=True, choices=collab_type_array)
    user_ID = serializers.CharField(required=True)
    product_ID = serializers.CharField(required=True)
    shop_ID = serializers.CharField(required=True)
    creator_pitch = serializers.CharField(required=True)
    bid_type = serializers.ChoiceField(choices=collab_type_array)
    bid_amount = serializers.FloatField(required=True)
    accept_bid = serializers.BooleanField(required=True)
    created_at = serializers.CharField(required=True)
    modified_at = serializers.CharField(required=True)


    def create(self, validated_data):
        return Collaboration.objects.create(**validated_data)

    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.code = validated_data.get('code', instance.code)
        instance.description = validated_data.get('description', instance.description)
        instance.creator_collab_choice = validated_data.get('creator_collab_choice', instance.creator_collab_choice)
        instance.bid_type = validated_data.get('bid_type', instance.bid_type)
        instance.bid_amount = validated_data.get('bid_amount', instance.bid_amount)
        instance.accept_bid = validated_data.get('accept_bid', instance.accept_bid)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.modified_at = validated_data.get('modified_at', instance.modified_at)

        instance.save()
        return instance




#Shopping Session Serializer Class 
class ShoppingSessionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    total_amount = serializers.FloatField(required=True)
    created_at = serializers.CharField(required=True)
    modified_at = serializers.CharField(required=True)

    def create(self, validated_data):
        return Shopping_Session.objects.create(**validated_data)

    
    def update(self, instance, validated_data):
        instance.total_amount = validated_data.get('total_amount', instance.total_amount)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.modified_at = validated_data.get('modified_at', instance.modified_at)

        instance.save()
        return instance



#Cart Item Serializer
class CartItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    session_ID = serializers.CharField(required=True)
    product_ID = serializers.CharField(required=True)
    quantity = serializers.IntegerField(required=True)
    created_at = serializers.CharField(required=True)
    modified_at = serializers.CharField(required=True)

    def create(self, validated_data):
        return Cart_Item.objects.create(**validated_data)

    
    def update(self, instance, validated_data):
        instance.session_ID = validated_data.get('session_ID', instance.session_ID)
        instance.product_ID = validated_data.get('product_ID', instance.product_ID)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.modified_at = validated_data.get('modified_at', instance.modified_at)

        instance.save()
        return instance



#Order Details Serializer class
class OrderDetailsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    total_amount = serializers.FloatField(required=True)
    payment_info = serializers.CharField(required=True)
    created_at = serializers.CharField(required=True)
    modified_at = serializers.CharField(required=True)

    def create(self, validated_data):
        return Order_Detail.objects.create(**validated_data)

    
    def update(self, instance, validated_data):
        instance.total_amount = validated_data.get('total_amount', instance.total_amount)
        instance.payment_info = validated_data.get('payment_info', instance.payment_info)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.modified_at = validated_data.get('modified_at', instance.modified_at)

        instance.save()
        return instance



#Order Items Serializer Class
class OrderItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    order_ID = serializers.CharField(required=True)
    product_ID = serializers.CharField(required=True)
    quantity = serializers.IntegerField(required=True)
    created_at = serializers.CharField(required=True)
    modified_at = serializers.CharField(required=True)

    def create(self, validated_data):
        return Order_Item.objects.create(**validated_data)

    
    def update(self, instance, validated_data):
        instance.order_ID = validated_data.get('order_ID', instance.order_ID)
        instance.product_ID = validated_data.get('product_ID', instance.product_ID)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.modified_at = validated_data.get('modified_at', instance.modified_at)

        instance.save()
        return instance




#Shop Payout Serializer Class
#NOT COMPLETED
#Need to revisit after seeing Stipe Connect
class ShopPayoutSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    order_detail_ID = serializers.CharField(required=True)

    def create(self, validated_idea):
        return Shop_Payout.objects.create(**validated_idea)

    
    def update(self, instance, validated_idea):
        instance.order_detail_ID = validated_idea.get('order_detail_ID', instance.order_detail_ID)