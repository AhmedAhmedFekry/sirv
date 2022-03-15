from django.shortcuts import render
from SirvPy import get_access, upload_files ,search_files
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
clientId ="UHX1CNPhTW93q98lzj3Ll0l2fdB"
clientSecret ="IzW5lm0Xvc8NdhrAOCB6+81ZynReBwA1w4zDllUwrWbKk4B2Tl2bXEWNQwLRiUglljKlywbimBAMYDa/p97ikg=="



@api_view(['POST'])
def access(request):
    access_token = get_access(clientId, clientSecret)
    print("access_token",access_token)
    # print("the request body", request.FILES)
    return Response(access_token,status=status.HTTP_200_OK)



access_token = get_access(clientId, clientSecret)

# def accessTem(request):

    # upload_path = '/myfolder/'
    # if request.method=="POST":
    #     upload_files(access_token, request.FILES['file_upload'], upload_path)
    
    # return render(request, 'form.html')



@api_view(['GET'])
def search(request):
    data=search_files(access_token)
    return Response(data,status=status.HTTP_200_OK)




import requests
import time
import json #for parsing str into dict
import ast #for parsing single quote "json" to dict

import re

base_url = "https://api.sirv.com"

def upload_filesd(access_token, local_file, upload_path):
	endpoint = base_url + "/v2/files/upload"
	headers = {"Content-Type" : "application/zip", "authorization": "bearer {}".format(access_token)}
	upload_path = {"filename": upload_path}#The path to which the file will be uploaded TBD

	if str(local_file.__class__) == "<class 'str'>":
		print("User passed a File Path")
		open_file = open(local_file, 'rb')
		sirv_api_request = requests.post(endpoint, headers = headers, data = open_file, params = upload_path)
	elif re.match("<class 'django.core.files", str(local_file.__class__)):
		print("User passed a django uploadfile")
		sirv_api_request = requests.post(endpoint, headers = headers, data = local_file, params = upload_path)
	else:
		print("Unsupported file source")
		return

	if sirv_api_request.status_code == 200:
		print("Successfully uploaded file")
	else:
		print("Error {}. File upload failed".format(sirv_api_request.status_code))

	return sirv_api_request

    
def accessTem(request):

    upload_path = '/myfolder/'
    if request.method=="POST":
        upload_filesd(access_token, request.FILES['file_upload'], upload_path)
    
    return render(request, 'form.html')