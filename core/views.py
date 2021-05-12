from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Product, Category
from core.serializers.dto import CategoryDTO, ProductDTO

class CategoryList(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        return Response(CategoryDTO(categories, many=True).data)

class ProductList(APIView):
    def get(self, request, slug, format=None):
        category = Category.objects.filter(slug=slug).first()
        products = Product.objects.filter(category=category)
        return Response(ProductDTO(products, many=True).data)

class CartView(APIView):
    def post(self, request, product_id):
        attributes = AddCartDao(data=request.data)
        if not attributes.is_valid():
            return bad_request(attributes.errors)

        product = Product.objects.filter(
            uuid=product_id, is_archived=False).first()
        if not product:
            return success({}, "invalid product id", False)

        cart = Cart.objects.filter(product=product, user=request.user).first()
        if not cart:
            cart = Cart(product=product, user=request.user)
            cart.quantity = attributes.data["quantity"]
            cart.color = attributes.data["color"]
        else:
            cart.quantity = attributes.data["quantity"]
            cart.color = attributes.data["color"]
        cart.save()

        return success({}, "product added successfully", True)

    def delete(self, request, product_id):
        product = Product.objects.filter(
            uuid=product_id, is_archived=False).first()
        if not product:
            return success({}, "invalid product id", False)

        cart = Cart.objects.filter(product=product, user=request.user).first()
        if not cart:
            return success({}, "product not present in cart", False)

        if cart.quantity == 1:
            cart.delete()
        else:
            cart.quantity -= 1
            cart.save()

        return success({}, "product removed successfully", True)

