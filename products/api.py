from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


from .serializers import ProductDetailSerializers, ProductListSerializers , BrandListSerializers, BrandDetailSerializers
from .models import Product , Brand
from .mypagination import CustomPagination


# @api_view(["GET"])
# def product_list_api(request):
#     products = Product.objects.all() 
#     data = Productserializers(products,many=True).data 
#     return Response({'products':data})


class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializers
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['flag', 'brand', 'quantity']
    search_fields = ['name', 'subtitle','description']
    ordering_fields = ['price', 'quantity', 'name']



class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializers



class BrandListAPI(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializers
    pagination_class = CustomPagination
    


class BrandDetailApi(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializers
