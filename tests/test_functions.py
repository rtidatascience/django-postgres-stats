from django.test import TestCase
from datetime import datetime

from postgres_stats import DateTrunc, Extract
from .models import Checkin


class TestFunctions(TestCase):
    def test_date_trunc(self):
        _checkin = Checkin.objects.create(logged_at='2015-11-01 11:14:01')
        checkin = Checkin.objects. \
            annotate(day=DateTrunc('logged_at', 'day'),
                     hour=DateTrunc('logged_at', 'hour')). \
            get(pk=_checkin.pk)

        assert checkin.day == datetime(2015, 11, 1, 0, 0, 0)
        assert checkin.hour == datetime(2015, 11, 1, 11, 0, 0)

    def test_extract(self):
        _checkin = Checkin.objects.create(logged_at='2015-11-03 11:45:02')
        checkin = Checkin.objects. \
            annotate(day=Extract('logged_at', 'day'),
                     hour=Extract('logged_at', 'second'),
                     quarter=Extract('logged_at', 'quarter')). \
            get(pk=_checkin.pk)

        assert checkin.day == 3
        assert checkin.hour == 2
        assert checkin.quarter == 4
