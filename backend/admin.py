from django.contrib import admin
from .models import MetaUser, User_Address, User_Payment, User_Type

admin.site.register(MetaUser)
admin.site.register(User_Address)
admin.site.register(User_Payment)
admin.site.register(User_Type)


# Register your models here.
