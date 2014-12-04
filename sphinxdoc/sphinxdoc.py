# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os, re
from helpers.files import File, Dir
from pyment import PyComment
from . import ejecutar_comando as cmd

class SphinxDocProjecto(Dir):
    """docstring for SphinxDocProject"""

    __SPHINX_EXT__ = [
        'sphinx.ext.autodoc',
        'sphinx.ext.doctest',
        'sphinx.ext.mathjax',
        'sphinx.ext.viewcode'
    ]

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
        return os.path.join(self.abspath,self.__package_name__)

    @property
    def __doc_dir__(self):
        return os.path.join(self.abspath,'docs')

    @property
    def __doc_config_path__(self):
        return os.path.join(self.abspath,'docs','conf.py')

    @property
    def __sphinx_ext_parse__(self):
        return ["'"+item+"',\n" for item in self.__SPHINX_EXT__]

    @property
    def __index_build_html_doc__(self):
        return os.path.join(self.abspath,'docs','_build','html','index.html')


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
        self.__doc_config_file__ = File(self.__doc_config_path__)


    def agregar_package_path_to_conf_doc(self):
        """Agrega la ruta del package al archivo de configuración"""
        agregar = False

        if self.__doc_config_file__.isfile:
            line = 'sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../"))\n\n'
            nline = self.__doc_config_file__.serach_line_by_text('#sys.path.insert',result=1)
            self.__doc_config_file__.replace_line(nline,line)

        return agregar

    def agregar_plugins_to_conf_doc(self):
        """Agrega los plugins por defecto a la configuración de la ayuda"""
        agregar = False
        init = self.__doc_config_file__.serach_line_by_text('extensions = [',result=1)
        end = self.__doc_config_file__.serach_line_by_text(']',init=init,result=1)
        if self.__doc_config_file__.remove_lines_between(init,end):
            agregar = self.__doc_config_file__.append_lines_after_line(init,self.__sphinx_ext_parse__)
        
        return agregar

    def eliminar_epub_to_config_doc(self):
        """Elimina la configuración epub que genera por defecto el comando sphinx-apidoc"""
        init = self.__doc_config_file__.serach_line_by_text('# -- Options for Epub output',result=1)
        return self.__doc_config_file__.remove_lines_between(init)

    def agregar_sphinx_rtd_theme(self):
        """Agrega el tema sphinx_rtd_theme como tema por defecto"""
        nline = self.__doc_config_file__.serach_line_by_text('import os',result=1)
        self.__doc_config_file__.append_lines_after_line(nline,['import sphinx_rtd_theme\n'])
        
        nline = self.__doc_config_file__.serach_line_by_text('html_theme =',result=1)
        self.__doc_config_file__.replace_line(nline,"html_theme = 'sphinx_rtd_theme'")
        
        nline = self.__doc_config_file__.serach_line_by_text('html_theme_path =',result=1)
        self.__doc_config_file__.replace_line(nline,"html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]")
    

    def agregar_modules_rst(self):
        """agrega la documentación rst por modulos al api"""
        cmd("python ./script/generate_modules -d {0} -s rst -f {1}",self.__doc_dir__,self.__package_path__)

        for item in self.get_files(ext='rst'):
            rstfile = File(item)
            if rstfile.basename == 'modules.rst':
                rstfile.remove()
            else:
                rstfile.strip_end_lines()

    def generar_html_doc(self):
        """Genera la documentacion en formato html"""
        cmd("make -C {0} html",self.__doc_dir__)

    def open_html_doc(self):
        """Permite ver la documentación desde su navegador"""
        import webbrowser
        webbrowser.open(self.__index_build_html_doc__)
