import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.core.management import call_command

call_command('makemigrations')
call_command('migrate')
call_command('collectstatic', '--noinput')

print("Migrations et fichiers statiques appliqués !")
