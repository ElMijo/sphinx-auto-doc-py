# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os, shutil
from terminal_text_color import TextColor,AlertTextColor

def obtener_mensaje(id_mensaje):
    """Función que permite ontener un mesaje predeterminado por id del mensaje"""
    from .mensajes import __mensajes__ as msj

    return msj.get(id_mensaje,"")













# def get_files(ruta_origen,ext='py'):
#     """Esta función nos permite obtener los archivos de una determinada extención dentro de una ruta"""
#     cfiles = []
#     for root, dirs, files in os.walk(ruta_origen):
#         for file in files:
#             if file.endswith('.'+ext):
#                 cfiles.append(os.path.join(root, file))

#     return cfiles

# def zip_dir(ruta_origen,ruta_destino):
#     """Esta función permite crear un archivo .zip de una carpeta"""
#     try:
#         shutil.make_archive(ruta_destino, 'zip', ruta_origen)
#     except EnvironmentError:
#         return False
#     else:
#         return True    

# def abspath(ruta_origen):
#     """Esta función permite obtener la ruta absoluta de un path"""
#     return os.path.abspath(ruta_origen)

# def basename(ruta_origen):
#     """Esta función permite obtener el nombre base de la ruta espesificada"""
#     return os.path.basename(ruta_origen)

# def move(ruta_origen,ruta_destino):
#     """Esta función permite mover un archivo o directorio a otra locación"""
#     try:
#         shutil.move(ruta_origen,ruta_destino)
#     except EnvironmentError:
#         return False
#     else:
#         return True

# def backup_files(ruta_origen):
#     """Esta función nos permite crear aun archivo zip de respaldo del proyecto donde se esta creando la ddocumentación"""
#     respuesta = False
#     archivos = get_files(ruta_origen)
#     zipname = './'+basename(ruta_origen)
#     zipfilename = zipname+'.zip'
#     backupfilename = abspath(ruta_origen)+'/'+zipfilename
#     tc = TextColor()
#     atc= AlertTextColor()

#     print tc.default_cyan("Creando backup de del proyecto...")

#     if zip_dir(ruta_origen,zipname):

#         if move(zipfilename,backupfilename):

#             respuesta = True

#             print tc.default_green("Backup creado..")

#         else:

#             atc.error("No se Pudo mover el Archivo de Respaldos .zip a la carpeta destino")

#     else:

#         atc.error("No se Pudo crear el Archivo de Respaldos .zip")

#     return respuesta



# def sphinx_quickstart(ruta_origen):
#     """Esta función ejecuta el comando sphinx-quickstart de Sphinx para crear la documentación por primera vez"""
#     os.system("sphinx-quickstart "+ruta_origen+"/docs")

# def sphinx_apidoc(ruta_origen,package):
#     """Esta función ejecuta el comando sphinx-apidoc de Sphinx para crear la documentación del API"""
#     ruta_package = ruta_origen+'/'+package
#     ruta_docs = ruta_origen+'/docs'
#     os.system('sphinx-apidoc -F -o '+ruta_docs+' '+ruta_package)




# def crerate_api_folder(directorio):
#     if not os.path.exists(directorio):
#         os.makedirs(directorio)

# def generate_html_doc(ruta_origen):
#     pwd = os.getcwd()
#     docfolder = ruta_origen+'/docs'
#     os.system("make -C %s html" % docfolder)

# def get_principal_package(ruta_origen):
#     import re
#     from setuptools import find_packages
#     principal_package = None
#     patron = re.compile('[.]')
#     list_packages = find_packages(where=ruta_origen,exclude=["*.tests", "*.tests.*", "tests.*", "tests"])
#     for item in list_packages:
#         if  patron.search(item) is None:
#             principal_package = item
#             break

#     return principal_package
     
# def pyment_files(ruta_origen):
#     """Esta función permite estructurar una lista de archivos obtimos para utilizar los comandos de Pyment"""
#     files = []
#     for f in get_files(ruta_origen):
#         files.append(dict(original=f,patch=f+".patch"))

#     return files
#     
#               

# def apply_patch(archivo):
#     """Esta función aplica los patch generados por Pymet"""
#     os.system("patch "+archivo['original']+" "+archivo['patch'])
#     os.system("rm "+archivo['patch'])
#     
#
# def add_package(ruta_origen):
#     texto = 'sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../"))\n'
#     archivo = ruta_origen+"/docs/conf.py"
#     replace_line(archivo, 17, texto)
#     add_extensions(archivo)
#     remove_epub_options(archivo)
# def replace_line(archivo, linea, texto):
#     lines = open(archivo, 'r').readlines()
#     lines[linea] = texto
#     out = open(archivo, 'w')
#     out.writelines(lines)
#     out.close()
#     
#     
#     
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
#####Inicio de los metodos pendientes#####     





# def remove_end_black_line(archivo):
#     text = open(archivo).read().strip()
#     open('copia.rst', "w").write(text)




# def add_api_doc(ruta_origen): 
#     archivo = ruta_origen+'/index.rst'
#     lines = open(archivo, 'r').readlines()
#     line = None
#     for inx, val in enumerate(lines):
#         if val.find('maxdepth')>=0:
#             line = inx + 2
#             break

#     if line:
#         replace_line(archivo, line, '   modules\n\n')

# def generate_api(ruta_origen,package):
#     apifolder = abspath(ruta_origen+'/docs')
#     packfolder = abspath(ruta_origen+'/'+package)
#     #crerate_api_folder(apifolder)
#     os.system("python ./sphinxdoc/script/generate_modules -d "+apifolder+" -s rst -f "+packfolder)
#     add_api_doc(apifolder)
#     for archivo in get_files(apifolder,ext='rst'):
#         remove_end_black_line(archivo)




# def remove_epub_options(archivo):
#     from string import find
#     lines = open(archivo,"r").readlines()
#     for inx,val in enumerate(lines):
#         if  find(val,'Options for Epub output')>-1:
#             lines = lines[:inx]
#             break

#     out = open(archivo, 'w')
#     out.writelines(lines)
#     out.close()