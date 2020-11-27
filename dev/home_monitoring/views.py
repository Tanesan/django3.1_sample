from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.utils import timezone

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from home_monitoring.models import IOT
from home_monitoring.serializers import IoTSerializer

def index(request):
    
    return render(request, 
    'dashboard.html', {})


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def send(request):

    # accesstokenを調べる

    # name をもつuserが登録されているかを確認する。


    # PUT

    if request.method == 'PUT':

        data = JSONParser().parse(request)
        serializer = IoTSerializer(data=data)
        print("■■■■■■■■■■■■■■■■■■■■■■■■■", data)
        data.update({"pub_date": timezone.now()})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse(serializer.errors, status=400)
