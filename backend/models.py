from password_generator import PasswordGenerator
from django.contrib.postgres.fields import ArrayField
import hashlib
from django.apps import apps
from django.db.models import JSONField
from django.db import models
from django.utils import timezone
import datetime


# 95% efficiency
# 99% particpation - HUNTER X


# Bodega Encryption Algorithm
# PasswordGenerator() has been modified
# Different hashkey types for different uses
# Play ground where users can put in shit and see output

pg = PasswordGenerator()  # initiating PG exec


def private_metauser_hashkey_generator():
    return hashlib.sha3_256(str(pg.non_duplicate_password(40)).encode()).hexdigest()
    # PRIVATE KEY
    # Use PRIVATE KEY to AUTH MetaUser - Use Private Key whenever we want to verify that we are talking to the right user
    # On Website - Users can set a password or a code to view their hashkeys
    # To delete a product, you need PRIVATE KEY for AUTH
    # Use PRIVATE KEY when MetaUser initiates Delete response


def public_metauser_hashkey_generator():
    return hashlib.md5(str(pg.non_duplicate_password(40)).encode()).hexdigest()
    # PUBLIC KEY
    # Use Public Key to verify your identity online without worry
    # Public Key never gives admin access to any user
    # For Admin access, You need to use your PRIVATE KEY


def agent_hashkey_generator():
    return hashlib.sha3_512(str(pg.non_duplicate_password(40)).encode()).hexdigest()
    # For Internal Bodega Employees to verify auth


def project_hashkey_generator():
    return hashlib.sha3_512(str(pg.non_duplicate_password(40)).encode()).hexdigest()
    # For Internal Bodega Employees to verify auth


def product_hashkey_generator():
    return hashlib.sha3_384(str(pg.non_duplicate_password(40)).encode()).hexdigest()
    # PUBLIC KEY
    # Can be used for sharing


def chatroom_hashkey_generator():
    return hashlib.sha3_224(str(pg.non_duplicate_password(40)).encode()).hexdigest()
    # AUTO GENERATED KEY WHEN CHAT ROOM IS CREATED
    # Used to AUTH user entering the Chat Room
    # IF hashkey doesnt match - Deny entry to the room


def message_hashkey_generator():
    return hashlib.sha3_224(str(pg.non_duplicate_password(10)).encode()).hexdigest()
    # AUTO GENERATED KEY WHEN CHAT ROOM IS CREATED
    # Used to AUTH user entering the Chat Room
    # IF hashkey doesnt match - Deny entry to the room


# Solomon v0.0.1
class Solomonv0(models.Model):
    psy_traits = JSONField(null=True, blank=True)
    engagement_traits = JSONField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Solomon v0 WIP'


# Link to DB ER Diagram : https://excalidraw.com/#json=1o-AHOOFnaF6jYHp2Hgz1,4aF7oWBC0cdS89i-a0AN7A


# Creating MetaUser - ONLY AUTH USER CAN DELETE MetaUser.object
class MetaUser(models.Model):
    meta_username = models.TextField(default='username_not_defined', unique=True)
    passcode = models.TextField(unique=True)
    private_hashkey = models.TextField(default=private_metauser_hashkey_generator, unique=True)
    public_hashkey = models.TextField( default=public_metauser_hashkey_generator, unique=True)
    discord_username = models.TextField()
    created_at = models.DateField(auto_now_add=True)  
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # returns username & modified_at
        return 'username: %s -- ID: %s' % (self.meta_username, self.id)

# Creating MetaUser Tags for Profile 
class MetaUserTags(models.Model):
    metauserID = models.ForeignKey(MetaUser, on_delete=models.PROTECT)
    metauserStatus = models.CharField(default="ACTIVE GUEST CREATOR", max_length=255)
    trophiesAllocated = models.TextField(default="BABYSTEPS REVOLUTIONARY")
    projectBodegaLogo = models.ImageField(default="https://bdgdaostorage.blob.core.windows.net/media/bodegaLogoBackend.jpeg")
    metauserProfileLogo = models.ImageField(default="https://bdgdaostorage.blob.core.windows.net/media/bodegaLogoBackend.jpeg")
    subscribersNumber = models.IntegerField(default=0)
    followersNumber = models.IntegerField(default=0)
    subscriptionActive = models.BooleanField(default=False)
    accessLevelClearance = models.FloatField(default=3.5)
    isProfilePrivate = models.BooleanField(default=False)

    def __str__(self):
        return "MetaUser Tags for metauser: %s" % (self.metauserID)





# Designing Bodega's ML Models

# What Level are you on
# 5.0 scale
# everyone starts at 3.0
class Level(models.Model):
    metauserID = models.ForeignKey(MetaUser, on_delete=models.PROTECT)
    number = models.FloatField(default=3.0)

    def __str__(self):
        # returns level number and userID
        return 'MetaUserID: %s -- Level #: %s' % (self.metauserID, self.number)


# Base Line Analysis Model
class BLAScore(models.Model):
    # Solomon Model to be created later on for now  - pass
    # Possible Values: 3.0, 2.5,(Level 3+) 1.0,(Level 1) 0.0 (Level 0)
    metauserID = models.ForeignKey(MetaUser, on_delete=models.PROTECT)
    levelID = models.ForeignKey(Level, on_delete=models.PROTECT)
    ReviewCycleNo = models.FloatField(default=1.0)
    current_score = models.FloatField(default=3.0)
    predicted_score = models.FloatField(
        default=3.0)  # Incoming data from Solomon
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'BLA Score: %s -- MetaUserID: %s ' % (self.current_score, self.metauserID)



