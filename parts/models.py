from django.db import models


class Mark(models.Model):
    name = models.CharField(max_length=100)
    producer_country_name = models.CharField(max_length=100)
    is_visible = models.BooleanField(default=True)


class Model(models.Model):
    name = models.CharField(max_length=100)
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)
    is_visible = models.BooleanField(default=True)


class Part(models.Model):
    name = models.CharField(max_length=100)
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    json_data = models.JSONField(default=dict)
    is_visible = models.BooleanField(default=True)
