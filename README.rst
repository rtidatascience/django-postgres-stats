======================
Django Postgres Stats
======================

Django Postgres Stats exposes statistical and datetime functions specific to
Postgres to Django without making the user write raw SQL. The plan is to
expand the library over time to cover many Postgres-specific functions. For
now, only functions personally used by the authors have been added.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "postgres_stats" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'postgres_stats',
    )

2. Import the functions you need to use with your models.