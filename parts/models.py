from django.db import models
from django.contrib.postgres.indexes import GinIndex
from django.db.models import Q, F


class Mark(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    producer_country_name = models.CharField(max_length=100, db_index=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['producer_country_name']),
        ]


class Model(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE, db_index=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['mark']),
        ]


class Part(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE, db_index=True)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    json_data = models.JSONField(default=dict, null=True, blank=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['mark']),
            models.Index(fields=['model']),
            models.Index(fields=['is_visible']),
        ]
