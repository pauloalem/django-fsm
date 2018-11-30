PROJECT_APPS = ('django_fsm', 'testapp',)
INSTALLED_APPS = ('django.contrib.contenttypes', 'django.contrib.auth', 'guardian', ) + PROJECT_APPS
DATABASE_ENGINE = 'sqlite3'
SECRET_KEY = 'nokey'
MIDDLEWARE_CLASSES = ()
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend'
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        }
}

ANONYMOUS_USER_ID = 0
