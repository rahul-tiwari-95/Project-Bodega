from django.contrib import admin

from .models import BLAScore, BodegaCognitiveInventory, BodegaCognitiveItem, BodegaCognitivePerson, BodegaDept, BodegaFace, BodegaPersonalizer, BodegaVision, CartItem, ChatRoom, Collaboration, Discount, Level, Message, MetaUser, OrderDetail, OrderItem, Participant, Product, ProductCategory, BoostTags, ProductMetaData, SentinoInventory, SentinoItemClassification, SentinoItemProjection, SentinoItemProximity, SentinoProfile, SentinoSelfDescription,  Shop, ShopPayout, ShoppingSession, Social, Solomonv0, SysOpsAgent, SysOpsAgentRepo, SysOpsDemandNode, SysOpsProject, SysOpsSupplyNode, UserAddress, UserPayment, UserType, SentinoSelfDescription



#User Type Models
admin.site.register(MetaUser)

#User Metadata
admin.site.register(UserAddress)
admin.site.register(UserPayment)
admin.site.register(UserType)

#Message Model
admin.site.register(ChatRoom)
admin.site.register(Participant)
admin.site.register(Message)

#Products Assets
admin.site.register(ProductCategory)
admin.site.register(BoostTags)
admin.site.register(Discount)
admin.site.register(Collaboration)
admin.site.register(Social)
admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(ProductMetaData)
admin.site.register(ProductOwnershipLedger)


#Cart & Checkout Tables - No need to be filled 
admin.site.register(ShoppingSession)
admin.site.register(CartItem)
admin.site.register(OrderDetail)
admin.site.register(OrderItem)
admin.site.register(ShopPayout)

#Level Score
admin.site.register(Level)
admin.site.register(BLAScore)

#Sentino Profile AI
admin.site.register(SentinoItemProximity)
admin.site.register(SentinoItemProjection)
admin.site.register(SentinoInventory)
admin.site.register(SentinoSelfDescription)
admin.site.register(SentinoProfile)
admin.site.register(SentinoItemClassification)

#Bodega Vision Models
admin.site.register(BodegaVision)
admin.site.register(BodegaFace)
admin.site.register(BodegaPersonalizer)
admin.site.register(BodegaCognitiveItem)
admin.site.register(BodegaCognitiveInventory)
admin.site.register(BodegaCognitivePerson)
admin.site.register(BodegaDept)
admin.site.register(Solomonv0)

#SysOps Agent Models
admin.site.register(SysOpsAgent)
admin.site.register(SysOpsAgentRepo)
admin.site.register(SysOpsProject)
admin.site.register(SysOpsSupplyNode)
admin.site.register(SysOpsDemandNode)






# Register your models here.
