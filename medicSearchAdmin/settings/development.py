import os
#add gitignore

from .settings import *

DEBUG = True

SECRET_KEY = 'ixb62ha#ts=ab4t2u%p1_62-!5w2j==j6d^3-j$!z(@*m+-h'

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.sqlite3',
        "NAME": BASE_DIR / "db.sqlite3",
    }
}