from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.db.models import Q
from store_api import mixins as mx
from store_api.serializers import ProductSerializer, StoreSerializer, SaleItemSerializer
from products_app.models import Product, User, SaleItem, Sale
from store_api import functions

# Create your views here.


class AllProductsView(mx.AuthenticationMixin, generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        queryset = queryset.filter(store=self.request.user)
        query = self.request.query_params.get("q")
        if query is not None:
            queryset = queryset.filter(
                Q(Title__icontains=query) |
                Q(Description__icontains=query)
            )
        return queryset


class GetSingleProductView(mx.AuthenticationMixin, generics.RetrieveAPIView):
    lookup_field = "URL"
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateProductView(mx.AuthenticationMixin, mx.ProductQuerySetMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        product_url = functions.product_url()
        user = self.request.user
        serializer.save(store=user, URL=product_url)


class EditProductView(mx.AuthenticationMixin, generics.UpdateAPIView):
    lookup_field = "URL"
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance)
        if instance.store != request.user:
            response = {
                "message": "The product does not belong to you",
                "success": "false"
            }
            return Response(response)

        else:
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            response = {
                "message": "product successfully updated"
            }
            return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class DeleteProductView(mx.AuthenticationMixin, generics.DestroyAPIView):
    lookup_field = "URL"
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.store != request.user:
            response = {
                "message": "The product does not belong to you",
                "success": "false"
            }

        else:
            self.destroy(request, *args, **kwargs)
            response = {
                "message": "Product successfully deleted",
                "success": "true"
            }
        return Response(response)


class GetAllStoresView(mx.AuthenticationMixin, generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = StoreSerializer


class GetSingleStoreView(mx.AuthenticationMixin, generics.RetrieveAPIView):
    lookup_field = "pk"
    queryset = User.objects.all()
    serializer_class = StoreSerializer


class GetUserSales(mx.AuthenticationMixin, generics.ListAPIView):
    serializer_class = SaleItemSerializer

    def get_queryset(self):
        store = self.request.user
        store_sale = Sale.objects.get_or_create(user=store)
        sale_items = store_sale.saleitem_set.all()
        return sale_items