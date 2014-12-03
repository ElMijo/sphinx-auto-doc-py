# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import  os

class FileDir(object):
    """docstring for FileDir"""
    def __init__(self,ruta_archivo=''):
        self.__ruta_archivo__ = ruta_archivo if os.path.exists(ruta_archivo) else '.'

    @property
    def abspath(self):
        """Devuelve una versión normalizada de la ruta absoluta del archivo o directorio"""
        return os.path.abspath(self.__ruta_archivo__)

    @property
    def basename(self):
        """Devuelve el nombre base del archivo o directorio"""
        return os.path.basename(self.__ruta_archivo__)

    @property
    def dirname(self):
        """Devuelve el nombre del directorio"""
        return os.path.dirname(self.__ruta_archivo__)

    @property
    def split(self):
        """Devuelve un arreglo con del dirname y el base basename de la ruta del archivo o directorio"""
        return os.path.split(self.__ruta_archivo__)                     

    @property
    def getatime(self):
        """Devuelve el timestamp de la ultima vez que se acceso el archivo o directorio"""
        return os.path.getatime(self.__ruta_archivo__)  

    @property
    def getmtime(self):
        """Devuelve el timestamp de la ultima modificación de el archivo o directorio"""
        return os.path.getmtime(self.__ruta_archivo__)  

    @property
    def getsize(self):
        """Devuelve el tamaño del archivo o directorio en bytes"""
        return os.path.getsize(self.__ruta_archivo__)                   

    @property
    def splitunc(self):
        """Devuelve un arreglo con del dirname y el base basename de la ruta del archivo o directorio"""
        return os.path.splitunc(self.__ruta_archivo__)  

    @property
    def isfile(self):
        """Valida si la ruta es de un archivo"""
        return os.path.isfile(self.__ruta_archivo__)

    @property
    def isdir(self):
        """Valida si la ruta es de un directorio"""
        return os.path.isdir(self.__ruta_archivo__)

    @property
    def islink(self):
        """Valida si la ruta es un enlace simbolico"""
        return os.path.islink(self.__ruta_archivo__)    

    @property
    def isabs(self):
        """Valida si la ruta es absoluta"""
        return os.path.isabs(self.__ruta_archivo__)

    @property
    def ismount(self):
        """Valida si la ruta es un punto de montaje"""
        return os.path.ismount(self.__ruta_archivo__)

    @property
    def content(self):
        """Permite ontener el contenido de un archivo"""
        return open(self.abspath, 'r').read()

    @property
    def content_lines(self):
        """Permite ontener el contenido de un archivo"""
        return open(self.abspath, 'r').readlines()

    def get_files(self,ext='*'):
        """Esta función nos permite obtener los archivos de una determinada extención dentro de una ruta"""
        lista_archivos = []

        if self.isdir:
            for raiz, directorios, archivos in os.walk(self.__ruta_archivo__):
                for archivo in archivos:
                    if ext == '*' or archivo.endswith('.'+ext):
                        lista_archivos.append(os.path.join(raiz, archivo))

        return lista_archivos

    def replace_line(self, linea, texto):

        replace = False

        try:
            if self.isfile:
                lineas = open(self.abspath, 'r').readlines()
                lineas[linea] = texto
                out = open(self.abspath, 'w')
                out.writelines(lineas)
                out.close()
                replace = True

        except:
            pass
        
        return replace

    def append_after_line(self,line,texto):
        append = False

        try:
            if self.isfile:
                lineas = open(self.abspath, 'r').readlines()
                lineas[linea] = texto
                out = open(self.abspath, 'w')
                out.writelines(lineas)
                out.close()
                append = True

        except:
            pass
        
        return append

# def add_extensions(archivo):
#     from string import find
#     lines = open(archivo,"r").readlines()
#     ext = [
#         "'sphinx.ext.autodoc',\n",
#         "'sphinx.ext.doctest',\n",
#         "'sphinx.ext.mathjax',\n",
#         "'sphinx.ext.viewcode',\n"
#     ]
#     inx_init = 0
#     inx_end = 0
#     for inx,val in enumerate(lines):
#         if  find(val,'extensions = [')>-1:
#             inx_init = inx
#             continue
#         elif find(val,']') > -1:
#             inx_end = inx
#             break

#     lines = lines[:inx_init+1]+ext+lines[inx_end:]
#     out = open(archivo, 'w')
#     out.writelines(lines)
#     out.close()        



        
        
        
        


# class SphinxDocProjecto(FileDir):
#       """docstring for SphinxDocProject"""

#   def __init__(self, ruta_proyecto):
#       super(self.__class__, self).__init__(ruta_proyecto)

#   @property
#   def excluir_archivos(self):
#       """Devuel los patrones a excluir al momento de buscar un paquete"""
#       return ["*.tests", "*.tests.*", "tests.*", "tests"]

#   @property
#   def __get_proyect_packages__():
#       """Devuelve una lista de todos los paquetes y sub-paquetes dentro del proyecto"""
#       from setuptools import find_packages
#       return find_packages(where=self.abspath,exclude=self.excluir_archivos)

#   @property
#   def __package_name__():
#       """Devuelve el nombre del paquete principal del proyecto"""
#       import re
#       paquete = None
#       patron = re.compile('[.]')
#       for item in self.__get_proyect_packages__:
#           if patron.search(item) is None:
#               paquete = item
#               break

#       return paquete

#   @property
#   def __package_path__():
#       """Devuelve la ruta absoluta del paquete principal del proyecto"""
#       return os.path.join(self.abspath,self.__package_name__)

#   @property
#   def __doc_dir__():
#       return os.path.join(self.abspath,'docs')


#   def respaldar():
#       """Genera un archivo zip dentro del proyecto"""
#       import tmpdir, shutil

#       respaldo = False
#       directorio_tempotal = tempfile.mkdtemp()

#       try:

#           archivo_temporal = os.path.join(tmpdir, self.basename+'_sphinxdoc_backup')
#           archivo_zip = open(shutil.make_archive(archivo_temporal, 'zip', self.abspath), 'rb').read()
#           respaldo = True         

#       finally:

#           shutil.rmtree(directorio_tempotal)

#       return respaldo

#   def generar_html_doc(ruta_origen):
#       os.system("make -C %s html" % self.__doc_dir__)

#     def generar_api_doc():
#     """Esta función ejecuta el comando sphinx-apidoc de Sphinx para crear la documentación del API"""
#       comando = 'sphinx-apidoc -F -o %s %s' % (self.__doc_dir__,self.__package_path__)
#       os.system(comando)


