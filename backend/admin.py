from django.contrib import admin
from .models import Chat_Room, Collaboration, Discount, Message, MetaUser, Particpant, Product, Product_Category, Product_Themes,  Shop, Social, User_Address, User_Payment, User_Type



admin.site.register(MetaUser)
admin.site.register(User_Address)
admin.site.register(User_Payment)
admin.site.register(User_Type)
admin.site.register(Chat_Room)
admin.site.register(Particpant)
admin.site.register(Message)
admin.site.register(Product_Category)
admin.site.register(Product_Themes)
admin.site.register(Discount)
admin.site.register(Collaboration)
admin.site.register(Social)
admin.site.register(Shop)
admin.site.register(Product)

# Register your models here.
