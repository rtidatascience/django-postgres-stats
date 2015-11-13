======================
Django Postgres Power
======================

Postgres Power exposes functions specific to Postgres to Django without
making the user write raw SQL. The plan is to expand the library over time
to cover all Postgres-specific functions. For now, only functions personally
used by the authors have been added.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "postgres_power" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'postgres_power',
    )

2. Import the functions you need to use with your models.