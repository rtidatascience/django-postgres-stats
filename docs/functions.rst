Postgres functions
==================

Database functions
------------------

You can use these like the standard `Django database functions`_.

.. autoclass:: postgres_stats.functions.DateTrunc

.. autoclass:: postgres_stats.functions.Extract


Aggregations
------------

You can use these like the standard `Django aggregations`_.

.. autoclass:: postgres_stats.aggregates.Percentile


.. _Django database functions: https://docs.djangoproject.com/en/1.8/ref/models/database-functions/
.. _Django aggregations: https://docs.djangoproject.com/en/1.8/topics/db/aggregation/