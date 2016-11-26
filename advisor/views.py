from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse, HttpRequest
from .models import Auto


def index(request):

    template = loader.get_template('advisor/index.html')
    context = {'bla': 1}
    return HttpResponse(template.render(context, request))


def response(request):

    print (request.GET.get('patente'))
    plate = request.GET.get('patente')
    owner_info = Auto.objects.filter(plate=plate)
    if len(owner_info) is 0:
        prop = "Patente no registrada"
        return render(request, 'advisor/response.html', {'bli': prop})
    prop = []
    for CAR in owner_info:
        print (CAR.owner)
        prop.append(str(CAR.owner))
        prop.append(str(CAR.class_name))
    return render(request, 'advisor/response.html', {'bli': prop[0], 'ble': prop[1]})
