from django.shortcuts import get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
import rest_framework
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
        # serializer._validated_data
        return Response('ok')


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
