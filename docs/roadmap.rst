Roadmap
=======

In general, we want to create the ability to use Postgres functions that will
give us better statistical methods. If a function can be easily accessed using
`Func`_, we do not need to implement it.

Next functions
--------------
* mode
* width_bucket
* `corr, covar, and regr functions`_

After we have the set of functions, we can begin to introduce other parts of
Postgres that are not yet available in Django.

Possible additions
------------------
* `OVERLAPS operator`_
* `Range types`_
* `Window functions`_

.. _Func: https://docs.djangoproject.com/en/1.8/ref/models/expressions/#func-expressions
.. _OVERLAPS operator: http://www.postgresql.org/docs/9.4/static/functions-datetime.html
.. _Range types: http://www.postgresql.org/docs/9.4/static/rangetypes.html
.. _corr, covar, and regr functions: http://www.postgresql.org/docs/9.4/static/functions-aggregate.html#FUNCTIONS-AGGREGATE-STATISTICS-TABLE
.. _Window functions: http://www.postgresql.org/docs/9.4/static/tutorial-window.html