Installation instructions
=========================

Download and installation
-------------------------

Installation with pip
^^^^^^^^^^^^^^^^^^^^^

You can use pip to install django-postgres-stats::

  $ pip install django-postgres-stats


Using in Django
^^^^^^^^^^^^^^^

You will need to add the *postgres_stats* application to the INSTALLED_APPS
setting of your Django project *settings.py* file.::

    INSTALLED_APPS = (
        ...
        'postgres_stats',
    )


Version control
---------------

Django Postgres Stats is hosted on GitHub::

  https://github.com/rtidatascience/django-postgres-stats