"""
ASGI config for exemplo_01 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
from dotenv import load_dotenv
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exemplo_01.settings')
load_dotenv()

application = get_asgi_application()
