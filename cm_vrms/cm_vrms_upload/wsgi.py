"""
WSGI config for cm_vrms_upload project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
#sys.path.append('/home/bea/app/httpd/cm_vrms/')
#sys.path.append('/home/bea/app/httpd/cm_vrms/cm_vrms_upload/')
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cm_vrms_upload.settings")

application = get_wsgi_application()
