from rest_framework import viewsets
from .models import Store, Category, Product, Sale
from .serializers import (
    StoreSerializer,
    CategorySerializer,
    ProductSerializer,
    SaleSerializer
)


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer








# from django.shortcuts import render

# # Create your views here.
# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
# from .models import Store, Category, Product, Sale
# from .serializers import (
#     StoreSerializer,
#     CategorySerializer,
#     ProductSerializer,
#     SaleSerializer
# )

# class StoreViewSet(viewsets.ModelViewSet):
#     serializer_class = StoreSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Store.objects.filter(owner=self.request.user)

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class CategoryViewSet(viewsets.ModelViewSet):
#     serializer_class = CategorySerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Category.objects.filter(store=self.request.user.store)

#     def perform_create(self, serializer):
#         serializer.save(store=self.request.user.store)



# class ProductViewSet(viewsets.ModelViewSet):
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Product.objects.filter(store=self.request.user.store)

#     def perform_create(self, serializer):
#         serializer.save(store=self.request.user.store)


# class SaleViewSet(viewsets.ModelViewSet):
#     serializer_class = SaleSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Sale.objects.filter(store=self.request.user.store)

#     def perform_create(self, serializer):
#         serializer.save(store=self.request.user.store)
