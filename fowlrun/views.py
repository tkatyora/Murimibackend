from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializers import ConditionsSerializer
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import FowlRunConditions
# Create your views here.
@api_view(['GET' ,'POST'])
def ViewConditions_list(request):
    if request.method == 'GET':
        conditions = FowlRunConditions.objects.all()
        serializer = ConditionsSerializer(conditions )
        return Response(serializer.data)
    elif request.method == 'POST':
        condition = ConditionsSerializer(data=request.data)
        if condition.is_valid():
            condition.save()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status =status.HTTP_405_METHOD_IS_NOT_ALLOWED)

@api_view(['GET','POST','PUT','DELETE'])
def SingleCondition(request ,pk):
    try: 
        #The condition which s needed to be deleted ,created, updated and viewed
        condition = FowlRunConditions.objects.get(id= pk)
    except condition.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ConditionsSerializer(condition) 
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ConditionsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        serializer = ConditionsSerializer(conditon,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(status= status.HTTP_406_NOT_ACCEPTABLE)
    elif request.method == 'DELETE':
        condition.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(serializer.errors, status =status.HTTP_405_METHOD_NOT_ALLOWED)