#STRIPE INTEGRATION CLASSES
class stripeAccountInfo(models.Model):
    metauserID = models.ForeignKey(MetaUser, on_delete=models.PROTECT)
    stripeAccountID = models.CharField(unique=True, max_length=400)
    businessType = models.CharField(max_length=300, default='Digital Services')
    businessName = models.CharField(blank=True, max_length=255)
    businessDescription = models.CharField(blank=True, max_length=255)
    businessCity = models.CharField(blank=True, max_length=255)
    businessCountry = models.CharField(blank=True, max_length=255)
    businessLine1 = models.CharField(blank=True, max_length=255)
    businessLine2 = models.CharField(blank=True, max_length=255)
    businessPostalCode = models.CharField(blank=True, max_length=255)
    businessEmail = models.CharField(blank=True, max_length=255)
    businessBankName = models.CharField(blank=True, max_length=255)
    businessPhone = models.CharField(blank=True, max_length=255)
    businessURL = models.CharField(blank=True, max_length=255)
    businessLogo = models.ImageField(blank=True)
    accountPaymentStatus = models.CharField(blank=True, max_length=255)
    accountTransfersStatus = models.CharField(blank=True, max_length=255)
    accountCurrency = models.CharField(blank=True, max_length=255)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)


#Instance is created whenever a new transfer Stripe API is triggered.
class stripeAccountTransfer(models.Model):
    stripeAccountInfoID = models.ForeignKey(stripeAccountInfo, on_delete=models.PROTECT)
    transactionID = models.CharField(max_length=500)
    payoutAmount = models.FloatField(default=0.0)
    payoutOrderInfo = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

#Model design to act as a ledger of our account's Stripe Balance.
class stripeAccountBalance(models.Model):
    balance = models.FloatField(default=0.0)
    currency= models.TextField()
    pendingAmount = models.FloatField(default=0.0)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)






class customerPayment(models.Model):
    metauserID = models.ForeignKey(MetaUser, on_delete=models.PROTECT)
    name = models.CharField(default='John Doe', max_length=255)
    email = models.CharField(default="johndoe@email.com", max_length=255)
    customerID = models.CharField(max_length=500)
    paymentMethodID = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


#Cash Register for Merchants
#This table will be automatically filled as the charge is created on a product by a customer.
#This ledger will show all earnings made via selling of products or via subscriptions
class CashFlowLedger(models.Model):
    stripeAccountInfoID = models.ForeignKey(stripeAccountInfo, on_delete=models.PROTECT)
    bodegaCustomerID = models.ForeignKey(customerPayment, on_delete=models.PROTECT)
    amount = models.FloatField(default=0.0)
    description = models.CharField(max_length=300, default='PRODUCT NAME')
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)



class stripeCharges(models.Model):
    bodegaCustomerID = models.ForeignKey(customerPayment, on_delete=models.PROTECT)
    stripeChargeID = models.CharField(max_length=300)
    stripeCustomerID = models.CharField(max_length=400)
    stripePaymentMethodID = models.CharField(max_length=400, default='None', blank=True)
    amount = models.FloatField(default=0.0)
    currency = models.TextField(default='us')
    description = models.CharField(max_length=400)
    capturedStatus = models.BooleanField(default=False)
    paymentStatus = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)





class creatorSubscription(models.Model):
    metauserID = models.ForeignKey(MetaUser, on_delete=models.PROTECT)
    subscriptionName = models.CharField(max_length=300)
    subscriptionDescription = models.CharField(max_length=500)
    amount = models.IntegerField(default=0)
    currency = models.CharField(max_length=255)
    chargingFrequency = models.CharField(max_length=300)
    stripeProductID = models.CharField(max_length=400)
    stripePriceID = models.CharField(max_length=400)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class Subscribers(models.Model):
    metauserID = models.ForeignKey(MetaUser, on_delete=models.PROTECT)
    customerID = models.CharField(max_length=400)
    priceID = models.CharField(max_length=400)
    subscriptionID = models.CharField(max_length=400)
    productID = models.CharField(max_length=400) 
    amount = models.IntegerField(default=0)
    invoiceID = models.CharField(max_length=400)
    status = models.CharField(max_length=400)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)





# Models for Sentino APIs - These tables act as a backup and allows us to measure all different personality profiles of the customer/user

class SentinoItemProximity(models.Model):
    # fetches data from Sentino Item Proximity API
    content_metadata = JSONField(null=True, blank=True)
    content_metadata2 = JSONField(null=True, blank=True)
    content_metadata3 = JSONField(null=True, blank=True)
    syslog_metadata = JSONField(null=True, blank=True)
    # needed so that we can send POST request to Sentino API
    self_statements = JSONField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'RESTRICTED ACCESS TO THIS DATABASE'


class SentinoItemProjection(models.Model):
    # fetches data from Sentino Item Projection API
    content_metadata = JSONField(null=True, blank=True)
    content_metadata2 = JSONField(null=True, blank=True)
    content_metadata3 = JSONField(null=True, blank=True)
    syslog_metadata = JSONField(null=True, blank=True)
    # needed so that we can send POST request to Sentino API
    self_statements = JSONField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'RESTRICTED ACCESS TO THIS DATABASE'


class SentinoItemClassification(models.Model):
    # fetches data from Sentino Item Proximity API
    content_metadata = JSONField(null=True, blank=True)
    content_metadata2 = JSONField(null=True, blank=True)
    content_metadata3 = JSONField(null=True, blank=True)
    syslog_metadata = JSONField(null=True, blank=True)
    # needed so that we can send POST request to Sentino API
    self_statements = JSONField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'RESTRICTED ACCESS TO THIS DATABASE'


