from django.urls import path
from .views import model_list, mark_list, search_parts


app_name = 'parts'

urlpatterns = [
    path('models', model_list, name='models'),
    path('marks', mark_list, name='marks'),
    path('search', search_parts, name='search'),
]