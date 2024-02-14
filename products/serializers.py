from rest_framework import serializers
from .models import Product , Brand , Review , ProductImages


class BrandListSerializers(serializers.ModelSerializer):
    class Meta :
        model = Brand
        fields = '__all__'


class BrandDetailSerializers(serializers.ModelSerializer):
    class Meta :
        model = Brand
        fields = '__all__'


class ProductImagesSerializers(serializers.ModelSerializer):
    class Meta :
        model =  ProductImages
        fields  = '__all__'



class ReviewSerializers(serializers.ModelSerializer):
    class Meta :
        model = Review
        fields  = '__all__'




class ProductListSerializers(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    class Meta :
        model = Product
        fields = '__all__' 



class ProductDetailSerializers(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    product_images = ProductImagesSerializers(many=True)
    review_product = ReviewSerializers(many=True)

    class Meta :
        model = Product
        fields = '__all__' 