class SentinoInventory(models.Model):
    # fetches data from Sentino  Inventory API
    content_metadata = JSONField(null=True, blank=True)
    content_metadata2 = JSONField(null=True, blank=True)
    content_metadata3 = JSONField(null=True, blank=True)
    syslog_metadata = JSONField(null=True, blank=True)
    # needed so that we can send POST request to Sentino API
    self_statements = JSONField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'RESTRICTED ACCESS TO THIS DATABASE'


class SentinoSelfDescription(models.Model):
    # fetches data from Sentino Self Description API
    content_metadata = JSONField(null=True, blank=True)
    content_metadata2 = JSONField(null=True, blank=True)
    content_metadata3 = JSONField(null=True, blank=True)
    syslog_metadata = JSONField(null=True, blank=True)
    # needed so that we can send POST request to Sentino API
    self_statements = JSONField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'RESTRICTED ACCESS TO THIS DATABASE'


class SentinoProfile(models.Model):
    # Fetches data from Sentino Profile API
    content_metadata = JSONField(null=True, blank=True)
    content_metadata2 = JSONField(null=True, blank=True)
    content_metadata3 = JSONField(null=True, blank=True)
    syslog_metadata = JSONField(null=True, blank=True)
    # needed so that we can send POST request to Sentino API
    self_statements = JSONField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'RESTRICTED ACCESS TO THIS DATABASE'


# Bodega Vision OCR AI Model
class BodegaVision(models.Model):
    # incoming data from Azure Vision Model Cognitive Services
    metauserID = models.ForeignKey(MetaUser, on_delete=models.CASCADE)
    image_metadata = JSONField(null=True, blank=True)
    video_metadata = JSONField(null=True, blank=True)
    content_metadata = JSONField(null=True, blank=True)
    syslog_metadata = JSONField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'MetaUserID: %s' % (self.metauserID)


# Bodega Face AI Services
class BodegaFace(models.Model):
    # incoming data from Azure Vision Face Cognitive Services
    metauserID = models.ForeignKey(MetaUser, on_delete=models.CASCADE)
    facial_metadata = JSONField(null=True, blank=True)
    syslog_metadata = JSONField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'MetaUserID: %s ' % (self.metauserID)


# Bodega Personalizer Services
class BodegaPersonalizer(models.Model):
    # incoming data from Azure Personalizer API
    metauserID = models.ForeignKey(MetaUser, on_delete=models.CASCADE)
    content_metadata = JSONField(null=True, blank=True)
    syslog_metadata = JSONField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'MetaUserID: %s ' % (self.metauserID)


# Bodega Items Cognitive Services
class BodegaCognitiveItem(models.Model):
    # incoming data from Sentino Models
    # this table will be populated by fetched the data from our Sentino Model via APIs and fill it here via POST
    metauserID = models.ForeignKey(MetaUser, on_delete=models.CASCADE)
    proximityID = models.ForeignKey(
        SentinoItemProximity, on_delete=models.CASCADE)
    classificationID = models.ForeignKey(
        SentinoItemClassification, on_delete=models.CASCADE)
    projectionID = models.ForeignKey(
        SentinoItemProjection, on_delete=models.CASCADE)
    # needed so that we can send POST request to Sentino API
    self_statements = JSONField(null=True, blank=True)
    content_metadata = JSONField(null=True, blank=True)
    syslog_metadata = JSONField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Bodega Cognitive Service Accessed'


# Bodega Inventory Cognitive Services
class BodegaCognitiveInventory(models.Model):
    # incoming data from Sentino Model
    # this table will be populated by fetched the data from our Sentino Model via APIs and fill it here via POST
    metauserID = models.ForeignKey(MetaUser, on_delete=models.CASCADE)
    inventoryID = models.ForeignKey(SentinoInventory, on_delete=models.CASCADE)
    # needed so that we can send POST request to Sentino API
    self_statements = JSONField(null=True, blank=True)
    content_metadata = JSONField(null=True, blank=True)
    syslog_metadata = JSONField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Bodega Cognitive Service Accessed'

    # Bodega Person Cognitive Services


class BodegaCognitivePerson(models.Model):
    # incoming data from Sentino Models
    # this table will be populated by fetched the data from our Sentino Model via APIs and fill it here via POST
    metauserID = models.ForeignKey(MetaUser, on_delete=models.CASCADE)
    self_descriptionID = models.ForeignKey(
        SentinoSelfDescription, on_delete=models.CASCADE)
    profileID = models.ForeignKey(SentinoProfile, on_delete=models.CASCADE)
    # needed so that we can send POST request to Sentino API
    self_statements = JSONField(null=True, blank=True)
    content_metadata = JSONField(null=True, blank=True)
    syslog_metadata = JSONField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ' Bodega Cognitive Services Accessed'


# Creating Division Class - Base default Division is 3 on a 5-point scale
class BodegaDept(models.Model):
    metauserID = models.ForeignKey(MetaUser, on_delete=models.CASCADE)
    departmentname = models.TextField(choices=[
        ('SUDO', 'SUDO'),  # Engineering Dvision
        ('SysOps', 'SysOps'),  # Operations Division
        ('FinLe', 'FinLe')  # Finance & Legal Division
    ])
    content_metadata = JSONField(null=True, blank=True)
    syslog_metadata = JSONField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # returns department name and metauserID
        return 'MetaUserID: %s -- Department: %s ' % (self.metauserID, self.departmentname)


# creating User_Address - Only accounts for Shipping Address.
class UserAddress(models.Model):
    metauserID = models.ForeignKey(MetaUser, on_delete=models.CASCADE)
    address_line1 = models.TextField()
    address_line2 = models.TextField()
    address_state = models.TextField()
    city = models.TextField()
    postal_code = models.TextField()
    country = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # returns metauserID and their address
        return 'metauserID: %s -- User_Location: %s %s' % (self.metauserID, self.city, self.country)


# creating User_payment model - 90% payments will be outsourced by Stripe.

