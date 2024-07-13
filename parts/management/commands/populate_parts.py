from django.core.management.base import BaseCommand
from parts.models import Mark, Model, Part
import random
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = 'Populate Part table with random data'

    def handle(self, *args, **kwargs):
        parts_names = ['Бампер', 'Фара', 'Капот', 'Дверь', 'Крыло']
        marks = list(Mark.objects.all())
        models = list(Model.objects.all())

        for _ in range(10000):
            part = Part(
                name=random.choice(parts_names),
                mark=random.choice(marks),
                model=random.choice(models),
                price=random.uniform(1000, 10000),
                json_data={
                    'color': fake.color_name() if random.choice([True, False]) else None,
                    'is_new_part': random.choice([True, False]) if random.choice([True, False]) else None,
                    'count': random.randint(0, 10) if random.choice([True, False]) else None,
                } if random.choice([True, False]) else None,
                is_visible=random.choice([True, False])
            )
            part.save()
