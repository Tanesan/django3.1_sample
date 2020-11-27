from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from home_monitoring.models import IOT
from home_monitoring.serializers import IoTSerializer

import plotly.figure_factory as ff
from plotly.offline import plot
df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
      dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
      dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')]
fig = ff.create_gantt(df)
plot_fig = plot(fig, output_type='div', include_plotlyjs=True)


# DASHBOARD
# @login_required
# if User.is_authentificated is not True,  accounts/login redirect executed.
# 
def index(request):    
    return render(request, 
    'dashboard.html', {})


def shower(request):
    # user情報取得
    # ユーザに関わるshowerデータ取得
    # ここのイメージずれていた。
    return render(request, 
    'shower.html', {})

def toilet(request):
    # user情報取得
    # ユーザに関わる排便データ取得
    # ここのイメージずれていた。

    return render(request, 'toilet.html', {"plot_div":df})

def curtain(request):
    # user情報取得
    # ユーザに関わるshowerデータ取得
    # ここのイメージずれていた。
    return render(request, 
    'curtain.html', {})



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
