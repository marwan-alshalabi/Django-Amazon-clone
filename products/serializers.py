from rest_framework import serializers
from .models import Product , Brand , Review , ProductImages


class BrandListSerializers(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()
    class Meta :
        model = Brand
        fields = '__all__'

    def get_products_count(self,object) :
        count = object.product_brand.all().count()
        return count





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
    review_count = serializers.SerializerMethodField()
    class Meta :
        model = Product
        fields = '__all__' 

    def get_review_count (self, object):
        review_counts = object.review_product.all().count()
        return review_counts



class ProductDetailSerializers(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    product_images = ProductImagesSerializers(many=True)
    review_product = ReviewSerializers(many=True)
    review_count = serializers.SerializerMethodField()

    class Meta :
        model = Product
        fields = '__all__'

    def get_review_count (self, object):
        review_counts = object.review_product.all().count()
        return review_counts



class BrandDetailSerializers(serializers.ModelSerializer):
    product_brand = ProductListSerializers(many=True)
    products_count = serializers.SerializerMethodField()
    class Meta :
        model = Brand
        fields = '__all__'
    
    
    def get_products_count(self,object) :
        count = object.product_brand.all().count()
        return count


    