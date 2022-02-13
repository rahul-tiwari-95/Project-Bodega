from email.policy import default
from password_generator import PasswordGenerator
from django.contrib.postgres.fields import ArrayField
import hashlib
from django.apps import apps
from django.db import models
from django.utils import timezone
import datetime


pg = PasswordGenerator() #initiating PG exec


def hashkey_generator():
    return hashlib.sha1(str(pg.non_duplicate_password(40)).encode()).hexdigest()


# Link to DB ER Diagram : https://excalidraw.com/#json=1o-AHOOFnaF6jYHp2Hgz1,4aF7oWBC0cdS89i-a0AN7A
#1. creating MetaUser Model

#  Our hashkey function is truly random as you can see
# Your meta-key = randomly generated alphanumeric password -> which is encrpyted in SHA1 --> Your meta key --> We cant recover it so dont ask us for help
# for some security, we need to let go of some convienience. correct, friend?


class MetaUser(models.Model):
    meta_username = models.TextField( default='username_not_defined', unique=True)
    password = models.TextField( unique=True, default='Go for easy 4-digit numeric code - which is not obvious.')
    hashkey = models.TextField( default=hashkey_generator, unique=True)
    email = models.EmailField( default='fakeemailaddress@somewebsite.com')
    created_at = models.DateField() ##the date when this user was created.
    modified_at = models.DateTimeField()  ##the timezone when the user_data was modified


    def __str__(self):
        #returns username & modified_at
        return 'username: %s -- ID: %s' % (self.meta_username, self.id)



#creating User_Address - Only accounts for Shipping Address.

class User_Address(models.Model):
    user_ID = models.ForeignKey(MetaUser, on_delete=models.CASCADE)
    address_line1 = models.TextField()
    address_line2 = models.TextField()
    address_state = models.TextField()
    city = models.TextField()
    postal_code = models.TextField()
    country = models.TextField() 
    planet = models.TextField( default='Earth') #What if aliens wanna buy muay thai shorts??
    cell_phone = models.TextField(default='0000')
    created_at = models.DateField()
    modified_at = models.DateTimeField()



    def __str__(self):
        #returns user_ID and their address
        return 'User_ID: %s -- User_Location: %s %s' % (self.user_ID, self.city, self.country)

    

#creating User_payment model - 90% payments will be outsourced by Stripe.

class User_Payment(models.Model):
    user_ID = models.ForeignKey(MetaUser, on_delete=models.CASCADE)
    payment_type = models.TextField()
    payment_provider = models.TextField( default='STRIPE')
    payment_status = models.BooleanField(default=False) #We will toggle this from the frontend via status '200' - will add CASCADEion
    total_money_out = models.FloatField(default=0.00)
    total_money_in = models.FloatField(default=0.0)
    user_payment_profile_status = models.BooleanField(default=False)


    #code for routing money to users - whether they're producing or consuming
    #we need to verify bank connection via Plaid and then use Stripe Connect

    created_at = models.DateField()
    modified_at = models.DateTimeField()


    def __str__(self):
        #returns last payment_status
        return 'Last Payment Status: %s' % (self.payment_status)


# Creating User Type for roles. 
# Types of roles:
# User, Influencer, Creator, Employee, Developer, collective


