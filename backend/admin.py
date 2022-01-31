from django.contrib import admin
from .models import Chat_Room, Collaboration, Discount, Message, MetaUser, Particpants, Product, Product_Category, Product_Themes, Shop, Social, User_Address, User_Payment, User_Type
from import_export import resources
from backend.models import MetaUser

admin.site.register(MetaUser)
admin.site.register(User_Address)
admin.site.register(User_Payment)
admin.site.register(User_Type)
admin.site.register(Chat_Room)
admin.site.register(Particpants)
admin.site.register(Message)
admin.site.register(Product_Category)
admin.site.register(Product_Themes)
admin.site.register(Discount)
admin.site.register(Collaboration)
admin.site.register(Social)
admin.site.register(Shop)
admin.site.register(Product)

class UserResources(resources.ModelResource):

    class Meta:
        model = MetaUser


# Register your models here.
