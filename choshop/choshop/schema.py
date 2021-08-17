import graphene

import graphql_jwt

import account.schema as account_schema 
import cart.schema as cart_schema 
import shop.schema as shop_schema 
import orders.schema orders_schema 
import blog.schema as blog_schema 

class Query(cart_schema.Query,account_schema.Query, shop_schema.Query, blog_schema.Query , orders_schema.Query, graphene.ObjectType):
	pass

class Mutation(language_schema.Mutation,graphene.ObjectType ):
	token_auth = graphql_jwt.ObtainJSONWebToken.Field()
	verify_token = graphql_jwt.Verify.Field()
	refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query = Query, mutation=Mutation)

