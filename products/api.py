from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

from .serializers import Productserializers , Brandserializers
from .models import Product , Brand



# @api_view(["GET"])
# def product_list_api(request):
#     products = Product.objects.all() 
#     data = Productserializers(products,many=True).data 
#     return Response({'products':data})


class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = Productserializers


class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = Productserializers



class BrandListAPI(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = Brandserializers


class BrandDetailApi(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = Brandserializers
