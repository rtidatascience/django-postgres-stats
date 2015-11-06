from django.db.models import Aggregate, Func


class DateTrunc(Func):
    """
    Truncates a timestamp to a specified precision. This is useful for
    investigating time series.

    The `precision` named parameter can take:

    * microseconds
    * milliseconds
    * second
    * minute
    * hour
    * day
    * week
    * month
    * quarter
    * year
    * decade
    * century
    * millennium
    """

    function = "DATE_TRUNC"
    template = "%(function)s('%(precision)s', %(expressions)s)"

    def __init__(self, expression, precision, **extra):
        super().__init__(expression, precision=precision, **extra)


class Extract(Func):
    """
    Get a subfield of a timestamp or an interval. This is useful for grouping
    data.

    The `subfield` named parameter can take:

    * century
    * day
    * decade
    * dow (day of week)
    * doy (day of year)
    * epoch (seconds since 1970-01-01 00:00:00 UTC)
    * hour
    * isodow
    * isodoy
    * isoyear
    * microseconds
    * millennium
    * milliseconds
    * minute
    * month
    * quarter
    * second
    * timezone
    * timezone_hour
    * timezone_minute
    * week
    * year

    See `the Postgres documentation`_ for details about the subfields.

    .. _the Postgres documentation: http://www.postgresql.org/docs/current/static/functions-datetime.html#FUNCTIONS-DATETIME-EXTRACT
    """
    function = 'EXTRACT'
    name = 'extract'
    template = "%(function)s(%(subfield)s FROM %(expressions)s)"

    def __init__(self, expression, subfield, **extra):
        super().__init__(expression, subfield=subfield, **extra)


class Percentile(Aggregate):
    """
    Returns values for each fraction given corresponding to that fraction in
    the ordered expression.

    If ``continuous`` is True (the default), the value will be interpolated
    between adjacent values if needed. Otherwise, the value will be the first
    input value whose position in the ordering equals or exceeds the specified
    fraction.
    """

    function = None
    name = "percentile"
    template = "%(function)s(%(percentiles)s) WITHIN GROUP (ORDER BY %(expressions)s)"

    def __init__(self, expression, percentiles, continuous=True, **extra):
        if isinstance(percentiles, (list, tuple)):
            percentiles = "array%(percentiles)s" % {'percentiles': percentiles}
        if continuous:
            extra['function'] = 'PERCENTILE_CONT'
        else:
            extra['function'] = 'PERCENTILE_DISC'
        super().__init__(expression, percentiles=percentiles, **extra)
