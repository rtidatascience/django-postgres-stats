import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', 'django_postgres_power'),
        'USER': os.environ.get('DB_USER', 'django'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

INSTALLED_APPS = ['django_nose', 'tests']
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
SECRET_KEY = 'testkey'