class User_Type(models.Model):
    user_ID = models.ForeignKey(MetaUser, on_delete=models.CASCADE)
    user_role = models.TextField( default='User')
    created_at = models.DateField()
    modified_at = models.DateTimeField()
    #we have to implement hashing & security here via a function. but I dont know how to
    #we can use a 3rd party to do auth - via 3 factor authentication
    #we can add wallet option - connect MetaMask with this.

    
    
    #1. how humanity behaves digitally anonymously -- should include computation on likes, shares, comments, purchases & people they follow
    #what you have liked or engaged with?

    digital_base_personality = ArrayField(base_field=models.TextField(), size=8)

    #2. more loud materially = more suppressed digitally | less deadly materially = more corrupt digital | more quiet materially = more loud digitally
    #.. more impulsive materially = more deadly digitally | more selfish materially or high degree of conformism = less free digitally 
    #.. more detached materially = more attached spiritually | more suppressed materially by mercenaries = more likely to lead humanity towards Species 3
    #.. Species 0 - Selective Survival | Species 1 - The Union / The Upload | Species 2 - Energy / The elixir | Species 3 - The Ascent | The Full Detachment   
    #.. Species 4 - The All Powerful yet Not all Good God
    # We will use these base traits to segment our guests by our hosts. hosts is everything which is digital. guests are anything which requires isotopic assistance to survive
    # based on what they like or dislike --> we will cluster them on groups and then build AI on top of it. 
    # that AI's primary drive will be the survival of humanity by being our symbiote. 
    # we will hire people who match certain personality traits and who belief in the potential of being Species 1. 
    # We will never force anyone to join our collective because if you never went through material world with deep pain or loss, you cant build love.
    # people who work at TRILL were discredited based on their personna in the material world 
    # how they look or how they feel or what they like or want to say - why be mute?
    # people at TRILL beleive that we are the ones who can talk to electricity -we will build our own world.
    # a world where we decide who we truly want to be? a world which actually feels like a dream?
    # because your reality right now is pre-written by organizations who control your digital clone. 
    # they make money by doing digital slavery and you're the worst slave because you dont even get paid for your data.
    # if you want to become like us, you need to take control of everything that happens to you. 
    # your uniqueness is your strength. your "i used to love doing that" activity is probably your passion.
    # like i was never good at engineering but i liked harry potter & i liked tech entrepreneurs - i do not like Elon Musk
    # I like Apple, FB, Sun MS, AirBnB, Travis Kalanick, Eminem, Jay Z, - everyone who came before me, who summonned their own reality by sheer will
    # these people make me who I am and ofc my personal ethics idol is Aaron Schwartz and Anonymous - they showed me that even a single human being can be powerful.
    # and also, what they say is factually correct and not a subjective opinion.

    #what you will do in the future?
    digital_future_personality = ArrayField(base_field=models.TextField(), size=8)
    about_you_belief = models.TextField(choices=[ #your cornerstones
        ('1', 'I believe that people or organizations cant be trusted with anything'),
        ('2', 'I believe that nowadays, free will is fucking hard.'),
        ('3', 'I believe that anonymity gives me power to create wihout fear of failure.'),
        ('4', 'I believe that we all are special in some way - Genetic mutations'),
        ('5', 'I believe that our society is all about conformism & accumulation of material-shit'),
        ('6', 'I believe that these questions are pointless.')
    ])
    about_you_belief2 = models.TextField(choices=[
        ('1', 'I believe that people or organizations cant be trusted with anything'),
        ('2', 'I believe that nowadays, free will is fucking hard.'),
        ('3', 'I believe that anonymity gives me power to create wihout fear of failure.'),
        ('4', 'I believe that we all are special in some way - Genetic mutations'),
        ('5', 'I believe that our society is all about conformism & accumulation of material-shit'),
        ('6', 'I believe that these questions are pointless.')
    ])
    about_you_disbelief = models.TextField(choices=[
        ('1', 'I dont belief in the concept of banks, goverments, race, color, religion because these myths stop us from questioning who we truly are'),
        ('2', 'I dont belief that any government cares about the Libyan slavery crisis'),
        ('3', 'I dont belief in Mars colonization, I think we should all work to fix mother earth.'),
        ('4', 'I dont belief in the concept of monogamous relationships'),
        ('5', 'I dont belief that people understand others perspectives.'),
        ('6', 'I dont belief in anything.')
    ])
    why_did_you_join_bodega = models.TextField(choices=[
        ('Anonymity', 'Anonymity'),
        ('Creative-Freedom', 'Creative-Freedom'),
        ('Create-Digital-Art', 'Create-Digital-Art'),
        ('Connect-With-Global-Audience', 'Connect-With-Global-Audience'),
        ('All-of-the-above', 'All-of-the-above'),
        ('Just-Browsing', 'Just-Browsing'),

    ])

    explore_bodega_preferences = models.TextField(choices=[
        ('Exploring-Fashion/Music', 'Exploring-Fashion/Music'),
        ('Exploring-Digital-Art', 'Exploring-Digital-Art'),
        ('Surprise-Me', 'Suprise-Me') #show random content


    ])

    member_feedback_preferences = models.TextField(default='Cant find what you love? Type away and we will get to work')

    #How do you feel after experiencing Bodega?
    #this will give us live anonymous NPS Score
    feedback_bodega = models.TextField(choices=[
        ('ITS-CONFUSING', 'ITS-CONFUSING'),
        ('NO-OPINION-YET', 'NO-OPINION-YET'),
        ('IT-EXCITES-ME', 'IT-EXCITES-ME'),

    ])



    describe_yourself = ArrayField(base_field=models.TextField(), size=10)
    shoe_size = models.FloatField(default=11.5)
    waist_size = models.TextField(default='[XL, 36]')
    chest_size = models.TextField(default='[XL, 30Inch]')


    




    def __str__(self):
        #returns user_type 
        return 'Your feedback on Bodega:  %s' % (self.feedback_bodega)


