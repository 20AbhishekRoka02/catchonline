from django.db.models import fields
from rest_framework import serializers
from .models import Query, Test
 
class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = ('id','message')

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id','message')