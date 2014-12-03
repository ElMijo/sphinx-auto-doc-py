# -*- coding: utf8 -*-
"""Esta es una herramienta que permite autogenerardocumentación de python"""
import os
from helpers import *

__name__ = "Sphinx-AutoDoc"
__author__ = "Jerry Anselmi"
__author_email__ = "jerry.anselmi@gmail.com"
__description__ = "Esta es una herramienta que permite autogenerardocumentación de python"
__copyright__ = "Copyright (c) 2014 Jerry Anselmi"
__license__ = "MIT"
__version__ = "1.0"
__url_proyect__ = "https://github.com/ElMijo/sphinx-auto-doc-py"
__maintainer__ = __author__
__maintainer_email__ = __author_email__
__package_folder__ = os.path.abspath(os.path.dirname(__file__))
__proyect_folder__ = os.path.abspath(os.path.join(__package_folder__, '../'))
__config_folder__ = os.path.join(__package_folder__,'config/')


def importar_config(configfile):
	import codecs, json
	configfile = os.path.join(__config_folder__,configfile+'.json')
	config = None

	if (os.path.exists(configfile)):
		json_data = codecs.open(os.path.join(__config_folder__,configfile),'rU','utf-8').read()
		config = json.loads(json_data)
	
	return config

def ejecutar_comando(comando,*arg):
	os.system(comando.format(*arg))