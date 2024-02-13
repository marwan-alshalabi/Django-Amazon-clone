from rest_framework import serializers
from .models import Product , Brand , Review , ProductImages


class Brandserializers(serializers.ModelSerializer):
    class Meta :
        model = Brand
        fields = '__all__'



class Productserializers(serializers.ModelSerializer):
    brand = serializers.RelatedField()
    class Meta :
        model = Product
        fields = '__all__'



