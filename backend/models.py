from password_generator import PasswordGenerator
from django.contrib.postgres.fields import ArrayField
import hashlib
from django.apps import apps
from django.db import models

pg = PasswordGenerator() #initiating PG exec
pg.maxlen = 30
pg2 = PasswordGenerator()
pg2.minlen = 10


# Link to DB ER Diagram : https://excalidraw.com/#json=1o-AHOOFnaF6jYHp2Hgz1,4aF7oWBC0cdS89i-a0AN7A
#1. creating MetaUser Model

#  Our hashkey function is truly random as you can see
# Your meta-key = randomly generated alphanumeric password -> which is encrpyted in SHA1 --> Your meta key --> We cant recover it so dont ask us for help
# for some security, we need to let go of some convienience. correct, friend?


class MetaUser(models.Model):
    meta_username = models.TextField( default='username_not_defined', unique=True)
    password = models.TextField( unique=True)
    hashkey = models.TextField( default=hashlib.sha512(str(pg2.generate()).encode()).hexdigest(), unique=True)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField( default='you@you.com')
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
    payment_type = models.TextField( default='Credit / Debit Card')
    payment_provider = models.TextField( default='STRIPE')
    payment_status = models.BooleanField(default=False) #We will toggle this from the frontend via status '200' - will add protection
    total_money_out = models.FloatField(default=0.00)
    total_money_in = models.FloatField(default=0.0)
    user_payment_profile_status = models.BooleanField(default=False)

    #code for routing money to users - whether they're producing or consuming
    if user_payment_profile_status:
        #IF TRUE, we need User payment details like bank account etc etc?
        pass
    else:
        pass

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
    login_password = models.TextField( default='\xafJ@\n,\xebyc\xa4$\xd9\xcf7y\x17\\\x8d%\x8f\xac\xf8\xa3\x1e\xe8\xbc\x19I\xdc\x06\x0e\x10\xe6')
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
    human_race = models.TextField( default='Libyan')
    question_gender = models.BooleanField(default=False)
    question_god = models.BooleanField(default=False)
    question_society = models.BooleanField(default=False)
    is_life_random = models.BooleanField(default=False)
    one_humanity = models.BooleanField(default=False) #Do you beleive that humanity should be together?
    is_internet_a_happy_place = models.BooleanField(default=True)




    def __str__(self):
        #returns user_type 
        return 'You are a/an %s' % (self.user_type)


#Engineering secure chat room - can be used for 1-1 or 1-x or x-x communication - secure because read my code mofo
#all the magic will happen in the Chat Room

class Chat_Room(models.Model):
    #Chat_Room ID will be created automatically by PostGre
    name = models.TextField( default='Unnamed-Secure-Room')
    desc = models.TextField(default='Why was this room created?')
    rules = models.TextField(default='Follow the rules else create your own room')
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
class Particpants(models.Model):
    #Particpant_ID will be created automaticaly
    #one user_ID can have multiple particpantIDs
    #one room can have multiple particpants

    user_ID = models.ForeignKey(MetaUser, on_delete=models.PROTECT)
    chat_room_ID = models.ForeignKey(Chat_Room, on_delete=models.PROTECT)

    def __str__(self):
        #returns nothing

        return ('Nothing to see here.')


#what a message will look like or what traits will it have
class Message(models.Model):

    #message_ID will be automatically be generated
    chat_room_ID = models.ForeignKey(Chat_Room, on_delete=models.CASCADE)
    user_ID = models.ForeignKey(MetaUser, on_delete=models.PROTECT)
    message_body = models.TextField()
    upload_file = models.FileField(upload_to='user_meta_key/message/files')
    created_at = models.DateField()
    modified_at = models.DateTimeField()
    hashkey = models.TextField( default=hashlib.sha256(str(pg.generate()).encode()).hexdigest(), unique=True)

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
    category_image1 = models.FileField(upload_to='category/category_image1')
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
    discount_name = models.TextField()
    discount_desc = models.TextField()
    disocunt_percent = models.FloatField(default=0.0)
    active_status = models.BooleanField(default=False)
    created_by = models.ForeignKey(MetaUser, on_delete=models.CASCADE) #which user created this
    created_at = models.DateField()
    modified_at = models.DateTimeField()

    def __str__(self):
        #returns Discount code and Discount %

        return 'Code: %s -- %-Discount: %s' % (self.discount_name, self.disocunt_percent)


