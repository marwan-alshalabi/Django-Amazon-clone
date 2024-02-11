from rest_framework import serializers
from .models import Product , Brand , Review , ProductImages


class Productserializers(serializers.ModelSerializer):
    class Meta :
        model = Product
        fields = '__all__'