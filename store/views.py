from django.shortcuts import get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializers


# Create your views here.


# def product_list(request):
#     return render(request, "product_list.html")

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        queryset = Product.objects.select_related('collection').all()
        serializer = ProductSerializers(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response('OK')

        # if serializer.is_valid():
        #     serializer._validated_data
        #     return Response('ok')
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view()
def product_detail(request, id):
    product = get_list_or_404(Product, pk=id)
    serializers = ProductSerializers(product)
    return Response(serializers.data)
    # try:
    #     product = Product.objects.get(pk=id)
    #     serializer = ProductSerializers(product)
    #     return Response(serializer.data)
    # except Product.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)


@api_view()
def collection_detail(request, pk):
    return Response('ok')