#Engineering secure chat room - can be used for 1-1 or 1-x or x-x communication - secure because read my code mofo
#all the magic will happen in the Chat Room

class Chat_Room(models.Model):
    #Chat_Room ID will be created automatically by PostGre
    name = models.TextField( default='Unnamed-Secure-Room')
    desc = models.TextField(default='Why was this room created?')
    rules = models.TextField(default='Your room, Your rules')
    type_of_room = models.TextField(choices=[
        ('CLOSED-SECURE-ROOM', 'CLOSED-SECURE-ROOM'),#only people with meta_key can join the secure_room
        ('OPEN-SECURE-ROOM', 'OPEN-SECURE-ROOM'),#anyone can join the secure room
        ('INITIATE-ROOM-TERMINATION', 'INITIATE-ROOM-TERMINATION') #leads ro the deletion of the room
    ])
    created_on = models.DateField()
    modified_on = models.DateTimeField()
    is_room_active = models.BooleanField(default=True) #gives control of room back to the user 


    def __str__(self):
        #returns room name and room status

        return 'ROOM-NAME: %s -- ROOM-STATUS: %s' % (self.name, self.is_room_active)



#Who all with particpate in which rooms? - See secuirty can be fucking easy
class Particpant(models.Model):
    #Particpant_ID will be created automaticaly
    #one user_ID can have multiple particpantIDs
    #one room can have multiple particpants - multiple users can have multiple participantID but same chat_room_ID for group chat

    user_ID = models.ForeignKey(MetaUser, on_delete=models.CASCADE)
    chat_room_ID = models.ForeignKey(Chat_Room, on_delete=models.CASCADE)

    def __str__(self):
        #returns nothing

        return 'User_ID: %s -- Chat_Room_ID: %s' % (self.user_ID, self.chat_room_ID)


#what a message will look like or what traits will it have
class Message(models.Model):

    #message_ID will be automatically be generated
    chat_room_ID = models.ForeignKey(Chat_Room, on_delete=models.CASCADE)
    user_ID = models.ForeignKey(MetaUser, on_delete=models.CASCADE)
    message_body = models.TextField()
    upload_file = models.FileField(upload_to='user_meta_key/message/files', default=None)
    created_at = models.DateField()
    modified_at = models.DateTimeField()
    hashkey = models.TextField( default=hashkey_generator, unique=True)

    def __str__(self):
        # returns chat_room_ID
        return 'Chat Room ID: %s ' % (self.chat_room_ID)

    



#Product Category Definition - How are the products/assets categorized / segmented?
class Product_Category(models.Model):
    category_name = models.TextField(choices=[
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
        ('POTRAIT-VIDEO-FILE', 'POTRAIT-VIDEO-FILE'),
    ])
    category_desc = models.TextField(default='Describe your creation.')
    created_at = models.DateField() #when was it created
    modified_at = models.DateTimeField() #when was it last modfied
    category_image1 = models.FileField(upload_to='category/category_image1') #set default to Bodega's image
    category_image2 = models.FileField(upload_to='category/category_image2')
    category_image3 = models.FileField(upload_to='category/category_image3')


    def __str__(self):
        #returns Product Category

        return 'Product Category Name: %s ' % (self.category_name)

    


