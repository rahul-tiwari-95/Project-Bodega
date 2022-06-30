from django import forms
from django.forms.models import inlineformset_factory
from .models import MetaUser, UserAddress


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = (
            'address_line1',
            'city'
        )
        

UserAddressFormSet = inlineformset_factory(
    MetaUser,
    UserAddress,
    form=UserAddressForm,
    min_num=2,
    extra=1,
    can_delete=False
)