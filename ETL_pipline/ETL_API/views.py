from django.shortcuts import render
from django.http import JsonResponse
from .models import car_data
from django.db import IntegrityError  # Import for error handling

def read_first_chunk(request):
    try:
        if request.method == 'GET':
            data = car_data.objects.all()[:10].values()  # the first 10 records from the database
            serialized_data = list(data.values())
            return JsonResponse(serialized_data, safe=False)
        else:
            return JsonResponse({'error': 'Invalid request method'}, status=405)
    except IntegrityError as e:
        return JsonResponse({'error': 'Database error'}, status=500)