from rest_framework import serializers
from . models import *
  


# class JSONSerializerField(serializers.Field):
#     """ Serializer for JSONField -- required to make field writable"""
#     def to_internal_value(self, data):
#         return data
#     def to_representation(self, value):
#         return value


class CarryAndCompsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarryAndComps
        fields = ['name','body']
        # fields = ['name',]
    
    # json_data = JSONSerializerField()
 

 
