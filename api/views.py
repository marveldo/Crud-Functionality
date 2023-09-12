from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import status




@api_view(['POST'])
def Createuser(request):
    data = request.data

    try:
        data_info = request.data['name']
    except :
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    serializer = ProfileSerializer(data= request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
       
        
@api_view(['GET','PUT','DELETE'])
def Getprofile(request,pk):
    if request.method == 'GET':
        try:
           profile = Profile.objects.get(id = pk)
        except Profile.DoesNotExist:
           return Response(status=status.HTTP_404_NOT_FOUND)
    
        serializer = ProfileSerializer(profile, many = False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        data = request.data
        try:
           profile = Profile.objects.get(id = pk)
           
        except Profile.DoesNotExist:
           return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            data_info = data['name']
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)

             
        serializer = ProfileSerializer(profile, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        try:
           profile = Profile.objects.get(id = pk)
        except Profile.DoesNotExist:
           return Response(status=status.HTTP_404_NOT_FOUND)
        
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        
    

        
            