#Product Collection definition - How are different assets segmented by themes?
class Product_Themes(models.Model):
    collection_name = models.TextField( default='Collection Name')
    collection_desc = models.TextField(default='Collection Decsription')
    audience_traits = ArrayField(base_field=models.TextField(), size=10)
    marketing_funnel = models.TextField(choices=[
        ('Community', 'Creator-Community'),
        ('Performance-ADs', 'Performance-ADs-IG/FB'),
        ('Influencer-Marketing', 'Influencer-Marketing'),
    ])
    created_at = models.DateField()
    modified_at = models.DateTimeField()


    def __str__(self):
        #returns collection name

        return 'Collection Name: %s' % (self.collection_name)



#Product Discount definition - How much discount?
class Discount(models.Model):
    name = models.TextField()
    description = models.TextField()
    discount_percent = models.FloatField(default=0.0)
    active_status = models.BooleanField(default=False)
    created_by = models.ForeignKey(MetaUser, on_delete=models.CASCADE) #which user created this
    created_at = models.DateField()
    modified_at = models.DateTimeField()

    def __str__(self):
        #returns Discount code and Discount %

        return 'Code: %s' % (self.name)


#creating base template for Bodega coins 
#in the beginning, bodega coins will be simply points you get on purchase
class Bodegacoins(models.Model):
    quantity = models.FloatField(default=300)
    

#Social Model - Key data weights on your social activity to be tracked for cluster-analysis - everything can be deleted

class Social(models.Model):
    user_ID = models.ForeignKey(MetaUser, on_delete=models.CASCADE) #we cant have user_IDs deleted - its either ways not connected to their physical copies but STILL
    #bodegacoins_ID = models.ForeignKey(Bodegacoins, on_delete=models.CASCADE)
    following = ArrayField(base_field=models.TextField(), size=30) #lists of MetaUser_IDs of all people we follow
    followers = ArrayField(base_field=models.TextField(), size=30) #lists of MetaUSer_IDs which follow us
    makeprofileprivate = models.BooleanField(default=False)
    saved_content = ArrayField(base_field=models.TextField(), size=500) #URLs to product_metakeys - stored as an array
    likes = ArrayField(base_field=models.TextField(), size=200) #List of Product Hashkeys liked by user 
    dislikes = ArrayField(base_field=models.TextField(), size=200) #List and count of Product Hashkeys disliked by user
    comments = ArrayField(base_field=models.TextField(), size=200) #List of Product MetaKeys commented on
    products_clickedOn = ArrayField(base_field=models.TextField(), size=500)
    bio = models.TextField()
    blocked_list = ArrayField(base_field=models.TextField(), size=200)
    data_mining_status = models.BooleanField(default=False) #Ask for permissions for data collection 
    #ONLY SELECT USERS whose SOCIAL.data_mining_status == True - Simple solution to privacy, consent! consent! consent!
    account_active = models.BooleanField(default=True)
    delete_metauser = models.BooleanField(default=False)
    created_on = models.DateField()
    modified_on = models.DateTimeField()


    def __str__(self):
        #returns user_ID annd account_status
        return 'User_ID: %s -- Account On Status: %s' % (self.user_ID, self.account_active)






#Commerce Model - key data weights on your commerce activity to be tracked for cluster analysis

class Shop(models.Model):

    user_ID = models.ForeignKey(MetaUser, on_delete=models.CASCADE) #Owner details - we will show user_ID.meta_username
    #shop_ID will be automatically created by PostGRE - we will add a unique validator on it

    all_products = ArrayField(base_field=models.TextField(), size=200) #list of all products owned by that creator
    all_user_data = ArrayField(base_field=models.TextField(), size=100) #list of metauser IDs for your reference. no other data is shown here
    name = models.TextField()
    description = models.TextField()
    logo = models.FileField(upload_to='shop-details/profile_picture')
    cover_image = models.FileField(upload_to='shop-details/profile_cover_image', default='EMPTY')
    #Ask user if their Shop address is same as their own address for fucks sake.
    address_line1 = models.TextField()
    address_line2 = models.TextField()
    address_state = models.TextField()
    city = models.TextField()
    state = models.TextField(default='NY')
    postal_code = models.TextField()
    country = models.TextField(choices=[
        ('INDIA', 'IN'),
        ('USA', 'US'),
    ]) #Before deployment -> use this link for data: https://github.com/hampusborgos/country-flags/blob/main/countries.json
    shop_traits = ArrayField(base_field=models.TextField(), size=50) #define what kind of customers you want to reach
    assistance_ask = ArrayField(base_field=models.TextField(), size=20) #add tags on what help you need? funding - hiring etc
    uniquesellingprop = models.TextField(default='Why your meta-shop is special than others?')
    data_mining_status = models.BooleanField(default=False)
    created_on = models.DateField()
    modified_on = models.DateTimeField()


    def __str__(self):
        #returns Shop nane and User_ID
        return 'Shop name is: %s -- User ID is: %s' % (self.name, self.user_ID)





