# -*- coding: utf-8 -*-
import  os
from __future__ import unicode_literals

class FileDir(object):
	"""docstring for FileDir"""
	def __init__(self,ruta_archivo=''):
		self.__ruta_archivo__ = ruta_archivo if os.path.exists(ruta_archivo) else '.'

	@property
	def abspath():
	"""Devuelve una versión normalizada de la ruta absoluta del archivo o directorio"""
		return os.path.abspath(self.__ruta_archivo__)

	@property
	def basename():
	"""Devuelve el nombre base del archivo o directorio"""
		return os.path.basename(self.__ruta_archivo__)

	@property
	def dirname():
	"""Devuelve el nombre del directorio"""
		return os.path.dirname(self.__ruta_archivo__)

	@property
	def split():
	"""Devuelve un arreglo con del dirname y el base basename de la ruta del archivo o directorio"""
		return os.path.split(self.__ruta_archivo__)						

	@property
	def getatime():
	"""Devuelve el timestamp de la ultima vez que se acceso el archivo o directorio"""
		return os.path.getatime(self.__ruta_archivo__)	

	@property
	def getmtime():
	"""Devuelve el timestamp de la ultima modificación de el archivo o directorio"""
		return os.path.getmtime(self.__ruta_archivo__)	

	@property
	def getsize():
	"""Devuelve el tamaño del archivo o directorio en bytes"""
		return os.path.getsize(self.__ruta_archivo__)					

	@property
	def splitunc():
	"""Devuelve un arreglo con del dirname y el base basename de la ruta del archivo o directorio"""
		return os.path.splitunc(self.__ruta_archivo__)	

	@property
	def isfile():
	"""Valida si la ruta es de un archivo"""
		return os.path.isfile(self.__ruta_archivo__)

	@property
	def isdir():
	"""Valida si la ruta es de un directorio"""
		return os.path.isdir(self.__ruta_archivo__)

	@property
	def islink():
	"""Valida si la ruta es un enlace simbolico"""
		return os.path.islink(self.__ruta_archivo__)	

	@property
	def isabs():
	"""Valida si la ruta es absoluta"""
		return os.path.isabs(self.__ruta_archivo__)

	@property
	def ismount():
	"""Valida si la ruta es un punto de montaje"""
		return os.path.ismount(self.__ruta_archivo__)

	def get_files(ext='*'):
    """Esta función nos permite obtener los archivos de una determinada extención dentro de una ruta"""
    	lista_archivos = []

    	if self.isdir:
    		for raiz, directorios, archivos in os.walk(self.__ruta_archivo__):
        		for archivo in archivos:
            		if ext == '*' or archivo.endswith('.'+ext):
                		lista_archivos.append(os.path.join(raiz, archivo))

	    return lista_archivos


# class SphinxDocProjecto(FileDir):
# 	"""docstring for SphinxDocProject"""

# 	def __init__(self, ruta_proyecto):
# 		super(self.__class__, self).__init__(ruta_proyecto)

# 	@property
# 	def excluir_archivos():
# 		"""Devuel los patrones a excluir al momento de buscar un paquete"""
# 		return ["*.tests", "*.tests.*", "tests.*", "tests"]

# 	@property
# 	def __get_proyect_packages__():
# 		"""Devuelve una lista de todos los paquetes y sub-paquetes dentro del proyecto"""
# 		from setuptools import find_packages
# 		return find_packages(where=self.abspath,exclude=self.excluir_archivos)

# 	@property
# 	def __package_name__():
# 		"""Devuelve el nombre del paquete principal del proyecto"""
#     	import re
#     	paquete = None
#     	patron = re.compile('[.]')
#     	for item in self.__get_proyect_packages__:
#         	if patron.search(item) is None:
# 				paquete = item
#             	break

#     	return paquete

# 	@property
# 	def __package_path__():
# 		"""Devuelve la ruta absoluta del paquete principal del proyecto"""
# 		return os.path.join(self.abspath,self.__package_name__)

# 	@property
# 	def __doc_dir__():
# 		return os.path.join(self.abspath,'docs')


# 	def respaldar():
# 		"""Genera un archivo zip dentro del proyecto"""
# 		import tmpdir, shutil

# 		respaldo = False
# 		directorio_tempotal = tempfile.mkdtemp()

# 		try:

# 			archivo_temporal = os.path.join(tmpdir, self.basename+'_sphinxdoc_backup')
# 			archivo_zip = open(shutil.make_archive(archivo_temporal, 'zip', self.abspath), 'rb').read()
# 			respaldo = True			

# 		finally:

# 			shutil.rmtree(directorio_tempotal)

# 		return respaldo

# 	def generar_html_doc(ruta_origen):
#     	os.system("make -C %s html" % self.__doc_dir__)

#     def generar_api_doc():
#     """Esta función ejecuta el comando sphinx-apidoc de Sphinx para crear la documentación del API"""
#     	comando = 'sphinx-apidoc -F -o %s %s' % (self.__doc_dir__,self.__package_path__)
#     	os.system(comando)