class UserPayment(models.Model):
    metauserID = models.ForeignKey(MetaUser, on_delete=models.CASCADE)
    payment_type = models.TextField()
    stripeAccountID = models.TextField(default='Project-Bodega Member Stripe Account ID')
    total_money_out = models.FloatField(default=0.00)
    total_money_in = models.FloatField(default=0.0)
    user_payment_profile_status = models.BooleanField(default=False)

    # code for routing money to users - whether they're producing or consuming
    # we need to verify bank connection via Plaid and then use Stripe Connect

    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # returns last payment_status
        return 'Last Payment Status: %s' % (self.user_payment_profile_status)


# Creating User Type for roles.
# Types of roles:
# User, Influencer, Creator, Employee, Developer, collective


class UserType(models.Model):
    metauserID = models.ForeignKey(MetaUser, on_delete=models.CASCADE)
    bodega_vision_ID = models.ForeignKey(BodegaVision,
                                         on_delete=models.CASCADE)  # All data on what kind of content have you engaged with - Read-Write
    # Which level you on  - Read Only
    level_ID = models.ForeignKey(Level, on_delete=models.CASCADE)
    # Your personality traits - Read Write
    solomon_person_ID = models.ForeignKey(Solomonv0, on_delete=models.CASCADE)
    user_role = models.TextField(default='Creator')
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # returns user_type
        return 'Your feedback on Bodega:  %s' % (self.user_role)


# Engineering secure chat room - can be used for 1-1 or 1-x or x-x communication - secure because read my code mofo
# all the magic will happen in the Chat Room

class ChatRoom(models.Model):
    # Chat_Room ID will be created automatically by PostGre
    name = models.TextField(unique=True)
    desc = models.TextField(default='Why was this room created?')
    tags = models.TextField(default='#ROOM')
    type_of_room = models.TextField(choices=[
        # only people with meta_key can join the secure_room
        ('CLOSED-SECURE-ROOM', 'CLOSED-SECURE-ROOM'),
        # anyone can join the secure room
        ('OPEN-SECURE-ROOM', 'OPEN-SECURE-ROOM'),
        # leads ro the deletion of the room
        ('INITIATE-ROOM-TERMINATION', 'INITIATE-ROOM-TERMINATION')
    ])
    isRoomPrivate = models.BooleanField(default=True)
    room_hashkey = models.TextField(
        default=chatroom_hashkey_generator, unique=True)
    modified_on =models.DateTimeField(auto_now_add=True)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        # returns room name and room status

        return 'ROOM-NAME: %s -- ROOM-STATUS: %s' % (self.name, self.is_room_active)


# Who all with particpate in which rooms? - See secuirty can be fucking easy
class Participant(models.Model):
    # Particpant_ID will be created automaticaly
    # one metauserID can have multiple particpantIDs
    # one room can have multiple particpants - multiple users can have multiple participantID but same chat_room_ID for group chat

    metauserID = models.ForeignKey(MetaUser, on_delete=models.CASCADE)
    chat_room_ID = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

    def __str__(self):
        # returns nothing

        return 'metauserID: %s -- Chat_Room_ID: %s' % (self.metauserID, self.chat_room_ID)


# what a message will look like or what traits will it have
class Message(models.Model):
    # message_ID will be automatically be generated
    chat_room_ID = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    metauserID = models.ForeignKey(MetaUser, on_delete=models.CASCADE)
    message_body = models.TextField()
    upload_file = models.FileField(
        upload_to='user_meta_key/message/files', default=None)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)
    hashkey = models.TextField(default=message_hashkey_generator, unique=True)

    def __str__(self):
        # returns chat_room_ID
        return 'Chat Room ID: %s ' % (self.chat_room_ID)


# Product Category Definition - How are the products/assets categorized / segmented?
class ProductCategory(models.Model):
    category_name = models.TextField(choices=[
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
        ('POTRAIT-VIDEO-FILE', 'POTRAIT-VIDEO-FILE'),
    ])
    category_desc = models.TextField(default='Describe your creation.')
    created_at = models.DateField(auto_now_add=True)  # when was it created
    modified_at =models.DateTimeField(auto_now_add=True)  # when was it last modfied
    category_image1 = models.FileField(
        upload_to='category/category_image1')  # set default to Bodega's image
    category_image2 = models.FileField(upload_to='category/category_image2')
    category_image3 = models.FileField(upload_to='category/category_image3')

    def __str__(self):
        # returns Product Category

        return 'Product Category Name: %s ' % (self.category_name)


#BoostTags Model Instance
class BoostTags(models.Model):
    
    tags = models.CharField(max_length=11) #Name of BoostTags
    created_by = models.ForeignKey(MetaUser, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # returns collection name

        return 'BoostTags Name: %s' % (self.tags)


# Product Discount definition - How much discount?
class Discount(models.Model):
    name = models.TextField()
    description = models.TextField()
    discount_percent = models.FloatField(default=0.0)
    active_status = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        MetaUser, on_delete=models.CASCADE)  # which user created this
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # returns Discount code and Discount %

        return 'Code: %s' % (self.name)


# creating base template for Bodega coins
# in the beginning, bodega coins will be simply points you get on purchase
class Bodegacoins(models.Model):
    quantity = models.FloatField(default=300)


# Social Model - Key data weights on your social activity to be tracked for cluster-analysis - everything can be deleted