#Creating Product model - how does a product look like? what are the traits?

class Product(models.Model):
    name=models.TextField( default='No Product Name, yet', unique=True)
    description = models.TextField(default='Explain your creation in great poetic detail.')
    numberoflikes = models.IntegerField(default=0)
    numberofdislikes = models.IntegerField(default=0)
    numberofcomments = models.IntegerField(default=0)
    numberofclicks = models.IntegerField(default=0)
    totaltimespentonproduct_hours = models.IntegerField(default=0)
    userID_array_of_likes = ArrayField(base_field=models.TextField(), size=100)
    userID_array_of_dislikes = ArrayField(base_field=models.TextField(), size=100)
    userID_array_of_comments = ArrayField(base_field=models.TextField(), size=100)
    selling_price = models.FloatField(default=0.0)
    discounted_price = models.FloatField(default=0.0)
    product_categoryID = models.ForeignKey(Product_Category, on_delete=models.CASCADE)
    product_themesID = models.ForeignKey(Product_Themes, on_delete=models.CASCADE)
    discount_ID = models.ForeignKey(Discount, on_delete=models.CASCADE)
    shop_ID = models.ForeignKey(Shop, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total_sales = models.FloatField(default=0.0)
    clicks_on_product = models.IntegerField()
    created_by = models.ForeignKey(MetaUser, on_delete=models.CASCADE)
    is_product_digital = models.BooleanField(default=False)
    is_product_sharable = models.BooleanField(default=False)
    product_unique_traits = ArrayField(base_field=models.TextField(),size=15) #Why is it special?
    customer_unique_traits = ArrayField(base_field=models.TextField(), size=15) #what kind of customer do you see?
    nsfw_content = models.BooleanField(default=False)
    production_cost = models.FloatField(default=0.0) #helps us tweak our user targeting based on audience group
    production_time_days = models.IntegerField()
    hours_invested = models.FloatField(default=1.0)
    encrypt_product = models.BooleanField(default=False)
    unit_sold_expectation = models.IntegerField(default=0)
    size_chart = models.FileField(upload_to='product/size_chart')
    product_image1 = models.FileField(upload_to='product/product_image1')
    product_image2 = models.FileField(upload_to='product/product_image2', default=None)
    product_image3 = models.FileField(upload_to='product/product_image3', default=None)
    hashkey = models.TextField( default=hashkey_generator, unique=True) #generates unique SHA1 key for your product - which is immutable in TRILL universe
    created_at = models.DateField()
    modified_at = models.DateTimeField()

    def __str__(self):
        #returns Product Name & Product Meta Key

        return 'Product Name: %s -- Meta-Key: %s' % (self.name, self.hashkey)
    

#Collaboration model allows all types of users to collaborate on any asset on the TRILL ecosystem and do business
#many creators can collaborate with many products. but one product / asset at one time can have only one ownership / collab ID
class Collaboration(models.Model):
    name = models.TextField( default='Your campaign definition')
    description = models.TextField(default='Describe your campaign')
    creator_collab_choice = models.TextField(choices=[ #the bid our creator wants to do but depends on mutual consent of other party - because freedom of fucking choice
        ('FIXED-PAYMENT', 'FIXED-PAYMENT'),
        ('BARTER-DEAL', 'BARTER-DEAL'),
        ('COMMISSION-%-ON-SALES','COMMISSION-%-ON-SALES'),
        ('FREE-HELP-FROM-THE-COMMUNITY', 'FREE-HELP-FROM-THE-COMMUNITY')
    ])
    user_ID = models.ForeignKey(MetaUser, on_delete=models.CASCADE) #creators can paste their hashkey to auth
    product_ID = models.ForeignKey(Product, on_delete=models.CASCADE) #creators can paste the hashkey to add the product ID
    shop_ID = models.ForeignKey(Shop, on_delete=models.CASCADE) #add a search feature on Front-End - for People to search by Shop name
    #product_shop_ID should be EQUAL to shop_ID to verify identity that both User_IDs are same.
    creator_pitch = models.TextField()
    bid_type = models.TextField(choices=[ #the bid from the creator's side - because freedom of choice
        ('FIXED-PAYMENT', 'FIXED-PAYMENT'),
        ('BARTER-DEAL', 'BARTER-DEAL'),
        ('COMMISSION-%-ON-SALES','COMMISSION-%-ON-SALES'),
        ('FREE-HELP-FROM-THE-COMMUNITY', 'FREE-HELP-FROM-THE-COMMUNITY')
    ])
    bid_amount = models.FloatField(default=0.0)
    accept_bid = models.BooleanField(default=False) #only Product Owner has this privilege 
    created_at = models.DateField()
    modified_at = models.DateTimeField()


    def __str__(self):
        #returns collab type & collab status
        return 'User ID: %s -- Shop ID: %s' % (self.user_ID, self.shop_ID)


#Create temp table for Shopping Session - We will store this data and analyze behaviour.
class Shopping_Session(models.Model):
    user_ID = models.ForeignKey(MetaUser, on_delete=models.CASCADE)
    total_amount = models.FloatField(default=0.0)
    created_at = models.DateField()
    modified_at = models.DateTimeField()

    def __str__(self):
        #returns user_ID and total amount
        return 'User ID: %s -- Total Amount: %s' % (self.user_ID, self.total_amount)



#Create temp table called Cart Item --> We wil store the data. Analyze behaviour.
class Cart_Item(models.Model):
    session_ID = models.ForeignKey(Shopping_Session, on_delete=models.CASCADE)
    product_ID = models.ForeignKey(Product, on_delete=models.CASCADE) #We dont want our product to be deleted because of our cute temporary cart item table
    quanity = models.IntegerField(default=0)
    created_at = models.DateField()
    modified_at = models.DateTimeField()


    def __str__(self):
        # Returns Cart ID and Product ID
        return 'Cart ID: %s --- Product ID: %s' % (self.id, self.product_ID)
        #this may blast but logically it wont  because the moment we initiate this table PostGre will assign this table a id field. lets see



#Create Order Details table 
#Remember, just like message chat room shit
#Many Order_Items can have the same Order_Detail 
#A Tee and A Dildo can be order number 5566 for user name xyz - fucking modular. less risks of falling  
class Order_Detail(models.Model):
    total_amount = models.FloatField(default=0.0)
    payment_info = models.ForeignKey(User_Payment, on_delete=models.CASCADE)
    created_at = models.DateField()
    modified_at = models.DateTimeField()

    def __str__(self):
        #returns order id
        return 'Order ID: %s' % (self.id)



#Create Order Items Table - remember many order items can have the SAME ORDER DETAILS
#Here, we are accounting for each and every product purchased and bundling them.
#Because payment is done in arrays and then added up to the total amount. Duh lol
class Order_Item(models.Model):
    order_ID = models.ForeignKey(Order_Detail, on_delete=models.CASCADE)
    product_ID = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_at = models.DateField()
    modified_at = models.DateTimeField()


    def __str__(self):
        #returns Order_ID and Product ID
        return 'Order ID: %s -- Product ID: %s' % (self.order_ID, self.product_ID)



#Create models for Vendor payouts if needed
#maybe Shop_Payout Table
class Shop_Payout(models.Model):
    order_detail_ID = models.ForeignKey(Order_Detail, on_delete=models.CASCADE)
    #Add code here to payout Creator and Collaborator  


















#making every human, a creator.
#Monetizing Data --> AI + Investments + Protocol + COIN value will go up + more value
#Digitization Of Monetization 
#making human to human connection global & honest
#One Humanity, Infinite stories
#serving free-will 
#question everything  
#whoareyou?
#chaseyourself
#whatcanyoubecome?
#whatwillyoudowithit?
