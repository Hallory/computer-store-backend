from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from catalog.models import Category, Product
from catalog.serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ["name"]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.select_related("category").all()
    serializer_class = ProductSerializer
    lookup_field = "slug"
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["category","brand","in_stock"]
    search_fields = ["name","description"]
    ordering_fields = ["price","rating","created_at"]
    ordering = ["-created_at"]