class Social(models.Model):
    metauserID = models.ForeignKey(MetaUser,
                                   on_delete=models.CASCADE)  # we cant have metauserIDs deleted - its either ways not connected to their physical copies but STILL
    # bodegacoins_ID = models.ForeignKey(Bodegacoins, on_delete=models.CASCADE)
    # lists of MetametauserIDs of all people we follow
    following = JSONField(null=True, blank=True)
    # lists of MetametauserIDs which follow us
    followers = JSONField(null=True, blank=True)
    makeprofileprivate = models.BooleanField(default=False)
    # URLs to product_metakeys - stored as an array
    saved_content = JSONField(null=True, blank=True)
    # List of Product Hashkeys liked by user
    likes = JSONField(null=True, blank=True)
    # List and count of Product Hashkeys disliked by user
    dislikes = JSONField(null=True, blank=True)
    # List of Product MetaKeys commented on
    comments = JSONField(null=True, blank=True)
    products_clickedOn = JSONField(null=True, blank=True)
    bio = models.TextField()
    blocked_list = JSONField(null=True, blank=True)
    # Ask for permissions for data collection
    data_mining_status = models.BooleanField(default=False)
    # ONLY SELECT USERS whose SOCIAL.data_mining_status == True - Simple solution to privacy, consent! consent! consent!
    account_active = models.BooleanField(default=True)
    delete_metauser = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True)
    modified_on =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # returns metauserID annd account_status
        return 'metauserID: %s -- Account On Status: %s' % (self.metauserID, self.account_active)

class MetaUserSocial(models.Model):
    metauserID = models.ForeignKey(MetaUser, on_delete=models.PROTECT)
    followers = ArrayField(
                            ArrayField(
                                        models.CharField(blank=True, max_length=255)
                            ),
    )
    



class bodegaSocial(models.Model):
    metauserID = models.ForeignKey(MetaUser, on_delete=models.PROTECT)
    followers = ArrayField(
                            ArrayField(
                                        models.CharField(blank=True, max_length=255)
                            ),
    )
    following = ArrayField(
                            ArrayField(
                                        models.CharField(blank=True, max_length=255)
                            ),
    )
    likes = ArrayField(
                            ArrayField(
                                        models.CharField(blank=True, max_length=255)
                            ),
    )
    comments = ArrayField(
                            ArrayField(
                                        models.CharField(blank=True, max_length=255)
                            ),
    )
    productsClickedOn = ArrayField(
                            ArrayField(
                                        models.CharField(blank=True, max_length=255)
                            ),
    )
    unfollows= ArrayField(
                            ArrayField(
                                        models.CharField(blank=True, max_length=255)
                            ),
    )
    created_on = models.DateField(auto_now_add=True)
    modified_on =models.DateTimeField(auto_now_add=True)


# Commerce Model - key data weights on your commerce activity to be tracked for cluster analysis

class Shop(models.Model):
    metauserID = models.ForeignKey(MetaUser,on_delete=models.CASCADE)  # Owner details - we will show metauserID.meta_username
    all_products = JSONField(null=True, blank=True)
    all_user_data = JSONField(null=True,blank=True)  # list of metauser IDs for your reference. no other data is shown here
    name = models.TextField()
    description = models.TextField()
    logo = models.FileField(upload_to='shop-details/profile_picture')
    cover_image = models.FileField(
        upload_to='shop-details/profile_cover_image', default='EMPTY')
    # Ask user if their Shop address is same as their own address for fucks sake.
    address_line1 = models.TextField()
    address_line2 = models.TextField()
    address_state = models.TextField()
    city = models.TextField()
    state = models.TextField(default='NY')
    postal_code = models.TextField()
    country = models.TextField(choices=[
        ('INDIA', 'IN'),
        ('USA', 'US'),
    ])  # Before deployment -> use this link for data: https://github.com/hampusborgos/country-flags/blob/main/countries.json
    bodega_vision_tags = JSONField(null=True,
                                   blank=True)  # loaded data from Azure Vision API - All tags stored here - Solomon_vision
    bodega_customer_tags = JSONField(
        null=True, blank=True)  # load tags on customers
    uniquesellingprop = models.TextField(
        default='Why your meta-shop is special than others?')
    data_mining_status = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True)
    modified_on =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # returns Shop nane and metauserID
        return 'Shop name is: %s -- User ID is: %s' % (self.name, self.metauserID)


#Creator Merchant Model



