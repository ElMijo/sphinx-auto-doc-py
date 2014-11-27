# -*- coding: utf-8 -*-

# class ClassName(object):
#     """docstring for ClassName"""
#     def __init__(self, arg):
#         super(ClassName, self).__init__()
#         self.arg = arg
#         
from terminal_text_color import TextColor,AlertTextColor  

class SphinxDoc(object):
    def __init__(self, ruta_proyecto):
        self.tc = TextColor()
        self.atc = AlertTextColor()

# from helpers.utilitarios import pyment_files, backup_files,apply_patch, sphinx_quickstart, generate_api,crerate_api_folder,generate_html_doc,get_principal_package,sphinx_apidoc,add_package
# from pyment import PyComment
# from terminal_text_color import TextColor,AlertTextColor
# import os, sys

# proyecto = '../example-doc-project'
# package = get_principal_package(proyecto)
# #+'/trianglelib'

# tc = TextColor()

# if backup_files(proyecto):

#     archivos = pyment_files(proyecto)

#     print tc.default_cyan("Convirtiendo docstring en reStructuredText..")

#     for archivo in archivos:
#         c = PyComment(archivo['original'])
#         c.proceed()
#         c.diff_to_file(archivo['patch'])
#         apply_patch(archivo)

#     print tc.default_cyan("Creando documentación..")
#     sphinx_apidoc(proyecto,package)
#     print tc.default_cyan("Agregando el proyecto a la ayuda..")
#     add_package(proyecto)
#     print tc.bold_cyan("Generando la documentación del API...")
#     generate_api(proyecto,package)
#     print tc.bold_yellow("Generando la documentación HTML")
#     generate_html_doc(proyecto)