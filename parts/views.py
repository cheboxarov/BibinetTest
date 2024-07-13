from django.http import JsonResponse
from .models import Mark, Model, Part
from django.db.models import Q, Sum
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json


def mark_list(request):
    marks = list(Mark.objects.filter(is_visible=True).values('id', 'name', 'producer_country_name'))
    print(marks)
    return JsonResponse(marks, safe=False)


def model_list(request):
    models = list(Model.objects.filter(is_visible=True).values('id', 'name', 'mark_id'))
    return JsonResponse(models, safe=False)

@csrf_exempt
@require_POST
def search_parts(request):
    data = json.loads(request.body)
    mark_name = data.get('mark_name')
    part_name = data.get('part_name')
    params = data.get('params', {})
    page = data.get('page', 1)

    query = Q(is_visible=True)

    if mark_name:
        query &= Q(mark__name__icontains=mark_name)

    if part_name:
        query &= Q(name__icontains=part_name)

    if 'color' in params:
        query &= Q(json_data__color=params['color'])

    if 'is_new_part' in params:
        query &= Q(json_data__is_new_part=params['is_new_part'])

    if 'price_gte' in data:
        query &= Q(price__gte=data['price_gte'])

    if 'price_lte' in data:
        query &= Q(price__lte=data['price_lte'])

    parts = Part.objects.filter(query)[(page-1)*10:page*10]
    total_count = Part.objects.filter(query).count()
    total_sum = Part.objects.filter(query).aggregate(Sum('price'))['price__sum']

    if total_sum is None:
        total_sum = '0'
    results = [
        {
            "mark": {"id": part.mark.id, "name": part.mark.name, "producer_country_name": part.mark.producer_country_name},
            "model": {"id": part.model.id, "name": part.model.name},
            "name": part.name,
            "json_data": part.json_data,
            "price": part.price
        }
        for part in parts
    ]

    return JsonResponse({"response": results, "count": total_count, "summ": float(total_sum)})