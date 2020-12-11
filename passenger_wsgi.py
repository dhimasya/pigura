import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

import odoo
conf = odoo.tools.config

# ???
# odoo.multi_process = True # Nah!

# Database
conf['db_host'] = 'localhost'
conf['db_port'] = 5432
conf['db_user'] = 'user'
conf['db_password'] = 'pass'
conf['db_name'] = 'db'

# Modules
# conf['addons_path'] = '/addons/path,/other/addons/path'

# Debugging
# conf['dev'] = 'reload,qweb,werkzeug,xml'

# WSGI Entrypoint
application = odoo.service.wsgi_server.application