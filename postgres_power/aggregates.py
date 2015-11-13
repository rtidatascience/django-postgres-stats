from django.db.models import Aggregate


class Percentile(Aggregate):
    """
    Accepts a numerical field or expression and a list of fractions and
    returns values for each fraction given corresponding to that fraction in
    that expression.

    If *continuous* is True (the default), the value will be interpolated
    between adjacent values if needed. Otherwise, the value will be the first
    input value whose position in the ordering equals or exceeds the
    specified fraction.
    """

    function = None
    name = "percentile"
    template = "%(function)s(%(percentiles)s) WITHIN GROUP (ORDER BY %(" \
               "expressions)s)"

    def __init__(self, expression, percentiles, continuous=True, **extra):
        if isinstance(percentiles, (list, tuple)):
            percentiles = "array%(percentiles)s" % {'percentiles': percentiles}
        if continuous:
            extra['function'] = 'PERCENTILE_CONT'
        else:
            extra['function'] = 'PERCENTILE_DISC'
        super().__init__(expression, percentiles=percentiles, **extra)
