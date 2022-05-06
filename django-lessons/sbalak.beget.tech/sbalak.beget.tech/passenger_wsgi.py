# -*- coding: utf-8 -*-

# /home/s/sbalak/sbalak.beget.tech/venv/lib/python3.8/site-packages/django/__init__.py

import os, sys
sys.path.insert(0, '/home/s/sbalak/sbalak.beget.tech/coolsite')
sys.path.insert(1, '/home/s/sbalak/sbalak.beget.tech/djangoenv/lib/python3.8/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'coolsite.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
