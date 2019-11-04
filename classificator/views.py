import json
from django.http import JsonResponse
from django.shortcuts import render
from . import models
from django.views.decorators.csrf import csrf_exempt
from classificator import predict


def index(request):
    return render(request, 'index.html')


def history(request):
    his = models.Trash.objects.all().order_by('-id')[:10]
    #his = models.Trash.objects.filter(timeStamp__day=datetime.date.today().day).order_by('-id')[:1]
    return render(request, 'history.html', {'history': his})


def support(request):
    return render(request, 'support.html')


@csrf_exempt
def process(request):
    content = json.loads(request.body)['content']
    print(content[23:])
    result = predict.PredictGarbageType(content[23:])
    '''
    print(result)
    retval = ''
    if result == 0:
        retval = 'cup'
    elif result == 1:
        retval = 'book'
    elif result == 2:
        retval = 'plastic wrapper'
    elif result == 3:
        retval = 'bottle'
    elif result == 4:
        retval = 'paper'
    else:
        retval = 'trash'
    '''
    models.Trash.objects.create(content=content, result='retval')
    return JsonResponse({'result': 'retval'})
