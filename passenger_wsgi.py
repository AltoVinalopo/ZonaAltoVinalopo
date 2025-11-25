import os
import sys

project_home = '/var/www/vhosts/practical-kalam.82-165-173-231.plesk.page/httpdocs/coordinacion'

if project_home not in sys.path:
    sys.path.insert(0, project_home)

from app import app as application
