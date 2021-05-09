from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Category
from core.serializers.dto import CategoryDTO

class CategoryList(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        return Response(CategoryDTO(categories, many=True).data)
