from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from store.filters import ProductFilter
from store.pagination import DefaultPagination
from .models import Cart, Collection, OrderItem, Product, Review
from .serializers import CartSerializer, CollectionSerializers, ProductSerializers, ReviewSerializer
from rest_framework.views import APIView
from django.db.models import Count


# Create your views here.


# def product_list(request):
#     return render(request, "product_list.html")


class ProductViewSet(ModelViewSet):
    # queryset = Product.objects.select_related('collection').all()
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title', 'description']
    # filterset_fields = ['collection_id']
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    ordering_fields = ['unit_price', 'last_update']

    # def get_queryset(self):
    #     queryset = Product.objects.select_related('collection').all()
    #     collection_id = self.request.query_params.get('collection_id')
    #     if collection_id is not None:
    #         queryset = queryset.filter(collection_id=collection_id)
    #     return queryset

    def get_serializer_context(self):
        return {'request': self.request}

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        return super().destroy(request, *args, **kwargs)

    # def delete(self, request, pk):
    #     product = get_object_or_404(Product, pk=pk)
    #     if product.orderitems.count() > 0:
    #         return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #     product.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


# Class Based View

# class ProductList(ListCreateAPIView):
    # queryset = Product.objects.select_related('collection').all()
    # serializer_class = ProductSerializers

    # if we don't have any logic we don't need this
    # def get_queryset(self):
    #     return Product.objects.select_related('collection').all()
    # def get_serializer_class(self):
    #     return ProductSerializers
    # def get_serializer_context(self):
    #     return {'request': self.request}

    # def get(self, request):
    #     queryset = Product.objects.select_related('collection').all()
    #     serializer = ProductSerializers(
    #         queryset, many=True, context={'request': request})
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = ProductSerializers(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


# class ProductDetail(RetrieveUpdateDestroyAPIView):
#     # product = get_object_or_404(Product, pk=id)
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializers

    # def get(self, request, id):
    #     product = get_object_or_404(Product, pk=id)
    #     serializer = ProductSerializers(product)
    #     return Response(serializer.data)

# already implemented b/c we Used RUDA
    # def put(self, request, id):
    #     product = get_object_or_404(Product, pk=id)
    #     serializer = ProductSerializers(product, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

    # def delete(self, request, pk):
    #     product = get_object_or_404(Product, pk=pk)
    #     if product.orderitems.count() > 0:
    #         return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #     product.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

# Function Based View
# @api_view(['GET', 'POST'])
# def product_list(request):
#     if request.method == 'GET':
#         queryset = Product.objects.select_related('collection').all()
#         serializer = ProductSerializers(
#             queryset, many=True, context={'request': request})
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProductSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # print(serializer.validated_data)
#         # return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#         # if serializer.is_valid():
#         #     serializer._validated_data
#         #     return Response('ok')
#         # else:
#         #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Function Based View
# @api_view(['GET', 'PUT', 'DELETE'])
# def product_detail(request, id):
#     product = get_object_or_404(Product, pk=id)
#     if request.method == 'GET':
#         serializer = ProductSerializers(product)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         # product = Product.objects.get(pk=id)
#         serializer = ProductSerializers(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         if product.orderitems.count() > 0:
#             return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    # try:
    #     product = Product.objects.get(pk=id)
    #     serializer = ProductSerializers(product)
    #     return Response(serializer.data)
    # except Product.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

# class CollectionList(APIView):
#     def get(self, request):
#         queryset = Collection.objects.annotate(
#             products_count=Count('product')).all()
#         serializer = CollectionSerializers(
#             queryset, many=True, context={'request': request})
#         return Response(serializer.data)

# if request.method == 'GET':
    #         # queryset = Collection.objects.select_related('co')
    #         queryset = Collection.objects.annotate(
    #             products_count=Count('product')).all()
    #         serializer = CollectionSerializers(
    #             queryset, many=True, context={'request': request})
    #         return Response(serializer.data)
    #     elif request.method == 'POST':
    #         serializer = CollectionSerializers(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         # print(serializer.validated_data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

# class ProductList(ListCreateAPIView):
#     queryset = Product.objects.select_related('collection').all()
#     serializer_class = ProductSerializers

#     # if we don't have any logic we don't need this
#     # def get_queryset(self):
#     #     return Product.objects.select_related('collection').all()
#     # def get_serializer_class(self):
#     #     return ProductSerializers
#     def get_serializer_context(self):
#         return {'request': self.request}

class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(
        products_count=Count('products')).all()
    serializer_class = CollectionSerializers

    def delete(self, request, pk):
        collection = get_object_or_404(Collection.objects.annotate(
            products_count=Count('products')), pk=pk)
        if collection.count() > 0:
            return Response({'error': 'Collection cannot be deleted because it is associated with a product.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewViewSet(ModelViewSet):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}


class CartViewSet(CreateModelMixin,  GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
# class CollectionList(ListCreateAPIView):

#     def get_queryset(self):
#         return Collection.objects.annotate(
#             products_count=Count('products')).all()

#     def get_serializer_class(self):
#         return CollectionSerializers

#     def get_serializer_context(self):
#         return {'request': self.request}
    # def get(self, request):
    #     queryset = Collection.objects.annotate(
    #         products_count=Count('product')).all()
    #     serializer = CollectionSerializers(
    #         queryset, many=True, context={'request': request})
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = CollectionSerializers(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


# class CollectionDetail(RetrieveUpdateDestroyAPIView):
#     # queryset = Product.objects.all()
#     queryset = Collection.objects.annotate()
#     serializer_class = CollectionSerializers

    # def get(self, request, pk):
    #     collection = get_object_or_404(Collection.objects.annotate(
    #         products_count=Count('products')), pk=pk)
    #     serializer = Collection.objects.annotate(collection)
    #     return Response(serializer.data)

    # def put(self, request, pk):
    #     collection = get_object_or_404(Collection.objects.annotate(
    #         products_count=Count('products')), pk=pk)

    #     serializer = CollectionSerializers(collection, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     print(serializer.validated_data)
    #     serializer.save()
    #     return Response(serializer.data)

    # def delete(self, request, pk):
    #     collection = get_object_or_404(Collection.objects.annotate(
    #         products_count=Count('products')), pk=pk)
    #     if collection.count() > 0:
    #         return Response({'error': 'Collection cannot be deleted because it is associated with a product.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #     collection.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def collection_list(request):
#     if request.method == 'GET':
#         # queryset = Collection.objects.select_related('co')
#         queryset = Collection.objects.annotate(
#             products_count=Count('product')).all()
#         serializer = CollectionSerializers(
#             queryset, many=True, context={'request': request})
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CollectionSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # print(serializer.validated_data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def collection_detail(request, pk):
#     collection = get_object_or_404(Collection.objects.annotate(
#         products_count=Count('products')), pk=pk)
#     if request.method == 'GET':
#         serializer = CollectionSerializers(collection)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = CollectionSerializers(collection, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         print(serializer.validated_data)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         if collection.count() > 0:
#             return Response({'error': 'Collection cannot be deleted because it is associated with a product.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         collection.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
