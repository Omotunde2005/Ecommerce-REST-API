from rest_framework import serializers, reverse
from products_app import models


class UserSerializer(serializers.ModelSerializer):
    store_link = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.User
        fields = [
            'email',
            'name',
            "store_link"
        ]

    def get_store_link(self, obj):
        request = self.context.get("request")
        pk = obj.pk
        return reverse.reverse("single-store", kwargs={"pk": pk}, request=request)


class ProductSerializer(serializers.ModelSerializer):
    product_store = UserSerializer(read_only=True, source="store")
    product_link = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Product
        fields = [
            "URL",
            "product_store",
            "Description",
            "Title",
            "Price",
            "Image",
            "product_link"
        ]

    def get_product_link(self, obj):
        request = self.context.get("request")
        url = obj.URL
        return reverse.reverse("single-product", kwargs={"URL": url}, request=request)


class StoreSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.User
        fields = [
            'email',
            'name',
            'products'
        ]

    def get_products(self, obj):
        store_products = obj.product_set.all()
        srz = ProductSerializer(store_products, many=True)
        return srz.data


class SaleItemSerializer(serializers.ModelSerializer):
    user = StoreSerializer(read_only=True, source="purchased_by")
    purchased_product = ProductSerializer(read_only=True, source="product")

    class Meta:
        model = models.SaleItem
        fields = ["quantity",
                  "user",
                  "purchased_product"]