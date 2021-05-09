from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Product
from core.serializers.dto import ProductDTO

class ProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        return Response(ProductDTO(products, many=True).data)
