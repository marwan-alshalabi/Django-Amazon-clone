from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

from .serializers import ProductSerializers , BrandSerializers
from .models import Product , Brand



# @api_view(["GET"])
# def product_list_api(request):
#     products = Product.objects.all() 
#     data = Productserializers(products,many=True).data 
#     return Response({'products':data})


class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers



class BrandListAPI(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializers


class BrandDetailApi(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializers
