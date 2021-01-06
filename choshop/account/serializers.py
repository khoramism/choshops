from rest_framework import serializers
from .models import Account, Shopper, Buyer




class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id', 
            'name',
            'email',
            'password',
        )
        extra_kwargs = {
            'email': {'write_only':True},
            'password': {'write_only':True},
        }






class ShopperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shopper






class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer



