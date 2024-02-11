from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

from .serializers import Productserializers
from .models import Product



# @api_view(["GET"])
# def product_list_api(request):
#     products = Product.objects.all() 
#     data = Productserializers(products,many=True).data 
#     return Response({'products':data})


class ProductListAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = Productserializers


class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = Productserializers