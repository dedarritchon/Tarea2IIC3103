from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from hamburguesas.models import Hamburguesa, Ingrediente
from hamburguesas.serializers import HamburguesaSerializer, IngredienteSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def index(request):
    return render(request, 'hamburguesas/index.html', status=404)


@csrf_exempt
def hamburguesa_list(request):
    """
    List all code serie, or create a new serie.
    """
    if request.method not in ('GET', 'POST'):
        return HttpResponse(status=404)

    if request.method == 'GET':
        hamburguesas = Hamburguesa.objects.all()
        serializer = HamburguesaSerializer(hamburguesas, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        try:
            data = JSONParser().parse(request)
        except:
            return HttpResponse(status=400)
        serializer = HamburguesaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def hamburguesa_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    if request.method not in ('GET', 'PATCH', 'DELETE'):
        return HttpResponse(status=404)

    if not pk.isdigit():
        return HttpResponse(status=400)
    try:
        hamburguesa = Hamburguesa.objects.get(pk=pk)
    except Hamburguesa.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = HamburguesaSerializer(hamburguesa)
        return JSONResponse(serializer.data)

    elif request.method == 'PATCH':
        try:
            data = JSONParser().parse(request)
        except:
            return HttpResponse(status=400)
        
        serializer = HamburguesaSerializer(hamburguesa, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=200)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        print("DELEEEETE")
        hamburguesa.delete()
        return HttpResponse(status=200)


@csrf_exempt
def ingrediente_list(request):
    """
    List all code serie, or create a new serie.
    """
    if request.method not in ('GET', 'POST'):
        return HttpResponse(status=404)

    if request.method == 'GET':
        ingredientes = Ingrediente.objects.all()
        serializer = IngredienteSerializer(ingredientes, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        try:
            data = JSONParser().parse(request)
        except:
            return HttpResponse(status=400)
        serializer = IngredienteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def ingrediente_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    if request.method not in ('GET', 'DELETE'):
        return HttpResponse(status=404)
    
    if not pk.isdigit():
        return HttpResponse(status=400)
    
    try:
        ingrediente = Ingrediente.objects.get(pk=pk)
    except Ingrediente.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = IngredienteSerializer(ingrediente)
        return JSONResponse(serializer.data)

    elif request.method == 'DELETE':

        for hamburguesa in Hamburguesa.objects.all():
            if ingrediente in hamburguesa.ingredientes.all():
                return HttpResponse(status=409)

        ingrediente.delete()
        return HttpResponse(status=200)
    


@csrf_exempt
def hamburguesa_edit(request, h_pk, i_pk):
    """
    Edit hamburguer
    """
    if request.method not in ('PUT', 'DELETE'):
        return HttpResponse(status=404)
    
    if not h_pk.isdigit():
        return HttpResponse(status=400)
    if not i_pk.isdigit():
        return HttpResponse(status=400)

    try:
        ingrediente = Ingrediente.objects.get(pk=i_pk)
    except Ingrediente.DoesNotExist:
        return HttpResponse(status=404)
    
    try:
        hamburguesa = Hamburguesa.objects.get(pk=h_pk)
    except Hamburguesa.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'PUT':
        hamburguesa.ingredientes.add(ingrediente)
        return HttpResponse(status=201)


    elif request.method == 'DELETE':
        if ingrediente in hamburguesa.ingredientes.all():
            hamburguesa.ingredientes.remove(ingrediente)
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)

