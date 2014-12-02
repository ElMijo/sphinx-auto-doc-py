# -*- coding: utf-8 -*-

# class ClassName(object):
#     """docstring for ClassName"""
#     def __init__(self, arg):
#         super(ClassName, self).__init__()
#         self.arg = arg
#        
from __future__ import unicode_literals
from helpers.files import FileDir
from pyment import PyComment
from . import ejecutar_comando as cmd

class SphinxDocProjecto(FileDir):
    """docstring for SphinxDocProject"""

    def __init__(self, ruta_proyecto):
        super(self.__class__, self).__init__(ruta_proyecto)

    @property
    def excluir_archivos(self):
        """Devuel los patrones a excluir al momento de buscar un paquete"""
        return ["*.tests", "*.tests.*", "tests.*", "tests"]

    @property
    def __get_proyect_packages__(self):
        """Devuelve una lista de todos los paquetes y sub-paquetes dentro del proyecto"""
        from setuptools import find_packages
        return find_packages(where=self.abspath,exclude=self.excluir_archivos)

    @property
    def __package_name__(self):
        """Devuelve el nombre del paquete principal del proyecto"""
        import re
        paquete = None
        patron = re.compile('[.]')
        for item in self.__get_proyect_packages__:
            if patron.search(item) is None:
                paquete = item
                break

        return paquete

    @property
    def __package_path__(self):
        """Devuelve la ruta absoluta del paquete principal del proyecto"""
        import os
        return os.path.join(self.abspath,self.__package_name__)

    @property
    def __doc_dir__(self):
        import os
        return os.path.join(self.abspath,'docs')

    @property
    def __doc_config__(self):
        import os
        return os.path.join(self.abspath,'docs','conf.py')

    def respaldar(self):
        """Genera un archivo zip dentro del proyecto"""
        import tempfile, shutil, os

        respaldo = False
        directorio_tempotal = tempfile.mkdtemp()

        try:

            archivo_temporal = os.path.join(directorio_tempotal, self.basename+'_sphinxdoc_backup')
            zip_temporal = shutil.make_archive(archivo_temporal, 'zip', self.abspath)
            zip_proyecto = os.path.join(self.abspath,os.path.basename(zip_temporal))

            open(zip_temporal, 'rb').read()

            if os.path.exists(zip_proyecto):
                os.remove(zip_proyecto)

            shutil.move(zip_temporal,self.abspath)
            respaldo = True         
        except:
            pass
        finally:
            shutil.rmtree(directorio_tempotal)

        return respaldo

    def generar_html_doc(self,ruta_origen):
        os.system("make -C %s html" % self.__doc_dir__)

    def generar_docstring_rst(self):
        """Esta función permite estructurar una lista de archivos obtimos para utilizar los comandos de Pyment"""
        for f in self.get_files('py'):
            fpatch = f+".patch"
            c = PyComment(f)
            c.proceed()
            c.diff_to_file(fpatch)
            cmd("patch {0} {1}",f,fpatch)
            cmd("rm {0}",fpatch)

    def generar_api_doc(self):
        """Esta función ejecuta el comando sphinx-apidoc de Sphinx para crear la documentación del API"""
        cmd("sphinx-apidoc -F -o {0} {1}",self.__doc_dir__,self.__package_path__)

    def configurar_documentacion(self):

        config = FileDir(self.__doc_config__)
        texto = 'sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../"))\n\n'
        config.replace_line(17,texto)
        
        # add_extensions(archivo)
        # remove_epub_options(archivo)        





# class SphinxDoc(SphinxDocProjecto):
#     def __init__(self, ruta_proyecto):
#         self.tc = TextColor()
#         self.atc = AlertTextColor()

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