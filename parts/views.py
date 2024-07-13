from django.http import JsonResponse
from .models import Mark, Model


def mark_list(request):
    marks = list(Mark.objects.filter(is_visible=True).values('id', 'name', 'producer_country_name'))
    print(marks)
    return JsonResponse(marks, safe=False)


def model_list(request):
    models = list(Model.objects.filter(is_visible=True).values('id', 'name', 'mark_id'))
    return JsonResponse(models, safe=False)
