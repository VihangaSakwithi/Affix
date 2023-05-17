from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from proworkerApp.models import ProWorkers
from proworkerApp.serializers import ProworkerSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def proworkerApi(request,id=0):
    if request.method=='GET':
        proworkers = ProWorkers.objects.all()
        proworkers_serializer=ProworkerSerializer(proworkers,many=True)
        return JsonResponse(proworkers_serializer.data,safe=False)
    
    elif request.method=='POST':
        proworker_data=JSONParser().parse(request)
        proworkers_serializer=ProworkerSerializer(data=proworker_data)
        if proworkers_serializer.is_valid():
            proworkers_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    
    elif request.method=='PUT':
        proworker_data=JSONParser().parse(request)
        proworker=ProWorkers.objects.get(ProWorkerId=proworker_data['ProWorkerId'])
        proworkers_serializer=ProworkerSerializer(proworker,data=proworker_data)
        if proworkers_serializer.is_valid():
            proworkers_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method=='DELETE':
        proworker=ProWorkers.objects.get(ProWorkerId=id)
        proworker.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)