class Product(models.Model):
    metauserID = models.ForeignKey(MetaUser, on_delete=models.CASCADE)
    product_categoryID = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    boostTagsID = models.ForeignKey(BoostTags, on_delete=models.CASCADE)
    discount_ID = models.ForeignKey(Discount, on_delete=models.CASCADE)
    shop_ID = models.ForeignKey(Shop, on_delete=models.CASCADE)
    productName = models.TextField(max_length=140, unique=True)
    producDescription = models.CharField(max_length=300)
    sellingPrice = models.FloatField(default=0.0)
    discounted_price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)
    subscriptionProduct = models.BooleanField(default=False)
    privateProduct = models.BooleanField(default=False)
    isPhysicalProduct = models.BooleanField(default=False)
    size_chart = models.FileField(upload_to='product/size_chart', default='https://projectbodegadb.blob.core.windows.net/media/8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg')
    product_image1 = models.FileField(upload_to='product/product_image1', default='https://projectbodegadb.blob.core.windows.net/media/8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg')
    product_image2 = models.FileField(upload_to='product/product_image2', default='https://projectbodegadb.blob.core.windows.net/media/8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg')
    product_image3 = models.FileField( upload_to='product/product_image3', default='https://projectbodegadb.blob.core.windows.net/media/8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg')
    product_image4 = models.FileField(upload_to='product/product_image4', default='https://projectbodegadb.blob.core.windows.net/media/8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg')
    productHashkey = models.TextField(default=product_hashkey_generator, unique=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # returns Product Name & Product Meta Key

        return 'Product Name: %s -- Meta-Key: %s' % (self.productName, self.productHashkey)


# Creating ProductMetaData model - how does a product look like? what are the traits?

class ProductMetaData(models.Model):
    productID = models.ForeignKey(Product, on_delete=models.PROTECT)
    numberoflikes = models.IntegerField(default=0)
    numberofdislikes = models.IntegerField(default=0)
    numberofcomments = models.IntegerField(default=0)
    numberofclicks = models.IntegerField(default=0)
    totaltimespentonproduct_hours = models.IntegerField(default=0)
    metauserID_of_likes = JSONField(null=True, blank=True)
    metauserID_of_dislikes = JSONField(null=True, blank=True)
    metauserID_of_comments = JSONField(null=True, blank=True)
    total_sales = models.FloatField(default=0.0)
    clicks_on_product = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # returns Product Name & Product Meta Key

        return 'Product Meta Data '


class MunchiesPage(models.Model):
    munchiesPageName = models.CharField(max_length=255)
    munchiesCoverImage = models.FileField(upload_to = 'munchies/coverImage')
    munchiesPageViews = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Munchies Page Name: %s -- Total Views: %s' %(self.munchiesPageName, self.munchiesPageViews)



#Creating Munchies Tabel
class MunchiesVideo(models.Model):
    munchiesPageID = models.ForeignKey(MunchiesPage, on_delete=models.PROTECT)
    munchiesVideo = models.FileField(upload_to='munchies/videos')
    munchiesCaption = models.CharField(max_length=200)
    munchiesVideoTags = models.CharField(max_length=200)
    munchiesDislikes = models.IntegerField(default=0)
    munchiesVideoViews = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Munchies Video: %s -- Total Views: %s' %(self.munchiesVideo, self.munchiesVideoViews)





# Collaboration model allows all types of users to collaborate on any asset on the TRILL ecosystem and do business
# many creators can collaborate with many products. but one product / asset at one time can have only one ownership / collab ID
class Collaboration(models.Model):
    name = models.TextField(default='Your campaign definition')
    description = models.TextField(default='Describe your campaign')
    creator_collab_choice = models.TextField(choices=[
        # the bid our creator wants to do but depends on mutual consent of other party - because freedom of fucking choice
        ('FIXED-PAYMENT', 'FIXED-PAYMENT'),
        ('COMMISSION-%-ON-SALES', 'COMMISSION-%-ON-SALES'),
        ('FREE-HELP-FROM-THE-COMMUNITY', 'FREE-HELP-FROM-THE-COMMUNITY')
    ])
    metauserID = models.ForeignKey(MetaUser, on_delete=models.CASCADE)

    product_ID = models.ForeignKey(Product,on_delete=models.CASCADE)  # creators can paste the hashkey to add the product ID
    shop_ID = models.ForeignKey(Shop,on_delete=models.CASCADE)  # add a search feature on Front-End - for People to search by Shop name
    # product_shop_ID should be EQUAL to shop_ID to verify identity that both metauserIDs are same.
    creator_pitch = models.TextField()
    bid_type = models.TextField(choices=[  # the bid from the creator's side - because freedom of choice
        ('FIXED-PAYMENT', 'FIXED-PAYMENT'),
        ('COMMISSION-%-ON-SALES', 'COMMISSION-%-ON-SALES'),
        ('FREE-HELP-FROM-THE-COMMUNITY', 'FREE-HELP-FROM-THE-COMMUNITY')
    ])
    bid_amount = models.FloatField(default=0.0)
    # only Product Owner has this privilege
    accept_bid = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # returns collab type & collab status
        return 'User ID: %s -- Shop ID: %s' % (self.metauserID, self.shop_ID)


class yerrrCollaboration(models.Model):
    collaboratorMetaUserID = models.ForeignKey(MetaUser, on_delete=models.PROTECT)
    ownerMetaUserID = models.IntegerField(default=0)
    productID = models.ForeignKey(Product, on_delete=models.PROTECT)
    campaignName = models.CharField(max_length=255, default='Your Campaign Name')
    campaignDescription = models.CharField(max_length=600, default='Why you want to collaborate on this product?')
    media1 = models.FileField(upload_to='yerrr/media1', default='https://projectbodegadb.blob.core.windows.net/media/8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg')
    caption1 = models.CharField(max_length=255, default='Caption for Media 1')
    media2 = models.FileField(upload_to='yerrr/media2', default='https://projectbodegadb.blob.core.windows.net/media/8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg')
    caption2 = models.CharField(max_length=255, default='Caption for Media 2')
    media3 = models.FileField(upload_to='yerrr/media3', default='https://projectbodegadb.blob.core.windows.net/media/8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg')
    caption3 = models.CharField(max_length=255, default='Caption for Media 3')
    collaborationType = models.TextField(choices=[ 
        ('FIXED-ONE-TIME-PAYMENT', 'FIXED-ONE-TIME-PAYMENT'),
        ('COMMISSION-%-ON-SALES', 'COMMISSION-%-ON-SALES'),
        ('FREE-HELP-FROM-THE-COMMUNITY', 'FREE-HELP-FROM-THE-COMMUNITY')
    ])
    campaignRules = models.CharField(max_length=255, default='Product Owner can list rules for the campaign.')
    collaboratorFixedPaymentAmount = models.IntegerField(default=0)
    collaboratorCommissionPercentageAmount = models.IntegerField(default=0)
    yerrrStatus = models.BooleanField(default=False)
    ownerAcceptBid = models.BooleanField(default=False)
    collaboratorAcceptBid = models.BooleanField(default=False)
    #Either the owner or the collaborator goes False on the bid then yerrrStatus goes False as well.
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)



# Create temp table for Shopping Session - We will store this data and analyze behaviour.
class ShoppingSession(models.Model):
    metauserID = models.ForeignKey(MetaUser, on_delete=models.CASCADE)
    total_amount = models.FloatField(default=0.0)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # returns metauserID and total amount
        return 'User ID: %s -- Total Amount: %s' % (self.metauserID, self.total_amount)


