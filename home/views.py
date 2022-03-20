from django.shortcuts import render
from SirvPy import get_access, upload_files ,search_files,account_info,get_users,get_spins_views
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
clientId = 'MTlcBJbEpi1XKL53F80VvxEbbDp'
clientSecret = '6xC8+n/2dZNAVyDxRcWFV/CjD55cPSLfuHU13Y18vElbFF1/tob0UdHGJ/h9WiZ+385NRqE+hichB4cB4rZWXQ=='




@api_view(['POST'])
def access(request):
    access_token = get_access(clientId, clientSecret)
    print("the request body", request.FILES)
    return Response(access_token,status=status.HTTP_200_OK)



access_token1 = get_access(clientId, clientSecret)['token']

def accessTem(request):

    upload_path = '/myfolder/'
    access_token1 = get_access(clientId, clientSecret)['token']
    if request.method=="POST":
        upload_files(access_token1, request.FILES['file_upload'], upload_path)
    
    return render(request, 'form.html')

@api_view(['GET'])
def get_userss(request):
    data=get_users(access_token1)
    return Response(data.json(),status=status.HTTP_200_OK)


@api_view(['GET'])
def search(request):
    access_token1 = get_access(clientId, clientSecret)['token']
    data=search_files(access_token1)
    return Response(data.json(),status=status.HTTP_200_OK)


@api_view(['GET'])
def  account_infomation(request):
    data= account_info(access_token1)
    print("the tpe of ",type(data))
    print("the tpe of ",data.json())
    return Response(data.json(),status=status.HTTP_200_OK)


@api_view(['GET'])
def get_spins_viewss(request):
    access_token1 = get_access(clientId, clientSecret)['token']
    data=get_spins_views(access_token1)
    return Response(data.json(),status=status.HTTP_200_OK)
