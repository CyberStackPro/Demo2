from rest_framework import serializers
from store.models import Product, Collection
from decimal import Decimal


# Serializer
# class CollectionSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Collection
#         fields = ['id', 'title']
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
# Model Serializer


class CollectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)


# class ProductSerializers(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(
#         max_digits=6, decimal_places=2, source='unit_price')
#     price_with_tax = serializers.SerializerMethodField(
#         method_name='calculate_tax')
#     # collection = serializers.PrimaryKeyRelatedField(
#     #     queryset=Collection.objects.all())
#     # collection = serializers.StringRelatedField()
#     # collection = CollectionSerializers()
#     collection = serializers.HyperlinkedRelatedField(
#         queryset=Collection.objects.all(),
#         view_name='collection-detail'
#     )

# Model Serializer


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['id', 'title', 'description', 'unit_price',
                  'slug', 'inventory', 'price_with_tax', 'collection']
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(
    #     max_digits=6, decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')
    # # collection = serializers.PrimaryKeyRelatedField(
    # #     queryset=Collection.objects.all())
    # # collection = serializers.StringRelatedField()
    # # collection = CollectionSerializers()
    # collection = serializers.HyperlinkedRelatedField(
    #     queryset=Collection.objects.all(),
    #     view_name='collection-detail'
    # )

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)

    # def create(self, validated_data):
    #     product = Product(**validated_data)
    #     product.others = 1
    #     product.save()
    #     return product
    # def update(self, instance, validated_data):
    #     instance.unit_price = validated_data.get('unit_price')
    #     instance.save()
    #     return instance


# {
#     "title": "A",
#     "slug": "a",
#     "unit_price": 1,
#     "collection": 1,
#     "inventory": 1
# }