#Collaboration model allows all types of users to collaborate on any asset on the TRILL ecosystem and do business
#many creators can collaborate with many products. but one product / asset at one time can have only one ownership / collab ID
class Collaboration(models.Model):
    collab_name = models.TextField( default='Your campaign definition')
    collab_desc = models.TextField(default='Describe your campaign')
    collab_type = models.TextField(choices=[ #the bid our creator wants to do but depends on mutual consent of other party - because freedom of fucking choice
        ('FIXED-PAYMENT', 'FIXED-PAYMENT'),
        ('BARTER-DEAL', 'BARTER-DEAL'),
        ('COMMISSION-%-ON-SALES','COMMISSION-%-ON-SALES'),
        ('FREE-HELP-FROM-THE-COMMUNITY', 'FREE-HELP-FROM-THE-COMMUNITY')
    ])
    user_ID = models.ForeignKey(MetaUser, on_delete=models.PROTECT)
    collab_status = models.BooleanField(default=False)
    creator_pitch = models.TextField()
    bid_type = models.TextField(choices=[ #the bid from the creator's side - because freedom of choice
        ('FIXED-PAYMENT', 'FIXED-PAYMENT'),
        ('BARTER-DEAL', 'BARTER-DEAL'),
        ('COMMISSION-%-ON-SALES','COMMISSION-%-ON-SALES'),
        ('FREE-HELP-FROM-THE-COMMUNITY', 'FREE-HELP-FROM-THE-COMMUNITY')
    ])
    bid_amount = models.FloatField(default=0.0)
    accept_bid = models.BooleanField(default=False)
    created_at = models.DateField()
    modified_at = models.DateTimeField()


    def __str__(self):
        #returns collab type & collab status
        return 'Collab Type is: %s -- Collab Status: %s' % (self.collab_type, self.collab_status)


#Social Model - Key data weights on your social activity to be tracked for cluster-analysis - everything can be deleted

class Social(models.Model):
    user_ID = models.ForeignKey(MetaUser, on_delete=models.PROTECT) #we cant have user_IDs deleted - its either ways not connected to their physical copies but STILL
    following = ArrayField(base_field=models.TextField(), size=30) #lists of MetaUser_IDs of all people we follow
    followers = ArrayField(base_field=models.TextField(), size=30) #lists of MetaUSer_IDs which follow us
    profileprivate = models.BooleanField(default=False)
    saved_content = ArrayField(base_field=models.TextField(), size=500) #URLs to product_metakeys - stored as an array
    likes = ArrayField(base_field=models.TextField(), size=200) #List of Product MetaKeys liked 
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

    user_ID = models.ForeignKey(MetaUser, on_delete=models.PROTECT)
    #shop_ID will be automatically created by PostGRE - we will add a unique validator on it

    all_products = ArrayField(base_field=models.TextField(), size=200) #list of all products owned by that creator
    all_user_data = ArrayField(base_field=models.TextField(), size=100) #list of metauser IDs for your reference. no other data is shown here
    shop_name = models.TextField( default='Use your username as shop name?')
    shop_desc = models.TextField()
    shop_traits = ArrayField(base_field=models.TextField(), size=50) #define what kind of customers you want to reach
    assistance_ask = ArrayField(base_field=models.TextField(), size=20) #add tags on what help you need? funding - hiring etc
    uniquesellingprop = models.TextField(default='Why your meta-shop is special than others?')





# Creating Product model - how does a product look like? what are the traits?

class Product(models.Model):
    name=models.TextField( default='No Product Name, yet', unique=True)
    desc = models.TextField(default='Explain your creation in great poetic detail.')
    #ADD comments & likes
    sku = models.TextField(default='Give it a serial number ex: SNKRS-NKE-WMN-AJ12-7.5?')
    product_categoryID = models.ForeignKey(Product_Category, on_delete=models.CASCADE)
    product_themesID = models.ForeignKey(Product_Themes, on_delete=models.CASCADE)
    collaborationID = models.ForeignKey(Collaboration, on_delete=models.CASCADE)
    has_multiple_variants = models.BooleanField(default=False)

    if(has_multiple_variants):
        price_size = ArrayField(models.TextField(default='Size 0 Price 0'))
    else:
        price = models.FloatField(default=0.0)
    
    discount_ID = models.ForeignKey(Discount, on_delete=models.CASCADE)
    shop_ID = models.ForeignKey(Shop, on_delete=models.CASCADE)
    total_sales = models.FloatField(default=0.0)
    clicks_on_product = models.IntegerField(1)
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

    if encrypt_product == False:
        product_active = models.BooleanField(default=True)
        product_hidden = models.BooleanField(default=False)

    else:
        product_active = models.BooleanField(default=False)
        product_hidden= models.BooleanField(default=True)

    unit_sold_expectation = models.IntegerField(default=0)
    size_chart = models.FileField(upload_to='product/size_chart')
    product_image1 = models.FileField(upload_to='product/product_image1')
    product_image2 = models.FileField(upload_to='product/product_image2')
    product_image3 = models.FileField(upload_to='product/product_image3')
    hashkey = models.TextField( default=hashlib.sha1(str(pg.generate()).encode()).hexdigest(), unique=True) #generates unique SHA1 key for your product - which is immutable in TRILL universe
    created_at = models.DateField()
    modified_at = models.DateTimeField()

    def __str__(self):
        #returns Product Name & Product Meta Key

        return 'Product Name: %s -- Meta-Key: %s' % (self.name, self.hashkey)
    




















