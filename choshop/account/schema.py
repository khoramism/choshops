from graphene_django import DjangoObjectType
import graphene 
from .models import Buyer, Shopper, Account 
from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Q, F

class BuyerType(DjangoObjectType):
    class Meta:
        model = Buyer 
        exclude = ('account__password',)


class ShopperType(DjangoObjectType):
    class Meta:
        model = Shopper
        exclude = ('account__password',)


class Query(graphene.ObjectType):
    #framework = graphene.List(FrameWorkType)
    buyer = graphene.List(BuyerType)
    shopper = graphene.List(ShopperType)

    shopper_search = graphene.Field(ShopperType, q=graphene.String())
    buyer_search = graphene.Field(BuyerType, q=graphene.String())

    def resolve_all_buyers(root, info):
        return Buyer.objects.all()

    def resolve_all_shoopers(root, info):
        return Shopper.objects.all()

    def resolve_buyer(root,info):
        if info.context.user.is_authenticated:
        
            return get_object_or_404(Buyer, account=info.context.user)

        else: 
            return f'{info.context.user} is not Authenticated Sir!'


    def resolve_shopper(root,info):
        if info.context.user.is_authenticated:
        
            return get_object_or_404(Shopper, account=info.context.user)

        else: 
            return f'{info.context.user} is not Authenticated Sir!'


    def resolve_buyer_search(info,context, q):
        #  self.statics = StaticPlaceholder.objects.filter(
             #   Q(draft__in=placeholder_ids) | Q(public__in=placeholder_ids)
        return Buyer.objects.filter(
            Q(account__username=q) | Q(account_bio=q) | Q(account_email=q)
        )

        