from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


from receive_censor_data.models import HomeMonitoringIot


from receive_censor_data.serializers import IoTSerializer

@csrf_exempt
def send(request, name):

    # accesstokenを調べる

    # name をもつuserが登録されているかを確認する。


    # PUT

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = IoTSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse(serializer.errors, status=400)
