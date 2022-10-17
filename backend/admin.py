from django.contrib import admin

from .models import *



#User Type Models
admin.site.register(MetaUser)
admin.site.register(MetaUserAccountStatus)
admin.site.register(Product)
admin.site.register(Shop)
admin.site.register(stripeAccountInfo)
admin.site.register(stripeAccountBalance)
admin.site.register(stripeCharges)







# Register your models here.
