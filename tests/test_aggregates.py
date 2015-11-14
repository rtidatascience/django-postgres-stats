from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.test import TestCase

from postgres_stats import Percentile
from .models import Number


class TestAggregates(TestCase):
    def setUp(self):
        numbers = [31, 83, 237, 250, 305, 314, 439, 500, 520, 526, 527, 533,
                   540, 612, 831, 854, 857, 904, 928, 973]
        for n in numbers:
            Number.objects.create(n=n)

    def test_percentile_median(self):
        results = Number.objects.all().aggregate(
            median=Percentile('n', 0.5, output_field=models.FloatField()))
        assert results['median'] == 526.5

    def test_percentile_continuous(self):
        results = Number.objects.all().aggregate(
            quartiles=Percentile('n', [0.25, 0.5, 0.75],
                                 output_field=ArrayField(models.FloatField())))
        assert results['quartiles'] == [311.75, 526.5, 836.75]

    def test_percentile_not_continuous(self):
        results = Number.objects.all().aggregate(
            quartiles=Percentile('n', [0.25, 0.5, 0.75],
                                 continuous=False,
                                 output_field=ArrayField(models.FloatField())))
        assert results['quartiles'] == [305, 526, 831]

