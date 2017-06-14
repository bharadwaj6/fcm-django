#!/usr/bin/env python
import fcm_django
from distutils.core import setup

VERSION = '0.0.3'

CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Web Environment",
    "Framework :: Django",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: System :: Networking",
]

setup(
    name="fcm-django-old",
    packages=[
        "fcm_django",
        "fcm_django/api",
        "fcm_django/migrations",
        "fcm_django/management",
        "fcm_django/management/commands",
    ],
    install_requires=[
        'pyfcm==1.2.3',
        'Django'
    ],
    author=fcm_django.__author__,
    author_email=fcm_django.__email__,
    classifiers=CLASSIFIERS,
    description="Send push notifications to mobile devices through FCM in Django. Old versions of Django supported.",
    download_url="https://github.com/bharadwaj6/fcm-django/tarball/master",
    long_description='',
    url="https://github.com/bharadwaj6/fcm-django",
    version=fcm_django.__version__,
)
