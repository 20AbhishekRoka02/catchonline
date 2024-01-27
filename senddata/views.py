from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Query, Test
from .serializers import QuerySerializer, TestSerializer
from rest_framework import serializers
from rest_framework import status

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'Add': '/create',
        
    }
 
    return Response(api_urls)

@api_view(['POST'])
def add_query(request):
    item = QuerySerializer(data=request.data)
 
    # validating for already existing data
    if Query.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_test_query(request):
    item = TestSerializer(data=request.data)
 
    # validating for already existing data
    if Query.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)