# Create temp table called Cart Item --> We wil store the data. Analyze behaviour.
class CartItem(models.Model):
    session_ID = models.ForeignKey(ShoppingSession, on_delete=models.CASCADE)
    product_ID = models.ForeignKey(Product,
                                   on_delete=models.CASCADE)  # We dont want our product to be deleted because of our cute temporary cart item table
    quantity = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Returns Cart ID and Product ID
        return 'Cart ID: %s --- Product ID: %s' % (self.id, self.product_ID)
        # this may blast but logically it wont  because the moment we initiate this table PostGre will assign this table a id field. lets see


# Create temp table called Cart Item --> We wil store the data. Analyze behaviour.
class ShoppingCartItem(models.Model):
    metauserID = models.ForeignKey(MetaUser, on_delete=models.CASCADE)
    product_ID = models.ForeignKey(Product, on_delete=models.CASCADE)  # We dont want our product to be deleted because of our cute temporary cart item table
    quantity = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Returns Cart ID and Product ID
        return 'Cart ID: %s --- Product ID: %s' % (self.id, self.product_ID)
        # this may blast but logically it wont  because the moment we initiate this table PostGre will assign this table a id field. lets see



# Create Order Details table
# Remember, just like message chat room shit
# Many Order_Items can have the same Order_Detail
# A Tee and A Dildo can be order number 5566 for user name xyz - fucking modular. less risks of falling
class OrderDetail(models.Model):
    total_amount = models.FloatField(default=0.0)
    payment_info = models.ForeignKey(UserPayment, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # returns order id
        return 'Order ID: %s' % (self.id)


# Create Order Items Table - remember many order items can have the SAME ORDER DETAILS
# Here, we are accounting for each and every product purchased and bundling them.
# Because payment is done in arrays and then added up to the total amount. Duh lol
class OrderItem(models.Model):
    order_ID = models.ForeignKey(OrderDetail, on_delete=models.PROTECT)
    product_ID = models.ForeignKey(Product, on_delete=models.PROTECT)
    metauserID = models.ForeignKey(MetaUser, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # returns Order_ID and Product ID
        return 'Order ID: %s -- Product ID: %s' % (self.order_ID, self.product_ID)

#Order Success table model

class OrderSuccess(models.Model):
    order_ID = models.ForeignKey(OrderDetail, on_delete=models.PROTECT)
    metauserID = models.ForeignKey(MetaUser, on_delete=models.PROTECT)
    stripeChargeID = models.TextField(blank=True)
    orderCompleted = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #Returns stripeChargeID and OrderID

        return 'Stripe Charge ID: %s --  Order ID: %s' % (self.stripeChargeID, self.order_ID)


#Order Failure Table Model

class OrderFailure(models.Model):
    order_ID = models.ForeignKey(OrderDetail, on_delete=models.PROTECT)
    metauserID = models.ForeignKey(MetaUser, on_delete=models.PROTECT)
    stripeChargeID = models.TextField(blank=True)
    orderCompleted = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Stripe Charge ID: %s -- Order ID: %s' % (self.stripeChargeID, self.order_ID)

# Create models for Vendor payouts if needed
# maybe Shop_Payout Table
class ShopPayout(models.Model):
    order_detail_ID = models.ForeignKey(OrderDetail, on_delete=models.CASCADE)
    # Add code here to payout Creator and Collaborator


# END OF FRONTEND-MODELS FOR USER


# Creating Bodega Employee CRM Models

# Creating SysOps Agent & Repository Models - PROTECT - Can never be deleted
class SysOpsAgent(models.Model):
    metauserID = models.ForeignKey(MetaUser, on_delete=models.PROTECT)
    levelID = models.ForeignKey(Level, on_delete=models.PROTECT)
    departmentID = models.ForeignKey(BodegaDept, on_delete=models.PROTECT)
    agent_hashkey = models.TextField(
        default=agent_hashkey_generator, unique=True)
    bio = models.TextField(default='I am Bodega')
    reporting_officer = models.TextField(
        default="PASTE PUBLIC METAUSER HASHKEY")
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Returns SysOps-Hashkey
        return 'SysOps Agent MetaUserID: %s ' % (self.metauserID)


# Creating SysOps Agent Repository Model - Normalize this for many to one relationships
# One SysOp Agent can have multiple repositories

class SysOpsAgentRepo(models.Model):
    # SysOps Agent Repo Design Structure
    metauserID = models.ForeignKey(MetaUser, on_delete=models.PROTECT)
    sysops_agentID = models.ForeignKey(SysOpsAgent, on_delete=models.PROTECT)
    project_hashkey = JSONField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # returns sysops_agentID
        return 'SysOps Agent ID: %s ' % (self.sysops_agentID)


# Creating SysOps Project Model
# Represents a independent problem statement

class SysOpsProject(models.Model):
    # SysOps Project Design
    owner_metauserID = models.ForeignKey(MetaUser, on_delete=models.PROTECT)
    owner_agentID = models.ForeignKey(SysOpsAgent, on_delete=models.PROTECT)
    levelID = models.ForeignKey(Level, on_delete=models.PROTECT)
    divisionID = models.ForeignKey(BodegaDept, on_delete=models.PROTECT)
    name = models.TextField(default='Project Name')
    problem_statement = models.CharField(
        default='140 Characters', max_length=300)
    problem_impact_size = models.CharField(
        default='140 Characters', max_length=300)
    hypothesis = models.TextField()
    key_performance_indicators = models.TextField()
    status = models.TextField(choices=[
        ('SUCCESS', 'SUCCESS'),
        ('WIP', 'WIP'),
        ('FAILED', 'FAILED')
    ])
    ttc_hours = models.FloatField(default=1.0)
    allocated_ttc_hours = models.FloatField(default=5.0)
    tasks = JSONField(null=True, blank=True)
    team_hashkey_json = JSONField(null=True, blank=True)
    hashkey = models.TextField(default=project_hashkey_generator, unique=True)
    genesis_project_hashkey = JSONField(null=True, blank=True)
    parent_project_hashkey = JSONField(null=True, blank=True)
    child_project_hashkey = JSONField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Return Project Hashkey
        return 'Project Hashkey : %s ' % (self.hashkey)


# Supply, Demand
# SysOps SupplyNode Model

class SysOpsSupplyNode(models.Model):
    # table for all creators who CREATE SHIT
    supply_metauserID = models.ForeignKey(MetaUser, on_delete=models.PROTECT)
    supply_shopID = models.ForeignKey(Shop, on_delete=models.PROTECT)
    bla_ScoreID = models.ForeignKey(BLAScore, on_delete=models.PROTECT)
    opsec_agent_hashkey = models.TextField(default='AGENT HASHKEY')
    name = models.TextField(default='JOHN')
    location = models.TextField(default='New York BABY')
    status = models.BooleanField(default=True)
    tokens_allocated = models.FloatField(default=1.0)
    # what the creator thinks of us? the team & Bodega
    creator_hypothesis = models.TextField(default='CREATORS PERSPECTIVE')
    # what we think of his primary drives? - how will he pull his weight?
    sysops_agent_hypothesis = models.TextField(
        default='SysOp Agent PERSPECTIVE')
    creator_identity_status = models.BooleanField(default=False)
    all_digital_url = JSONField(null=True, blank=True)
    influence_size = JSONField(null=True, blank=True)
    # what market is this? #fashion #anime
    genre = JSONField(null=True, blank=True)
    # What sub niche is this? #streetwear #female
    category_vertical = JSONField(null=True, blank=True)
    # What sub niche is this? #eaarings #bucket_hats
    category_vertical2 = JSONField(null=True, blank=True)
    # what do you feel about their creation?
    product_traits = JSONField(null=True, blank=True)

    creator_traits = JSONField(null=True,
                               blank=True)  # what do we think about the creator? - #trustworthy? #reliability

    # Digital? #On-Demand-Production #Wholesale #Abstract?
    production_type = JSONField(null=True, blank=True)
    current_revenue = JSONField(null=True, blank=True)
    current_aov = JSONField(null=True, blank=True)
    predicted_revenue = JSONField(null=True, blank=True)
    creator_audience_traits = JSONField(null=True, blank=True)
    # How can we fulfill their needs by collab with folks who work at Bodega? whats stopping them from reaching their maximu potential?
    sysops_solution_hypothesis = JSONField(null=True, blank=True)
    additional_notes = JSONField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'SupplyNode ShopID: %s ' % (self.supply_shopID)


# SysOps DemandNode Model

class SysOpsDemandNode(models.Model):
    # table for all creators who CAN SELL SHIT
    demand_metauserID = models.ForeignKey(MetaUser, on_delete=models.PROTECT)
    opsec_agent_hashkey = models.TextField(default='AGENT HASHKEY')
    name = models.TextField(default='JOHN')
    location = models.TextField(default='New York BABY')
    status = models.BooleanField(default=True)
    tokens_allocated = models.FloatField(default=1.0)
    # what the creator thinks of us? the team & Bodega
    creator_hypothesis = models.TextField(default='CREATORS PERSPECTIVE')
    # what we think of his primary drives? - how will he pull his weight?
    sysops_agent_hypothesis = models.TextField(
        default='SysOp Agent PERSPECTIVE')
    creator_identity_status = models.BooleanField(default=False)
    all_digital_url = JSONField(null=True, blank=True)
    influence_size = JSONField(null=True, blank=True)
    # what market is this? #fashion #anime
    genre = JSONField(null=True, blank=True)
    # What sub niche is this? #streetwear #female
    category_vertical = JSONField(null=True, blank=True)
    # What sub niche is this? #eaarings #bucket_hats
    category_vertical2 = JSONField(null=True, blank=True)
    # what do you feel about their creation?
    product_traits = JSONField(null=True, blank=True)

    creator_traits = JSONField(null=True,
                               blank=True)  # what do we think about the creator? - #trustworthy? #reliability

    # Digital? #On-Demand-Production #Wholesale #Abstract?
    production_type = JSONField(null=True, blank=True)
    current_revenue = JSONField(null=True, blank=True)
    predicted_revenue = JSONField(null=True, blank=True)
    creator_audience_traits = JSONField(null=True, blank=True)
    # How can we fulfill their needs by collab with folks who work at Bodega? whats stopping them from reaching their maximu potential?
    sysops_solution_hypothesis = JSONField(null=True, blank=True)
    additional_notes = JSONField(null=True, blank=True)
    bla_ScoreID = models.ForeignKey(BLAScore, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'DemandNode MetaUserID: %s ' % (self.demand_metauserID)

# making every human, a creator.
# monetizing data --> AI + Investments + Protocol + COIN value will go up + more value
# digitization Of monetization
# making human to human connection global & honest
# one humanity, infinite stories
# serving free-will?
# question everything?
# whoareyou?
# chaseyourself
# whatcanyoubecome?
# whatwillyoudowithit?





#Replacement for SHOP MODEL 
#New Shop model with only imp information and auto-create

class Notifications(models.Model):
    metauserID = models.ForeignKey(MetaUser, on_delete=models.PROTECT)
    text = models.CharField(max_length=400)
    image = models.CharField(default=None, max_length=255)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Notification Text: %s ' % (self.text)

        