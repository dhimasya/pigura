import imp
import os
import sys


sys.path.insert(0, os.path.dirname(__file__))

import odoo

#----------------------------------------------------------
# Common
#----------------------------------------------------------
# odoo.multi_process = True # Nah!

# Equivalent of --load command-line option
odoo.conf.server_wide_modules = ['base', 'web']
conf = odoo.tools.config

# Path to the OpenERP Addons repository (comma-separated for
# multiple locations)

# conf['addons_path'] = '../../addons/trunk,../../web/trunk/addons'

# Optional database config if not using local socket
conf['db_host'] = 'localhost'
conf['db_name'] = 'name'
conf['db_user'] = 'user'
conf['db_port'] = 5432
conf['db_password'] = 'pass'

#----------------------------------------------------------
# Generic WSGI handlers application
#----------------------------------------------------------
application = odoo.service.wsgi_server.application
