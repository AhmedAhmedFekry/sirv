from django.shortcuts import render
from SirvPy import get_access, upload_files ,search_files,account_info,get_users,get_spins_views
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from pathlib import Path
from home.serializers import UploadFileSerializer




@api_view(['GET'])
def  account_infomation(request):
    clientId2 = 'LjfSygEduUnaQJ0Ltu3GprGCpyX'
    clientSecret2 = '6gnPaSTmIXMGRASMCwoDMipL56aqP+eRcxJFxLXBzWb97rBuPSzYTLh4l9pN3gSEH1XIXsUtlmpQwmoKc0CtWA=='
    access_to = get_access(clientId2, clientSecret2)['token']
    print("the token is ",access_to)
    data= account_info(access_to)
    print("the tpe of ",type(data))
    print("the tpe of ",data.json())
    return Response(data.json(),status=status.HTTP_200_OK)


# # Create your views here.
clientId2 = 'MTlcBJbEpi1XKL53F80VvxEbbDp'
clientSecret2 = '6xC8+n/2dZNAVyDxRcWFV/CjD55cPSLfuHU13Y18vElbFF1/tob0UdHGJ/h9WiZ+385NRqE+hichB4cB4rZWXQ=='


# Create your views here.
clientId = 'Pf3ENRG6zsN2uLvsgJ7K6CXDUDq'
clientSecret = 'aAgBLboBCIEaL+NrS9YPfAPsVg3eZczVtwY/5sHpM7OkuUkOwwGSJ6ldLiRUEloh9W/kE4GIe17hE4E81cCdOg=='





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
def get_spins_viewss(request):
    access_token1 = get_access(clientId, clientSecret)['token']
    data=get_spins_views(access_token1)
    return Response(data.json(),status=status.HTTP_200_OK)
#####################################################################



@api_view(['POST'])
def upload_file(request):
    # data=get_users(access_token1)
    print("the request data ", request.data)
    fil=UploadFileSerializer(data=request.data)
    if fil.is_valid():
        print("the request body FILES", request.FILES)

        print("____________________________________________________________")
        print("success ")
        upload_path = '/myfolder/'
        access_token1 = get_access(clientId, clientSecret)['token']
        if request.method=="POST":
            print(" the file name",request.FILES['file'].name)
            p=Path(request.FILES['file'].name)
            extensions = "".join(p.suffixes)
            print("the extenstions", extensions)
            print(" the  new file name",p)
            (prefix, sep, suffix) = request.FILES['file'].name.rpartition('.')
            print(" the  prefix file name",prefix)
            print(" the  sep file name",sep)
            url='https://mostafasamir.sirv.com/{name}/{name}.spin'.format(name=prefix)
            print("url",url )
            print(" the  suffix file name",suffix)
            # print(" the file size",request.FILES['file'].size)
            # print(" the file charset",request.FILES['file'].charset)
            # print(" the file content_type",request.FILES['file'].content_type)
            # print(" the file size",request.FILES['file'].size)

            # print(" tje file name type",type(request.FILES['file']))
            upload_files(access_token1, request.FILES['file'], upload_path)
    
        return Response({"message","done"},status=status.HTTP_200_OK)
    print("**************************************")

    return Response(fil.errors,status=status.HTTP_400_BAD_REQUEST)
