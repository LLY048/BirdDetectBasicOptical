# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from streamManage.readDirectFromStream import streamToFrame
from django.http import JsonResponse
from django.conf import settings


@csrf_exempt
def birdCheck0915(request):
    url = request.POST.get("url")
    timeSeg = settings.TIMESEG
    fourcc = settings.FOURCC
    outVideoDir = settings.OUTVIDEODIR
    reSize = settings.OUTPUTSIZE
    resultList = streamToFrame(url, timeSeg, outVideoDir, reSize, fourcc)
    serverUrl = settings.STREAMURL
    print(resultList)
    return JsonResponse({"status": 200, "msg": "OK", "url": serverUrl, "data": resultList})
    # try:
    #     pass
    # except Exception as e:
    #     pass